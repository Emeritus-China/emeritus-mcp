"""
Order management tools for the Emeritus MCP server.
"""

from typing import Any, Dict, Optional
from ..services.emeritus_client import EmeritusClient


class OrderTools:
    """
    Tools for order management operations.
    """
    
    def __init__(self, emeritus_client: EmeritusClient):
        """
        Initialize order tools.
        
        Args:
            emeritus_client: The Emeritus API client
        """
        self.client = emeritus_client
    
    async def fetch_order(self, order_id: str) -> Dict[str, Any]:
        """
        Fetch details for a specific order.
        
        Args:
            order_id: Order ID to fetch
            
        Returns:
            Order details
        """
        return await self.client.fetch_order(order_id)
    
    async def list_orders(self, user_id: Optional[str] = None, status: Optional[str] = None, 
                         limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """
        List orders with optional filtering.
        
        Args:
            user_id: Filter by user ID
            status: Filter by order status
            limit: Maximum number of results
            offset: Offset for pagination
            
        Returns:
            List of orders
        """
        return await self.client.list_orders(user_id, status, limit, offset)
    
    async def list_order_financials(self, order_id: Optional[str] = None, 
                                   limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """
        List financial records for orders.
        
        Args:
            order_id: Filter by order ID
            limit: Maximum number of results
            offset: Offset for pagination
            
        Returns:
            List of order financial records
        """
        return await self.client.list_order_financials(order_id, limit, offset) 