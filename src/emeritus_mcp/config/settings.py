"""
Settings configuration for the Emeritus MCP server.
"""
import os
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    # API settings
    API_V5_PREFIX: str = "/api/v5"
    
    # Emeritus API settings
    EMERITUS_API_HOST: str = Field(..., description="Emeritus API host")
    EMERITUS_USER_ID: str = Field(..., description="Emeritus User ID")
    EMERITUS_API_SECRET: str = Field(..., description="Emeritus API Secret")
    
    # MCP settings
    MCP_API_KEY: Optional[str] = Field(None, description="MCP API Key")
    
    # Server settings
    DEBUG: bool = Field(False, description="Debug mode")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
