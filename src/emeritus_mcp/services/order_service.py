"""
Order-related services for interacting with the Emeritus API.
"""
from typing import Dict

import httpx
from fastapi import HTTPException, status

from emeritus_mcp.auth.authentication import emeritus_auth
from emeritus_mcp.config.settings import settings
from emeritus_mcp.models.order import (
    OrderDetailRequest,
    OrderFinancialListRequest,
    OrderListRequest,
)


class OrderService:
    """Service for order-related operations."""

    def __init__(self):
        self._http_client = httpx.AsyncClient(timeout=30.0)
        self._base_url = settings.EMERITUS_API_HOST

    async def get_order_detail(self, request: OrderDetailRequest) -> Dict:
        """
        Get order details.
        
        Args:
            request (OrderDetailRequest): The request data.
            
        Returns:
            Dict: The order details.
        """
        url = f"{self._base_url}/api/v5/entity/order/fetch"
        headers = await emeritus_auth.get_headers()
        
        params = {
            "corp_id": request.corp_id,
            "order_id": request.order_id,
        }
        
        response = await self._http_client.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to get order details: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def get_order_list(self, request: OrderListRequest) -> Dict:
        """
        Get order list.
        
        Args:
            request (OrderListRequest): The request data.
            
        Returns:
            Dict: The order list data.
        """
        url = f"{self._base_url}/api/v5/entity/order/list"
        headers = await emeritus_auth.get_headers()
        
        params = {
            "corp_id": request.corp_id,
            "page": request.page,
            "page_size": request.page_size,
        }
        
        if request.start_date:
            params["start_date"] = request.start_date
        
        if request.end_date:
            params["end_date"] = request.end_date
        
        if request.status:
            params["status"] = request.status
        
        if request.time_range_type:
            params["time_range_type"] = request.time_range_type
        
        response = await self._http_client.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to get order list: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]

    async def get_order_financial_list(self, request: OrderFinancialListRequest) -> Dict:
        """
        Get order financial list.
        
        Args:
            request (OrderFinancialListRequest): The request data.
            
        Returns:
            Dict: The order financial list data.
        """
        url = f"{self._base_url}/api/v5/entity/order/financial/list"
        headers = await emeritus_auth.get_headers()
        
        params = {
            "corp_id": request.corp_id,
            "page": request.page,
            "page_size": request.page_size,
        }
        
        if request.start_date:
            params["start_date"] = request.start_date
        
        if request.end_date:
            params["end_date"] = request.end_date
        
        if request.status:
            params["status"] = request.status
        
        if request.time_range_type:
            params["time_range_type"] = request.time_range_type
        
        response = await self._http_client.get(url=url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to get order financial list: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]


# Create a singleton instance
order_service = OrderService()
