"""
V5 API module for the Emeritus MCP server.
"""
from emeritus_mcp.api.v5.leads import router as leads_router
from emeritus_mcp.api.v5.order import router as order_router
from emeritus_mcp.api.v5.tag import router as tag_router
from emeritus_mcp.api.v5.user import router as user_router

__all__ = ["user_router", "tag_router", "order_router", "leads_router"]
