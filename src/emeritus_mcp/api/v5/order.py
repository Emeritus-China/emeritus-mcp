"""
Order-related API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from emeritus_mcp.auth.authentication import mcp_auth
from emeritus_mcp.models.common import MCPResponse
from emeritus_mcp.models.order import (
    OrderDetail,
    OrderDetailRequest,
    OrderFinancialListRequest,
    OrderFinancialListResponse,
    OrderListRequest,
    OrderListResponse,
)
from emeritus_mcp.services.order_service import order_service

# Create the router
router = APIRouter()


@router.get(
    "/order/fetch",
    response_model=MCPResponse[OrderDetail],
    summary="Get order details",
    description="Get details for a specific order",
)
async def get_order_detail(
    corp_id: str,
    order_id: str,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[OrderDetail]:
    """
    Get order details.
    
    Args:
        corp_id: The corporation ID.
        order_id: The order ID.
        
    Returns:
        MCPResponse[OrderDetail]: The response.
    """
    try:
        request = OrderDetailRequest(corp_id=corp_id, order_id=order_id)
        data = await order_service.get_order_detail(request)
        
        return MCPResponse.success_response(
            data=OrderDetail(**data)
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.get(
    "/order/list",
    response_model=MCPResponse[OrderListResponse],
    summary="Get order list",
    description="Get a list of orders",
)
async def get_order_list(
    corp_id: str,
    page: int = 0,
    page_size: int = 10,
    start_date: str = None,
    end_date: str = None,
    status: str = None,
    time_range_type: str = "create",
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[OrderListResponse]:
    """
    Get order list.
    
    Args:
        corp_id: The corporation ID.
        page: The page number.
        page_size: The page size.
        start_date: The start date.
        end_date: The end date.
        status: The order status.
        time_range_type: The time range type.
        
    Returns:
        MCPResponse[OrderListResponse]: The response.
    """
    try:
        request = OrderListRequest(
            corp_id=corp_id,
            page=page,
            page_size=page_size,
            start_date=start_date,
            end_date=end_date,
            status=status,
            time_range_type=time_range_type,
        )
        data = await order_service.get_order_list(request)
        
        return MCPResponse.success_response(
            data=OrderListResponse(
                total=data["total"],
                rows=data["rows"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.get(
    "/order/financial/list",
    response_model=MCPResponse[OrderFinancialListResponse],
    summary="Get order financial list",
    description="Get a list of order financial records",
)
async def get_order_financial_list(
    corp_id: str,
    page: int = 0,
    page_size: int = 10,
    start_date: str = None,
    end_date: str = None,
    status: str = None,
    time_range_type: str = "create",
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[OrderFinancialListResponse]:
    """
    Get order financial list.
    
    Args:
        corp_id: The corporation ID.
        page: The page number.
        page_size: The page size.
        start_date: The start date.
        end_date: The end date.
        status: The order status.
        time_range_type: The time range type.
        
    Returns:
        MCPResponse[OrderFinancialListResponse]: The response.
    """
    try:
        request = OrderFinancialListRequest(
            corp_id=corp_id,
            page=page,
            page_size=page_size,
            start_date=start_date,
            end_date=end_date,
            status=status,
            time_range_type=time_range_type,
        )
        data = await order_service.get_order_financial_list(request)
        
        return MCPResponse.success_response(
            data=OrderFinancialListResponse(
                total=data["total"],
                rows=data["rows"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))
