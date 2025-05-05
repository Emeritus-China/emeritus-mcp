"""
Leads-related services for interacting with the Emeritus API.
"""
from typing import Dict

import httpx
from fastapi import HTTPException, status

from emeritus_mcp.auth.authentication import emeritus_auth
from emeritus_mcp.config.settings import settings
from emeritus_mcp.models.leads import ImportLeadsRequest


class LeadsService:
    """Service for leads-related operations."""

    def __init__(self):
        self._http_client = httpx.AsyncClient(timeout=30.0)
        self._base_url = settings.EMERITUS_API_HOST

    async def import_leads(self, request: ImportLeadsRequest) -> Dict:
        """
        Import leads.
        
        Args:
            request (ImportLeadsRequest): The request data.
            
        Returns:
            Dict: The imported lead data.
        """
        url = f"{self._base_url}/api/v5/entity/leads/import"
        headers = await emeritus_auth.get_headers()
        
        # Convert the request model to a dictionary and remove None values
        payload = {k: v for k, v in request.model_dump().items() if v is not None}
        
        response = await self._http_client.post(url=url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to import leads: {response.text}",
            )
        
        data = response.json()
        if data["code"] != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Emeritus API error: {data['msg']}",
            )
        
        return data["data"]


# Create a singleton instance
leads_service = LeadsService()
