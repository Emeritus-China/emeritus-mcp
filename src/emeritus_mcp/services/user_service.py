"""
User-related services for interacting with the Emeritus API.
"""
from typing import Dict, Optional, Union

import httpx
from fastapi import HTTPException, status

from emeritus_mcp.auth.authentication import emeritus_auth
from emeritus_mcp.config.settings import settings
from emeritus_mcp.models.user import (
    CreateUserByEmailRequest,
    CreateUserByMobileRequest,
    FetchUserContactRequest,
    UpdateUserEmailRequest,
    UpdateUserOwnerRequest,
    UpdateUserPoolRequest,
    UserProfileRequest,
)


class UserService:
    """Service for user-related operations."""

    def __init__(self):
        self._http_client = httpx.AsyncClient(timeout=30.0)
        self._base_url = settings.EMERITUS_API_HOST

    async def create_user_by_mobile(self, request: CreateUserByMobileRequest) -> Dict:
        """
        Create a user by mobile number.
        
        Args:
            request (CreateUserByMobileRequest): The request data.
            
        Returns:
            Dict: The created user data.
        """
        url = f"{self._base_url}/api/v5/entity/user/create"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "area_code": request.area_code,
            "mobile": request.mobile,
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to create user: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def create_user_by_email(self, request: CreateUserByEmailRequest) -> Dict:
        """
        Create a user by email.
        
        Args:
            request (CreateUserByEmailRequest): The request data.
            
        Returns:
            Dict: The created user data.
        """
        url = f"{self._base_url}/api/v5/entity/user/create"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "email": request.email,
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to create user: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def get_user_profile(self, request: UserProfileRequest) -> Dict:
        """
        Get a user's profile.
        
        Args:
            request (UserProfileRequest): The request data.
            
        Returns:
            Dict: The user profile data.
        """
        url = f"{self._base_url}/api/v5/entity/profile/fetch"
        headers = await emeritus_auth.get_headers()
        
        params = {
            "corp_id": request.corp_id,
            "user_id": request.user_id,
        }
        
        response = await self._http_client.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to get user profile: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def update_user_owner(self, request: UpdateUserOwnerRequest) -> Dict:
        """
        Update a user's owner.
        
        Args:
            request (UpdateUserOwnerRequest): The request data.
            
        Returns:
            Dict: The updated user data.
        """
        url = f"{self._base_url}/api/v5/entity/user/owner/update"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "user_id": request.user_id,
            "owner_id": request.owner_id,
            "event_type": request.event_type,
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to update user owner: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def update_user_pool(self, request: UpdateUserPoolRequest) -> Dict:
        """
        Update a user's pool.
        
        Args:
            request (UpdateUserPoolRequest): The request data.
            
        Returns:
            Dict: The updated user data.
        """
        url = f"{self._base_url}/api/v5/entity/user/pool/update"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "user_id": request.user_id,
            "corp_id": request.corp_id,
            "pool": request.pool,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to update user pool: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def update_user_email(self, request: UpdateUserEmailRequest) -> Dict:
        """
        Update a user's email.
        
        Args:
            request (UpdateUserEmailRequest): The request data.
            
        Returns:
            Dict: The updated user data.
        """
        url = f"{self._base_url}/api/v5/entity/user/email/update"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "user_id": request.user_id,
            "email": request.email,
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to update user email: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def fetch_user_contact(self, request: FetchUserContactRequest) -> Dict:
        """
        Fetch a user's contact information.
        
        Args:
            request (FetchUserContactRequest): The request data.
            
        Returns:
            Dict: The user contact data.
        """
        url = f"{self._base_url}/api/v5/entity/user/contact/fetch"
        headers = await emeritus_auth.get_headers()
        
        params = {
            "user_id": request.user_id,
            "corp_id": request.corp_id,
            "contact_type": request.contact_type,
        }
        
        response = await self._http_client.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to fetch user contact: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]


# Create a singleton instance
user_service = UserService()
