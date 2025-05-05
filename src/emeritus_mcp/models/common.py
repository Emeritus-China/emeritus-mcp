"""
Common data models for the Emeritus MCP server.
"""
from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel, Field

# Define a generic type for the data field
T = TypeVar("T")


class EmeritusResponse(BaseModel):
    """Base response model for Emeritus API responses."""
    
    code: int = Field(..., description="Response code (0 for success)")
    msg: str = Field(..., description="Response message")
    data: Optional[Dict[str, Any]] = Field(None, description="Response data")


class MCPResponse(BaseModel, Generic[T]):
    """Base response model for MCP API responses."""
    
    success: bool = Field(..., description="Success flag")
    message: str = Field(..., description="Response message")
    data: Optional[T] = Field(None, description="Response data")
    
    @classmethod
    def success_response(cls, data: Optional[T] = None, message: str = "Success"):
        """Create a success response."""
        return cls(success=True, message=message, data=data)
    
    @classmethod
    def error_response(cls, message: str = "Error"):
        """Create an error response."""
        return cls(success=False, message=message, data=None)


class ErrorDetail(BaseModel):
    """Error detail model."""
    
    detail: str = Field(..., description="Error detail")
