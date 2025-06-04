"""
User management tools for the Emeritus MCP server.
"""

from typing import Any, Dict, Optional
from ..services.emeritus_client import EmeritusClient


class UserTools:
    """
    Tools for user management operations.
    """
    
    def __init__(self, emeritus_client: EmeritusClient):
        """
        Initialize user tools.
        
        Args:
            emeritus_client: The Emeritus API client
        """
        self.client = emeritus_client
    
    async def create_user(self, mobile: Optional[str] = None, email: Optional[str] = None, source: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new user by mobile number or email.
        
        Args:
            mobile: User's mobile number
            email: User's email address
            source: Source of the user creation
            
        Returns:
            API response with user creation result
        """
        if not mobile and not email:
            raise ValueError("Either mobile or email must be provided")
        
        return await self.client.create_user(mobile=mobile, email=email, source=source)
    
    async def fetch_user_profile(self, user_id: str) -> Dict[str, Any]:
        """
        Fetch user profile information.
        
        Args:
            user_id: User ID to fetch
            
        Returns:
            User profile data
        """
        return await self.client.fetch_user_profile(user_id)
    
    async def update_user_owner(self, user_id: str, owner_id: str) -> Dict[str, Any]:
        """
        Update the owner of a user.
        
        Args:
            user_id: User ID to update
            owner_id: New owner ID
            
        Returns:
            Update result
        """
        return await self.client.update_user_owner(user_id, owner_id)
    
    async def update_user_pool(self, user_id: str, pool_id: str) -> Dict[str, Any]:
        """
        Update the pool assignment of a user.
        
        Args:
            user_id: User ID to update
            pool_id: New pool ID
            
        Returns:
            Update result
        """
        return await self.client.update_user_pool(user_id, pool_id)
    
    async def update_user_email(self, user_id: str, email: str) -> Dict[str, Any]:
        """
        Update a user's email address.
        
        Args:
            user_id: User ID to update
            email: New email address
            
        Returns:
            Update result
        """
        return await self.client.update_user_email(user_id, email)
    
    async def fetch_user_contact(self, user_id: str) -> Dict[str, Any]:
        """
        Fetch user contact information.
        
        Args:
            user_id: User ID to fetch contact for
            
        Returns:
            User contact information
        """
        return await self.client.fetch_user_contact(user_id) 