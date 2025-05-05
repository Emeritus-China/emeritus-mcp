"""
Tag-related services for interacting with the Emeritus API.
"""
from typing import Dict

import httpx
from fastapi import HTTPException, status

from emeritus_mcp.auth.authentication import emeritus_auth
from emeritus_mcp.config.settings import settings
from emeritus_mcp.models.tag import (
    ActivateTagGroupRequest,
    AssignTagRequest,
    CreateTagRequest,
    DeactivateTagGroupRequest,
    ListUserTagsRequest,
    TagGroupListRequest,
    UpdateTagGroupRequest,
)


class TagService:
    """Service for tag-related operations."""

    def __init__(self):
        self._http_client = httpx.AsyncClient(timeout=30.0)
        self._base_url = settings.EMERITUS_API_HOST

    async def create_tag(self, request: CreateTagRequest) -> Dict:
        """
        Create a tag group.
        
        Args:
            request (CreateTagRequest): The request data.
            
        Returns:
            Dict: The created tag group data.
        """
        url = f"{self._base_url}/api/v5/entity/tags/group/create"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "name": request.name,
            "variable_name": request.variable_name,
            "description": request.description,
            "attribute": request.attribute,
            "category": request.category,
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to create tag group: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def get_tag_group_list(self, request: TagGroupListRequest) -> Dict:
        """
        Get a list of tag groups.
        
        Args:
            request (TagGroupListRequest): The request data.
            
        Returns:
            Dict: The tag group list data.
        """
        url = f"{self._base_url}/api/v5/entity/tags/group/list"
        headers = await emeritus_auth.get_headers()
        
        params = {
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to get tag group list: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def update_tag_group(self, request: UpdateTagGroupRequest) -> Dict:
        """
        Update a tag group.
        
        Args:
            request (UpdateTagGroupRequest): The request data.
            
        Returns:
            Dict: The updated tag group data.
        """
        url = f"{self._base_url}/api/v5/entity/tags/group/update"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "tags_group_id": request.tags_group_id,
            "corp_id": request.corp_id,
        }
        
        if request.name:
            payload["name"] = request.name
        
        if request.description:
            payload["description"] = request.description
        
        if request.category:
            payload["category"] = request.category
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to update tag group: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def deactivate_tag_group(self, request: DeactivateTagGroupRequest) -> Dict:
        """
        Deactivate a tag group.
        
        Args:
            request (DeactivateTagGroupRequest): The request data.
            
        Returns:
            Dict: The deactivated tag group data.
        """
        url = f"{self._base_url}/api/v5/entity/tags/group/deactivate"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "tags_group_id": request.tags_group_id,
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to deactivate tag group: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def activate_tag_group(self, request: ActivateTagGroupRequest) -> Dict:
        """
        Activate a tag group.
        
        Args:
            request (ActivateTagGroupRequest): The request data.
            
        Returns:
            Dict: The activated tag group data.
        """
        url = f"{self._base_url}/api/v5/entity/tags/group/activate"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "tags_group_id": request.tags_group_id,
            "corp_id": request.corp_id,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to activate tag group: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def assign_tag(self, request: AssignTagRequest) -> Dict:
        """
        Assign a tag to a user.
        
        Args:
            request (AssignTagRequest): The request data.
            
        Returns:
            Dict: The assigned tag data.
        """
        url = f"{self._base_url}/api/v5/entity/user/tags/assign"
        headers = await emeritus_auth.get_headers()
        
        payload = {
            "user_id": request.user_id,
            "tags_group_id": request.tags_group_id,
            "corp_id": request.corp_id,
            "define_value": request.define_value,
        }
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to assign tag: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def list_user_tags(self, request: ListUserTagsRequest) -> Dict:
        """
        List tags assigned to a user.
        
        Args:
            request (ListUserTagsRequest): The request data.
            
        Returns:
            Dict: The user tags data.
        """
        url = f"{self._base_url}/api/v5/entity/user/tags/list"
        headers = await emeritus_auth.get_headers()
        
        params = {
            "corp_id": request.corp_id,
            "user_id": request.user_id,
        }
        
        response = await self._http_client.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to list user tags: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]


# Create a singleton instance
tag_service = TagService()
