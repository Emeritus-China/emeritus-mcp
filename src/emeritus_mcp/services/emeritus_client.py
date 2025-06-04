"""
Emeritus API client for the MCP server.
"""

import hashlib
import time
from typing import Any, Dict, List, Optional
import httpx


class EmeritusClient:
    """
    Client for interacting with the Emeritus API.
    """
    
    def __init__(self, api_host: str, user_id: str, api_secret: str):
        """
        Initialize the Emeritus client.
        
        Args:
            api_host: The Emeritus API host URL
            user_id: The Emeritus user ID
            api_secret: The Emeritus API secret
        """
        self.api_host = api_host.rstrip('/')
        self.user_id = user_id
        self.api_secret = api_secret
        self.client = httpx.AsyncClient()
    
    def _generate_auth_headers(self) -> Dict[str, str]:
        """
        Generate authentication headers for Emeritus API requests.
        
        Returns:
            Dict with authentication headers
        """
        timestamp = str(int(time.time()))
        signature_string = f"{self.user_id}{timestamp}{self.api_secret}"
        signature = hashlib.sha256(signature_string.encode()).hexdigest()
        
        return {
            "X-User-ID": self.user_id,
            "X-Timestamp": timestamp,
            "X-Signature": signature,
            "Content-Type": "application/json"
        }
    
    async def make_request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make an authenticated request to the Emeritus API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Request body data
            params: URL parameters
            
        Returns:
            API response data
        """
        url = f"{self.api_host}{endpoint}"
        headers = self._generate_auth_headers()
        
        response = await self.client.request(
            method=method,
            url=url,
            headers=headers,
            json=data,
            params=params
        )
        
        response.raise_for_status()
        return response.json()
    
    # User Management Methods
    async def create_user(self, mobile: Optional[str] = None, email: Optional[str] = None, source: Optional[str] = None) -> Dict[str, Any]:
        """Create a user by mobile number or email."""
        data = {}
        if mobile:
            data["mobile"] = mobile
        if email:
            data["email"] = email
        if source:
            data["source"] = source
            
        return await self.make_request("POST", "/api/v5/entity/user/create", data=data)
    
    async def fetch_user_profile(self, user_id: str) -> Dict[str, Any]:
        """Fetch user profile information."""
        return await self.make_request("GET", "/api/v5/entity/profile/fetch", params={"user_id": user_id})
    
    async def update_user_owner(self, user_id: str, owner_id: str) -> Dict[str, Any]:
        """Update a user's owner."""
        return await self.make_request("POST", "/api/v5/entity/user/owner/update", data={"user_id": user_id, "owner_id": owner_id})
    
    async def update_user_pool(self, user_id: str, pool_id: str) -> Dict[str, Any]:
        """Update a user's pool."""
        return await self.make_request("POST", "/api/v5/entity/user/pool/update", data={"user_id": user_id, "pool_id": pool_id})
    
    async def update_user_email(self, user_id: str, email: str) -> Dict[str, Any]:
        """Update a user's email."""
        return await self.make_request("POST", "/api/v5/entity/user/email/update", data={"user_id": user_id, "email": email})
    
    async def fetch_user_contact(self, user_id: str) -> Dict[str, Any]:
        """Fetch user contact information."""
        return await self.make_request("GET", "/api/v5/entity/user/contact/fetch", params={"user_id": user_id})
    
    # Tag Management Methods
    async def create_tag_group(self, name: str, description: Optional[str] = None) -> Dict[str, Any]:
        """Create a tag group."""
        data = {"name": name}
        if description:
            data["description"] = description
        return await self.make_request("POST", "/api/v5/entity/tags/group/create", data=data)
    
    async def list_tag_groups(self, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """List tag groups."""
        params = {}
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        return await self.make_request("GET", "/api/v5/entity/tags/group/list", params=params)
    
    async def update_tag_group(self, group_id: str, name: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
        """Update a tag group."""
        data = {"group_id": group_id}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        return await self.make_request("POST", "/api/v5/entity/tags/group/update", data=data)
    
    async def deactivate_tag_group(self, group_id: str) -> Dict[str, Any]:
        """Deactivate a tag group."""
        return await self.make_request("POST", "/api/v5/entity/tags/group/deactivate", data={"group_id": group_id})
    
    async def activate_tag_group(self, group_id: str) -> Dict[str, Any]:
        """Activate a tag group."""
        return await self.make_request("POST", "/api/v5/entity/tags/group/activate", data={"group_id": group_id})
    
    async def assign_user_tag(self, user_id: str, tag_id: str) -> Dict[str, Any]:
        """Assign a tag to a user."""
        return await self.make_request("POST", "/api/v5/entity/user/tags/assign", data={"user_id": user_id, "tag_id": tag_id})
    
    async def list_user_tags(self, user_id: str) -> Dict[str, Any]:
        """List tags assigned to a user."""
        return await self.make_request("GET", "/api/v5/entity/user/tags/list", params={"user_id": user_id})
    
    # Order Management Methods
    async def fetch_order(self, order_id: str) -> Dict[str, Any]:
        """Fetch order details."""
        return await self.make_request("GET", "/api/v5/entity/order/fetch", params={"order_id": order_id})
    
    async def list_orders(self, user_id: Optional[str] = None, status: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """List orders with optional filtering."""
        params = {}
        if user_id:
            params["user_id"] = user_id
        if status:
            params["status"] = status
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        return await self.make_request("GET", "/api/v5/entity/order/list", params=params)
    
    async def list_order_financials(self, order_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """List order financial records."""
        params = {}
        if order_id:
            params["order_id"] = order_id
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        return await self.make_request("GET", "/api/v5/entity/order/financial/list", params=params)
    
    # Leads Management Methods
    async def import_leads(self, leads_data: List[Dict[str, Any]], source: Optional[str] = None) -> Dict[str, Any]:
        """Import leads from raw data."""
        data = {"leads_data": leads_data}
        if source:
            data["source"] = source
        return await self.make_request("POST", "/api/v5/entity/leads/import", data=data)
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose() 