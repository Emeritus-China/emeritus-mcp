"""
Tag management tools for the Emeritus MCP server.
"""

from typing import Any, Dict, Optional
from ..services.emeritus_client import EmeritusClient


class TagTools:
    """
    Tools for tag management operations.
    """
    
    def __init__(self, emeritus_client: EmeritusClient):
        """
        Initialize tag tools.
        
        Args:
            emeritus_client: The Emeritus API client
        """
        self.client = emeritus_client
    
    async def create_tag_group(self, name: str, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new tag group.
        
        Args:
            name: Tag group name
            description: Tag group description
            
        Returns:
            Tag group creation result
        """
        return await self.client.create_tag_group(name, description)
    
    async def list_tag_groups(self, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """
        List all tag groups.
        
        Args:
            limit: Maximum number of results
            offset: Offset for pagination
            
        Returns:
            List of tag groups
        """
        return await self.client.list_tag_groups(limit, offset)
    
    async def update_tag_group(self, group_id: str, name: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Update an existing tag group.
        
        Args:
            group_id: Tag group ID
            name: New name
            description: New description
            
        Returns:
            Update result
        """
        return await self.client.update_tag_group(group_id, name, description)
    
    async def deactivate_tag_group(self, group_id: str) -> Dict[str, Any]:
        """
        Deactivate a tag group.
        
        Args:
            group_id: Tag group ID to deactivate
            
        Returns:
            Deactivation result
        """
        return await self.client.deactivate_tag_group(group_id)
    
    async def activate_tag_group(self, group_id: str) -> Dict[str, Any]:
        """
        Activate a tag group.
        
        Args:
            group_id: Tag group ID to activate
            
        Returns:
            Activation result
        """
        return await self.client.activate_tag_group(group_id)
    
    async def assign_user_tag(self, user_id: str, tag_id: str) -> Dict[str, Any]:
        """
        Assign a tag to a user.
        
        Args:
            user_id: User ID
            tag_id: Tag ID to assign
            
        Returns:
            Assignment result
        """
        return await self.client.assign_user_tag(user_id, tag_id)
    
    async def list_user_tags(self, user_id: str) -> Dict[str, Any]:
        """
        List tags assigned to a user.
        
        Args:
            user_id: User ID to list tags for
            
        Returns:
            List of user tags
        """
        return await self.client.list_user_tags(user_id) 