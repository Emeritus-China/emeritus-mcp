"""
Authentication utilities for the Emeritus API.
"""
import hashlib
import time
from typing import Dict, Optional

import httpx
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from emeritus_mcp.config.settings import settings


class EmeritusAuth:
    """Authentication utilities for the Emeritus API."""

    def __init__(self):
        self._token: Optional[str] = None
        self._token_expire_time: Optional[str] = None
        self._http_client = httpx.AsyncClient(timeout=30.0)

    async def get_token(self) -> str:
        """
        Get an authentication token from the Emeritus API.
        
        Returns:
            str: The authentication token.
        """
        # Check if we already have a valid token
        if self._token and self._token_expire_time:
            # TODO: Add proper expiration time check
            # For now, we'll just return the existing token
            return self._token
        
        # Generate a new token
        time_stamp = int(time.time())
        app_id = settings.EMERITUS_USER_ID
        app_secret = settings.EMERITUS_API_SECRET
        
        # Create signature
        signed_str = f"{app_id}{time_stamp}{app_secret}"
        hl = hashlib.sha256()
        hl.update(signed_str.encode())
        signature = hl.hexdigest()
        
        # Prepare request parameters
        params = {
            "app_id": app_id,
            "time_stamp": time_stamp,
            "signature": signature
        }
        
        # Make request to get token
        url = f"{settings.EMERITUS_API_HOST}/api/v5/authentication/token"
        response = await self._http_client.post(url=url, json=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to authenticate with Emeritus API",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        # Store token and expiration time
        self._token = data["data"]["token"]
        self._token_expire_time = data["data"]["expire_time"]
        
        return self._token

    async def verify_token(self, token: str) -> Dict:
        """
        Verify a token with the Emeritus API.
        
        Args:
            token (str): The token to verify.
            
        Returns:
            Dict: The verification response.
        """
        url = f"{settings.EMERITUS_API_HOST}/api/v5/authentication/verify"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
            "X-APP-ID": settings.EMERITUS_USER_ID,
        }
        
        response = await self._http_client.get(url=url, headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to verify token with Emeritus API",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def get_headers(self) -> Dict[str, str]:
        """
        Get the headers needed for authenticated Emeritus API requests.
        
        Returns:
            Dict[str, str]: The headers.
        """
        token = await self.get_token()
        return {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
            "X-APP-ID": settings.EMERITUS_USER_ID,
        }


# Create a singleton instance
emeritus_auth = EmeritusAuth()


class MCPAuthBearer(HTTPBearer):
    """Authentication dependency for MCP API endpoints."""
    
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        """
        Validate the MCP API key.
        
        Args:
            request (Request): The incoming request.
            
        Returns:
            HTTPAuthorizationCredentials: The credentials.
        """
        credentials = await super().__call__(request)
        
        if credentials.scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme",
            )
        
        if credentials.credentials != settings.MCP_API_KEY:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid API key",
            )
        
        return credentials


# Create a dependency for MCP authentication
mcp_auth = MCPAuthBearer()
