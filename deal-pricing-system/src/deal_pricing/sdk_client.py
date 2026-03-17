"""Claude Code CLI client wrapper for Max subscription support.

Uses the Claude Code CLI directly, allowing the deal pricing system to
leverage Claude Max subscription instead of API credits.

Usage:
    1. Install Claude Code: curl -fsSL https://claude.ai/install.sh | bash
    2. Run `claude login` to authenticate with your Max subscription
    3. Set CLAUDE_CODE_OAUTH_TOKEN in .env (from `claude setup-token`)
"""

from __future__ import annotations

import asyncio
import os
import subprocess
from typing import Any, Dict, Optional


class SDKClient:
    """Client wrapper that uses Claude Code CLI.

    Uses Claude Code's OAuth authentication to leverage Max subscription
    instead of direct API billing.
    """

    def __init__(self, oauth_token: Optional[str] = None):
        self._oauth_token = oauth_token
        self._claude_path = self._find_claude_binary()

    def _find_claude_binary(self) -> str:
        """Find the Claude Code CLI binary."""
        paths_to_check = [
            os.path.expanduser("~/.local/bin/claude"),
            "/usr/local/bin/claude",
            os.path.expanduser("~/Library/Application Support/Claude/bin/claude"),
        ]

        for path in paths_to_check:
            if os.path.isfile(path) and os.access(path, os.X_OK):
                return path

        try:
            result = subprocess.run(
                ["which", "claude"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except Exception:
            pass

        raise RuntimeError(
            "Claude Code CLI not found. Install it with:\n"
            "curl -fsSL https://claude.ai/install.sh | bash"
        )

    async def create_message(
        self,
        system_prompt: str,
        user_prompt: str,
        model: str = "claude-sonnet-4-20250514",
        max_tokens: int = 4096,
    ) -> Dict[str, Any]:
        """Send a message using the Claude Code CLI.

        Args:
            system_prompt: System instructions for Claude
            user_prompt: User message/prompt
            model: Model to use
            max_tokens: Maximum tokens in response

        Returns:
            Response dict with 'content' and 'stop_reason'
        """
        env = os.environ.copy()
        if self._oauth_token:
            env["CLAUDE_CODE_OAUTH_TOKEN"] = self._oauth_token

        try:
            result = await asyncio.to_thread(
                self._run_claude_cli,
                system_prompt,
                user_prompt,
                model,
                env,
            )

            if result.returncode != 0:
                error_msg = result.stderr or "Unknown error"
                raise RuntimeError(f"Claude CLI failed: {error_msg}")

            response_text = result.stdout.strip()

            return {
                "content": [{"type": "text", "text": response_text}],
                "stop_reason": "end_turn",
                "model": model,
            }

        except subprocess.TimeoutExpired:
            raise RuntimeError("Claude CLI timed out after 5 minutes")
        except Exception as e:
            raise RuntimeError(f"CLI execution failed: {str(e)}") from e

    def _run_claude_cli(
        self,
        system_prompt: str,
        user_prompt: str,
        model: str,
        env: dict,
    ) -> subprocess.CompletedProcess:
        """Run Claude CLI with system prompt flag and user prompt via stdin.

        Tools disabled (--tools '') for single-turn text-only response.
        """
        process = subprocess.Popen(
            [
                self._claude_path,
                "--print",
                "--model", model,
                "--system-prompt", system_prompt,
                "--tools", "",
                "--max-turns", "1",
                "--no-session-persistence",
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        try:
            stdout, stderr = process.communicate(input=user_prompt, timeout=300)
            return subprocess.CompletedProcess(
                args=process.args,
                returncode=process.returncode,
                stdout=stdout,
                stderr=stderr,
            )
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
            raise


def get_sdk_client(oauth_token: Optional[str] = None) -> SDKClient:
    """Factory function to create an SDK client."""
    token = oauth_token or os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")
    if not token:
        raise ValueError(
            "No OAuth token provided. Run `claude setup-token` and set "
            "CLAUDE_CODE_OAUTH_TOKEN in your .env file."
        )
    return SDKClient(token)
