"""
Configuration settings for the Emeritus MCP server.
"""

import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the Emeritus MCP server.
    """
    
    # Emeritus API Configuration
    emeritus_api_host: str
    emeritus_user_id: str
    emeritus_api_secret: str
    
    # Debug settings
    debug: bool = False
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
_settings: Optional[Settings] = None


def get_settings() -> Settings:
    """
    Get the global settings instance.
    
    Returns:
        Settings: The settings instance.
    """
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
