"""
Main application module for the Emeritus MCP server.
"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from emeritus_mcp import __version__
from emeritus_mcp.api.router import api_router
from emeritus_mcp.config.settings import settings

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan events for the FastAPI application.
    
    Args:
        app: The FastAPI application.
    """
    # Startup events
    logger.info("Starting Emeritus MCP server...")
    
    yield
    
    # Shutdown events
    logger.info("Shutting down Emeritus MCP server...")


# Create the FastAPI application
app = FastAPI(
    title="Emeritus MCP Server",
    description="MCP server implementation for Emeritus API",
    version=__version__,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(api_router)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint.
    
    Returns:
        dict: Basic information about the API.
    """
    return {
        "name": "Emeritus MCP Server",
        "version": __version__,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint.
    
    Returns:
        dict: Health status.
    """
    return {"status": "healthy"}
