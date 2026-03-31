"""Configuration management for the Deal Pricing system."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Authentication
    anthropic_api_key: Optional[str] = None
    claude_code_oauth_token: Optional[str] = None

    # Client mode: "auto", "sdk", or "api"
    client_mode: str = "auto"

    # Model
    claude_model: str = "sonnet"

    # Paths
    project_root: Path = Path(__file__).parent.parent.parent
    output_dir: Path = Path("./output")
    deals_dir: Path = Path("./deals")
    knowledge_base_dir: Path = Path("./knowledge_base")
    templates_dir: Path = Path("./templates")

    # Debug
    debug: bool = False

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    def get_effective_client_mode(self) -> str:
        """Determine whether to use SDK or API based on available credentials."""
        if self.client_mode == "sdk":
            return "sdk"
        elif self.client_mode == "api":
            return "api"
        else:  # auto
            if self.claude_code_oauth_token:
                return "sdk"
            elif self.anthropic_api_key:
                return "api"
            return "sdk"  # default to SDK


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
