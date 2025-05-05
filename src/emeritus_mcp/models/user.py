"""
User-related data models.
"""
from typing import List, Optional, Union

from pydantic import BaseModel, Field


class CreateUserByMobileRequest(BaseModel):
    """Request model for creating a user by mobile number."""
    
    area_code: str = Field(..., description="Area code without '+' from ITU E.164")
    mobile: str = Field(..., description="Mobile phone number")
    corp_id: str = Field(..., description="Corporation ID")


class CreateUserByEmailRequest(BaseModel):
    """Request model for creating a user by email."""
    
    email: str = Field(..., description="User email")
    corp_id: str = Field(..., description="Corporation ID")


class UserCreationResponse(BaseModel):
    """Response model for user creation."""
    
    user_id: str = Field(..., description="The user's global User ID")
    is_user_exists: bool = Field(..., description="Flag if the user has been registered before creation")


class UserProfileRequest(BaseModel):
    """Request model for fetching a user profile."""
    
    corp_id: str = Field(..., description="Organization ID")
    user_id: str = Field(..., description="User ID")


class UserProfile(BaseModel):
    """User profile model."""
    
    user_id: str = Field(..., description="User ID")
    corp_id: str = Field(..., description="Corporation ID")
    name: str = Field(..., description="User name")
    last_name: Optional[str] = Field(None, description="User last name")
    first_name: Optional[str] = Field(None, description="User first name")
    area_code: Optional[str] = Field(None, description="Area code")
    mobile: Optional[str] = Field(None, description="Mobile number")
    gender: Optional[str] = Field(None, description="Gender")
    age: Optional[int] = Field(None, description="Age")
    city: Optional[str] = Field(None, description="City")
    city_raw: Optional[str] = Field(None, description="Raw city data")
    city_mobile: Optional[str] = Field(None, description="Mobile city")
    company_name: Optional[str] = Field(None, description="Company name")
    job_title: Optional[str] = Field(None, description="Job title")
    department: Optional[str] = Field(None, description="Department")
    industry: Optional[str] = Field(None, description="Industry")
    linkedin_url: Optional[str] = Field(None, description="LinkedIn URL")


class UpdateUserOwnerRequest(BaseModel):
    """Request model for updating a user's owner."""
    
    user_id: str = Field(..., description="User ID")
    owner_id: str = Field(..., description="Owner ID")
    event_type: str = Field(..., description="Event type (add or remove)")
    corp_id: str = Field(..., description="Corporation ID")


class UpdateUserOwnerResponse(BaseModel):
    """Response model for updating a user's owner."""
    
    user_id: str = Field(..., description="User ID")
    owner_id: List[str] = Field(..., description="List of owner IDs")


class UpdateUserPoolRequest(BaseModel):
    """Request model for updating a user's pool."""
    
    user_id: str = Field(..., description="User ID")
    corp_id: str = Field(..., description="Corporation ID")
    pool: str = Field(..., description="Pool (e.g., alive, dead, public)")


class UpdateUserPoolResponse(BaseModel):
    """Response model for updating a user's pool."""
    
    user_id: str = Field(..., description="User ID")


class UpdateUserEmailRequest(BaseModel):
    """Request model for updating a user's email."""
    
    user_id: str = Field(..., description="User ID")
    email: str = Field(..., description="Email")
    corp_id: str = Field(..., description="Corporation ID")


class UpdateUserEmailResponse(BaseModel):
    """Response model for updating a user's email."""
    
    user_id: str = Field(..., description="User ID")


class FetchUserContactRequest(BaseModel):
    """Request model for fetching a user's contact information."""
    
    user_id: str = Field(..., description="User ID")
    corp_id: str = Field(..., description="Corporation ID")
    contact_type: str = Field(..., description="Contact type (email or mobile)")


class FetchUserContactResponse(BaseModel):
    """Response model for fetching a user's contact information."""
    
    user_id: str = Field(..., description="User ID")
    corp_id: str = Field(..., description="Corporation ID")
    contact_type: str = Field(..., description="Contact type")
    value: Union[List[str], str] = Field(..., description="Contact value")
