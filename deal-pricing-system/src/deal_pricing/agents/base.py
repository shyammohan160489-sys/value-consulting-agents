"""Base agent class for the Deal Pricing system."""

from __future__ import annotations

import json
import re
from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel

from ..config import get_settings

T = TypeVar("T", bound=BaseModel)


class AgentResult(BaseModel):
    """Result from an agent execution."""

    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    reasoning: Optional[str] = None


def _create_client(settings):
    """Create the appropriate client based on configuration."""
    client_mode = settings.get_effective_client_mode()

    if client_mode == "sdk":
        from ..sdk_client import SDKClient
        return SDKClient(settings.claude_code_oauth_token), "sdk"
    else:
        import anthropic
        return anthropic.Anthropic(api_key=settings.anthropic_api_key), "api"


class BaseAgent(ABC, Generic[T]):
    """Base class for all deal pricing agents.

    Supports two client modes:
    - 'api': Direct Anthropic API (requires API key and credits)
    - 'sdk': Claude Code CLI (uses Max subscription via OAuth token)
    """

    def __init__(
        self,
        name: str,
        description: str,
        output_model: Optional[type[T]] = None,
    ):
        self.name = name
        self.description = description
        self.output_model = output_model
        self._settings = get_settings()
        self._client, self._client_mode = _create_client(self._settings)

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """System prompt defining the agent's role and capabilities."""
        pass

    @abstractmethod
    def build_prompt(self, **kwargs) -> str:
        """Build the user prompt from input parameters."""
        pass

    async def execute(self, **kwargs) -> AgentResult:
        """Execute the agent's task."""
        try:
            user_prompt = self.build_prompt(**kwargs)

            if self._client_mode == "sdk":
                return await self._execute_with_sdk(user_prompt)
            else:
                return await self._execute_with_api(user_prompt)

        except Exception as e:
            return AgentResult(success=False, error=f"Unexpected error: {str(e)}")

    async def _execute_with_api(self, user_prompt: str) -> AgentResult:
        """Execute using direct Anthropic API."""
        import anthropic

        try:
            response = self._client.messages.create(
                model=self._settings.claude_model,
                max_tokens=4096,
                system=self.system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
            )
            return self._process_response(response)

        except anthropic.APIError as e:
            return AgentResult(success=False, error=f"API error: {str(e)}")

    async def _execute_with_sdk(self, user_prompt: str) -> AgentResult:
        """Execute using Claude Code CLI (Max subscription)."""
        try:
            response = await self._client.create_message(
                system_prompt=self.system_prompt,
                user_prompt=user_prompt,
                model=self._settings.claude_model,
                max_tokens=4096,
            )

            text_content = ""
            for block in response.get("content", []):
                if block.get("type") == "text":
                    text_content += block.get("text", "")

            data = None
            if self.output_model and text_content:
                data = self._extract_structured_data(text_content)

            return AgentResult(
                success=True,
                data=data,
                reasoning=text_content,
            )

        except Exception as e:
            return AgentResult(success=False, error=f"SDK error: {str(e)}")

    def _process_response(self, response) -> AgentResult:
        """Process Claude's response into an AgentResult."""
        text_content = ""

        if isinstance(response, dict):
            for block in response.get("content", []):
                if isinstance(block, dict) and block.get("type") == "text":
                    text_content += block.get("text", "")
        else:
            for block in response.content:
                if block.type == "text":
                    text_content += block.text

        data = None
        if self.output_model and text_content:
            data = self._extract_structured_data(text_content)

        return AgentResult(
            success=True,
            data=data,
            reasoning=text_content,
        )

    def _extract_structured_data(self, text: str) -> Optional[Dict[str, Any]]:
        """Extract JSON data from response text."""
        # Try JSON code blocks first
        json_match = re.search(r"```json\s*([\s\S]*?)\s*```", text)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass

        # Try raw JSON object
        json_match = re.search(r"\{[\s\S]*\}", text)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                pass

        return None
