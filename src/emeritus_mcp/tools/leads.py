"""
Leads management tools for the Emeritus MCP server.
"""

from typing import Any, Dict, List, Optional
from ..services.emeritus_client import EmeritusClient


class LeadsTools:
    """
    Tools for leads management operations.
    """
    
    def __init__(self, emeritus_client: EmeritusClient):
        """
        Initialize leads tools.
        
        Args:
            emeritus_client: The Emeritus API client
        """
        self.client = emeritus_client
    
    async def import_leads(self, leads_data: List[Dict[str, Any]], source: Optional[str] = None) -> Dict[str, Any]:
        """
        Import leads from raw data.
        
        Args:
            leads_data: Array of lead objects to import
            source: Source of the leads
            
        Returns:
            Import result
        """
        return await self.client.import_leads(leads_data, source) 