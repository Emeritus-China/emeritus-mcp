"""
Emeritus Model Context Protocol Server

This module implements an MCP server that provides tools for interacting with the Emeritus API.
It exposes user management, tag operations, order management, and leads import functionality
through the standardized MCP protocol.
"""

import asyncio
import logging
import json
from typing import Any, Dict, List, Optional

from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequest,
    ListToolsRequest,
    Tool,
    TextContent,
    ToolResult,
    ErrorCode,
    McpError
)

from .config.settings import get_settings
from .services.emeritus_client import EmeritusClient
from .tools.user import UserTools
from .tools.tag import TagTools
from .tools.order import OrderTools
from .tools.leads import LeadsTools

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmeritusMCPServer:
    """
    Emeritus MCP Server implementation.
    
    This server provides tools for interacting with the Emeritus API through
    the Model Context Protocol standard.
    """
    
    def __init__(self):
        self.settings = get_settings()
        self.emeritus_client = EmeritusClient(
            api_host=self.settings.emeritus_api_host,
            user_id=self.settings.emeritus_user_id,
            api_secret=self.settings.emeritus_api_secret
        )
        
        # Initialize tool handlers
        self.user_tools = UserTools(self.emeritus_client)
        self.tag_tools = TagTools(self.emeritus_client)
        self.order_tools = OrderTools(self.emeritus_client)
        self.leads_tools = LeadsTools(self.emeritus_client)
        
        # Create MCP server
        self.server = Server("emeritus-mcp")
        self._register_handlers()
    
    def _register_handlers(self) -> None:
        """Register MCP handlers for tools and resources."""
        
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List all available tools."""
            return [
                # User management tools
                Tool(
                    name="create_user",
                    description="Create a new user by mobile number or email",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "mobile": {"type": "string", "description": "User's mobile number"},
                            "email": {"type": "string", "description": "User's email address"},
                            "source": {"type": "string", "description": "Source of the user creation"}
                        },
                        "anyOf": [
                            {"required": ["mobile"]},
                            {"required": ["email"]}
                        ]
                    }
                ),
                Tool(
                    name="fetch_user_profile",
                    description="Fetch user profile information",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "User ID to fetch"}
                        },
                        "required": ["user_id"]
                    }
                ),
                Tool(
                    name="update_user_owner",
                    description="Update the owner of a user",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "User ID to update"},
                            "owner_id": {"type": "string", "description": "New owner ID"}
                        },
                        "required": ["user_id", "owner_id"]
                    }
                ),
                Tool(
                    name="update_user_pool",
                    description="Update the pool assignment of a user",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "User ID to update"},
                            "pool_id": {"type": "string", "description": "New pool ID"}
                        },
                        "required": ["user_id", "pool_id"]
                    }
                ),
                Tool(
                    name="update_user_email",
                    description="Update a user's email address",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "User ID to update"},
                            "email": {"type": "string", "description": "New email address"}
                        },
                        "required": ["user_id", "email"]
                    }
                ),
                Tool(
                    name="fetch_user_contact",
                    description="Fetch user contact information",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "User ID to fetch contact for"}
                        },
                        "required": ["user_id"]
                    }
                ),
                
                # Tag management tools
                Tool(
                    name="create_tag_group",
                    description="Create a new tag group",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "Tag group name"},
                            "description": {"type": "string", "description": "Tag group description"}
                        },
                        "required": ["name"]
                    }
                ),
                Tool(
                    name="list_tag_groups",
                    description="List all tag groups",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "limit": {"type": "integer", "description": "Maximum number of results"},
                            "offset": {"type": "integer", "description": "Offset for pagination"}
                        }
                    }
                ),
                Tool(
                    name="update_tag_group",
                    description="Update an existing tag group",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "group_id": {"type": "string", "description": "Tag group ID"},
                            "name": {"type": "string", "description": "New name"},
                            "description": {"type": "string", "description": "New description"}
                        },
                        "required": ["group_id"]
                    }
                ),
                Tool(
                    name="deactivate_tag_group",
                    description="Deactivate a tag group",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "group_id": {"type": "string", "description": "Tag group ID to deactivate"}
                        },
                        "required": ["group_id"]
                    }
                ),
                Tool(
                    name="activate_tag_group",
                    description="Activate a tag group",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "group_id": {"type": "string", "description": "Tag group ID to activate"}
                        },
                        "required": ["group_id"]
                    }
                ),
                Tool(
                    name="assign_user_tag",
                    description="Assign a tag to a user",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "User ID"},
                            "tag_id": {"type": "string", "description": "Tag ID to assign"}
                        },
                        "required": ["user_id", "tag_id"]
                    }
                ),
                Tool(
                    name="list_user_tags",
                    description="List tags assigned to a user",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "User ID to list tags for"}
                        },
                        "required": ["user_id"]
                    }
                ),
                
                # Order management tools
                Tool(
                    name="fetch_order",
                    description="Fetch details for a specific order",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "order_id": {"type": "string", "description": "Order ID to fetch"}
                        },
                        "required": ["order_id"]
                    }
                ),
                Tool(
                    name="list_orders",
                    description="List orders with optional filtering",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "Filter by user ID"},
                            "status": {"type": "string", "description": "Filter by order status"},
                            "limit": {"type": "integer", "description": "Maximum number of results"},
                            "offset": {"type": "integer", "description": "Offset for pagination"}
                        }
                    }
                ),
                Tool(
                    name="list_order_financials",
                    description="List financial records for orders",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "order_id": {"type": "string", "description": "Filter by order ID"},
                            "limit": {"type": "integer", "description": "Maximum number of results"},
                            "offset": {"type": "integer", "description": "Offset for pagination"}
                        }
                    }
                ),
                
                # Leads management tools
                Tool(
                    name="import_leads",
                    description="Import leads from raw data",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "leads_data": {
                                "type": "array",
                                "description": "Array of lead objects to import",
                                "items": {"type": "object"}
                            },
                            "source": {"type": "string", "description": "Source of the leads"}
                        },
                        "required": ["leads_data"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def handle_call_tool(request: CallToolRequest) -> ToolResult:
            """Handle tool calls from the MCP client."""
            try:
                tool_name = request.params.name
                arguments = request.params.arguments or {}
                
                logger.info(f"Calling tool: {tool_name} with arguments: {arguments}")
                
                # Route to appropriate tool handler
                if tool_name.startswith("create_user") or tool_name.startswith("fetch_user") or tool_name.startswith("update_user"):
                    result = await self._handle_user_tool(tool_name, arguments)
                elif tool_name.endswith("_tag_group") or tool_name.endswith("_user_tag") or tool_name == "list_user_tags":
                    result = await self._handle_tag_tool(tool_name, arguments)
                elif tool_name.startswith("fetch_order") or tool_name.startswith("list_order"):
                    result = await self._handle_order_tool(tool_name, arguments)
                elif tool_name == "import_leads":
                    result = await self._handle_leads_tool(tool_name, arguments)
                else:
                    raise McpError(ErrorCode.METHOD_NOT_FOUND, f"Unknown tool: {tool_name}")
                
                return ToolResult(
                    content=[TextContent(type="text", text=json.dumps(result, indent=2))]
                )
                
            except Exception as e:
                logger.error(f"Error calling tool {request.params.name}: {str(e)}")
                raise McpError(ErrorCode.INTERNAL_ERROR, f"Tool execution failed: {str(e)}")
    
    async def _handle_user_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Handle user management tool calls."""
        if tool_name == "create_user":
            return await self.user_tools.create_user(**arguments)
        elif tool_name == "fetch_user_profile":
            return await self.user_tools.fetch_user_profile(**arguments)
        elif tool_name == "update_user_owner":
            return await self.user_tools.update_user_owner(**arguments)
        elif tool_name == "update_user_pool":
            return await self.user_tools.update_user_pool(**arguments)
        elif tool_name == "update_user_email":
            return await self.user_tools.update_user_email(**arguments)
        elif tool_name == "fetch_user_contact":
            return await self.user_tools.fetch_user_contact(**arguments)
        else:
            raise McpError(ErrorCode.METHOD_NOT_FOUND, f"Unknown user tool: {tool_name}")
    
    async def _handle_tag_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Handle tag management tool calls."""
        if tool_name == "create_tag_group":
            return await self.tag_tools.create_tag_group(**arguments)
        elif tool_name == "list_tag_groups":
            return await self.tag_tools.list_tag_groups(**arguments)
        elif tool_name == "update_tag_group":
            return await self.tag_tools.update_tag_group(**arguments)
        elif tool_name == "deactivate_tag_group":
            return await self.tag_tools.deactivate_tag_group(**arguments)
        elif tool_name == "activate_tag_group":
            return await self.tag_tools.activate_tag_group(**arguments)
        elif tool_name == "assign_user_tag":
            return await self.tag_tools.assign_user_tag(**arguments)
        elif tool_name == "list_user_tags":
            return await self.tag_tools.list_user_tags(**arguments)
        else:
            raise McpError(ErrorCode.METHOD_NOT_FOUND, f"Unknown tag tool: {tool_name}")
    
    async def _handle_order_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Handle order management tool calls."""
        if tool_name == "fetch_order":
            return await self.order_tools.fetch_order(**arguments)
        elif tool_name == "list_orders":
            return await self.order_tools.list_orders(**arguments)
        elif tool_name == "list_order_financials":
            return await self.order_tools.list_order_financials(**arguments)
        else:
            raise McpError(ErrorCode.METHOD_NOT_FOUND, f"Unknown order tool: {tool_name}")
    
    async def _handle_leads_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Handle leads management tool calls."""
        if tool_name == "import_leads":
            return await self.leads_tools.import_leads(**arguments)
        else:
            raise McpError(ErrorCode.METHOD_NOT_FOUND, f"Unknown leads tool: {tool_name}")
    
    async def run(self) -> None:
        """Run the MCP server."""
        logger.info("Starting Emeritus MCP Server...")
        
        # Run the server with stdio transport
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="emeritus-mcp",
                    server_version="0.1.0",
                    capabilities=self.server.get_capabilities()
                )
            )


async def main() -> None:
    """Main entry point for the MCP server."""
    server = EmeritusMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main()) 