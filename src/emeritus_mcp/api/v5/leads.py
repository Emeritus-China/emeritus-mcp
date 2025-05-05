"""
Leads-related API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from emeritus_mcp.auth.authentication import mcp_auth
from emeritus_mcp.models.common import MCPResponse
from emeritus_mcp.models.leads import ImportLeadsRequest, ImportLeadsResponse
from emeritus_mcp.services.leads_service import leads_service

# Create the router
router = APIRouter()


@router.post(
    "/leads/import",
    response_model=MCPResponse[ImportLeadsResponse],
    summary="Import leads",
    description="Import leads from raw data",
)
async def import_leads(
    request: ImportLeadsRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[ImportLeadsResponse]:
    """
    Import leads.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[ImportLeadsResponse]: The response.
    """
    try:
        data = await leads_service.import_leads(request)
        
        return MCPResponse.success_response(
            data=ImportLeadsResponse(
                lead_id=data["lead_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))
