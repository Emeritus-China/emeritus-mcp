"""
Order-related data models.
"""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class OrderDetailRequest(BaseModel):
    """Request model for fetching order details."""
    
    corp_id: str = Field(..., description="Organization ID")
    order_id: str = Field(..., description="Unique Order ID")


class OrderDetail(BaseModel):
    """Order detail model."""
    
    entity_id: str = Field(..., description="Order ID")
    application_fee_price: Optional[int] = Field(None, description="Application fee")
    corp_id: str = Field(..., description="Organization ID")
    course_code: Optional[str] = Field(None, description="Course code")
    course_end_time: Optional[str] = Field(None, description="Course end time")
    course_id: Optional[str] = Field(None, description="Course ID")
    ctime: str = Field(..., description="Order created time")
    currency: str = Field(..., description="Payment currency")
    discounted_price: int = Field(0, description="Discounted price")
    installment_count: int = Field(1, description="Number of installments")
    is_deleted: bool = Field(False, description="Is deleted flag")
    leads_id: Optional[str] = Field(None, description="Leads ID")
    listed_price: int = Field(..., description="Listed price")
    mtime: str = Field(..., description="Order modified time")
    paid_price: int = Field(0, description="Paid fees")
    post_refund_price: int = Field(0, description="Post refund price")
    pre_sub_order_ids: List[str] = Field([], description="Pre-sub order IDs")
    source: str = Field(..., description="Source of the order")
    status: str = Field(..., description="Order status")
    sub_order_ids: List[str] = Field([], description="Sub order IDs")
    total_price: int = Field(..., description="Total price")
    type: str = Field(..., description="Order type")
    user_id: str = Field(..., description="User ID")
    version: int = Field(0, description="Version")
    coupon_ids: List[str] = Field([], description="Coupon IDs")
    unpaid_price: int = Field(..., description="Unpaid fees")
    is_locked: bool = Field(False, description="Is locked flag")
    sub_orders: List[Dict[str, Any]] = Field([], description="Sub orders")


class OrderListRequest(BaseModel):
    """Request model for fetching order list."""
    
    corp_id: str = Field(..., description="Organization ID")
    page: Optional[int] = Field(0, description="Page number, start from 0")
    page_size: Optional[int] = Field(10, description="Data size within one page, max 1000")
    start_date: Optional[str] = Field(None, description="Order created/modified time range start")
    end_date: Optional[str] = Field(None, description="Order created/modified time range end")
    status: Optional[str] = Field(None, description="Order status")
    time_range_type: Optional[str] = Field("create", description="Time range type (create/modify)")


class OrderListResponse(BaseModel):
    """Response model for order list."""
    
    total: int = Field(..., description="Total number of orders")
    rows: List[Dict[str, Any]] = Field(..., description="List of orders")


class OrderFinancialListRequest(BaseModel):
    """Request model for fetching order financial list."""
    
    corp_id: str = Field(..., description="Organization ID")
    page: Optional[int] = Field(0, description="Page number")
    page_size: Optional[int] = Field(10, description="Number of items per page")
    start_date: Optional[str] = Field(None, description="Start date filter")
    end_date: Optional[str] = Field(None, description="End date filter")
    status: Optional[str] = Field(None, description="Status filter")
    time_range_type: Optional[str] = Field("create", description="Type of time range")


class OrderFinancialListResponse(BaseModel):
    """Response model for order financial list."""
    
    total: int = Field(..., description="Total number of financial records")
    rows: List[Dict[str, Any]] = Field(..., description="List of financial records")
