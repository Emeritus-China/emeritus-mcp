"""
Main API router for the Emeritus MCP server.
"""
from fastapi import APIRouter

from emeritus_mcp.api.v5 import leads_router, order_router, tag_router, user_router
from emeritus_mcp.config.settings import settings

# Create the main API router
api_router = APIRouter()

# Include the v5 API routers
api_router.include_router(
    user_router, prefix=f"{settings.API_V5_PREFIX}/entity", tags=["User"]
)
api_router.include_router(
    tag_router, prefix=f"{settings.API_V5_PREFIX}/entity", tags=["Tag"]
)
api_router.include_router(
    order_router, prefix=f"{settings.API_V5_PREFIX}/entity", tags=["Order"]
)
api_router.include_router(
    leads_router, prefix=f"{settings.API_V5_PREFIX}/entity", tags=["Leads"]
)
