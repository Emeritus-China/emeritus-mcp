"""
CLI entry point for the Emeritus MCP server.
Allows running the server with: python -m emeritus_mcp
"""

import asyncio
from .server import main

if __name__ == "__main__":
    asyncio.run(main()) 