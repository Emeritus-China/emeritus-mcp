"""
User-related API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials

from emeritus_mcp.auth.authentication import mcp_auth
from emeritus_mcp.models.common import MCPResponse
from emeritus_mcp.models.user import (
    CreateUserByEmailRequest,
    CreateUserByMobileRequest,
    FetchUserContactRequest,
    FetchUserContactResponse,
    UpdateUserEmailRequest,
    UpdateUserEmailResponse,
    UpdateUserOwnerRequest,
    UpdateUserOwnerResponse,
    UpdateUserPoolRequest,
    UpdateUserPoolResponse,
    UserCreationResponse,
    UserProfile,
    UserProfileRequest,
)
from emeritus_mcp.services.user_service import user_service

# Create the router
router = APIRouter()


@router.post(
    "/user/create",
    response_model=MCPResponse[UserCreationResponse],
    summary="Create a user",
    description="Create a user by mobile number or email",
)
async def create_user(
    request: CreateUserByMobileRequest | CreateUserByEmailRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[UserCreationResponse]:
    """
    Create a user by mobile number or email.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[UserCreationResponse]: The response.
    """
    try:
        if hasattr(request, "mobile"):
            data = await user_service.create_user_by_mobile(request)  # type: ignore
        else:
            data = await user_service.create_user_by_email(request)  # type: ignore
        
        return MCPResponse.success_response(
            data=UserCreationResponse(
                user_id=data["user_id"],
                is_user_exists=data["is_user_exists"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.get(
    "/profile/fetch",
    response_model=MCPResponse[UserProfile],
    summary="Get user profile",
    description="Get a user's profile information",
)
async def get_user_profile(
    corp_id: str,
    user_id: str,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[UserProfile]:
    """
    Get a user's profile.
    
    Args:
        corp_id: The corporation ID.
        user_id: The user ID.
        
    Returns:
        MCPResponse[UserProfile]: The response.
    """
    try:
        request = UserProfileRequest(corp_id=corp_id, user_id=user_id)
        data = await user_service.get_user_profile(request)
        
        return MCPResponse.success_response(
            data=UserProfile(
                user_id=data["user_id"],
                corp_id=data["corp_id"],
                name=data["name"],
                last_name=data.get("last_name"),
                first_name=data.get("first_name"),
                area_code=data.get("area_code"),
                mobile=data.get("mobile"),
                gender=data.get("gender"),
                age=data.get("age"),
                city=data.get("city"),
                city_raw=data.get("city_raw"),
                city_mobile=data.get("city_mobile"),
                company_name=data.get("company_name"),
                job_title=data.get("job_title"),
                department=data.get("department"),
                industry=data.get("industry"),
                linkedin_url=data.get("linkedin_url"),
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.post(
    "/user/owner/update",
    response_model=MCPResponse[UpdateUserOwnerResponse],
    summary="Update user's owner",
    description="Update a user's owner",
)
async def update_user_owner(
    request: UpdateUserOwnerRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[UpdateUserOwnerResponse]:
    """
    Update a user's owner.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[UpdateUserOwnerResponse]: The response.
    """
    try:
        data = await user_service.update_user_owner(request)
        
        return MCPResponse.success_response(
            data=UpdateUserOwnerResponse(
                user_id=data["user_id"],
                owner_id=data["owner_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.post(
    "/user/pool/update",
    response_model=MCPResponse[UpdateUserPoolResponse],
    summary="Update user's pool",
    description="Update a user's pool",
)
async def update_user_pool(
    request: UpdateUserPoolRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[UpdateUserPoolResponse]:
    """
    Update a user's pool.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[UpdateUserPoolResponse]: The response.
    """
    try:
        data = await user_service.update_user_pool(request)
        
        return MCPResponse.success_response(
            data=UpdateUserPoolResponse(
                user_id=data["user_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.post(
    "/user/email/update",
    response_model=MCPResponse[UpdateUserEmailResponse],
    summary="Update user's email",
    description="Update a user's email",
)
async def update_user_email(
    request: UpdateUserEmailRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[UpdateUserEmailResponse]:
    """
    Update a user's email.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[UpdateUserEmailResponse]: The response.
    """
    try:
        data = await user_service.update_user_email(request)
        
        return MCPResponse.success_response(
            data=UpdateUserEmailResponse(
                user_id=data["user_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.get(
    "/user/contact/fetch",
    response_model=MCPResponse[FetchUserContactResponse],
    summary="Fetch user's contact",
    description="Fetch a user's contact information",
)
async def fetch_user_contact(
    user_id: str,
    corp_id: str,
    contact_type: str,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[FetchUserContactResponse]:
    """
    Fetch a user's contact information.
    
    Args:
        user_id: The user ID.
        corp_id: The corporation ID.
        contact_type: The contact type.
        
    Returns:
        MCPResponse[FetchUserContactResponse]: The response.
    """
    try:
        request = FetchUserContactRequest(
            user_id=user_id,
            corp_id=corp_id,
            contact_type=contact_type,
        )
        data = await user_service.fetch_user_contact(request)
        
        return MCPResponse.success_response(
            data=FetchUserContactResponse(
                user_id=data["user_id"],
                corp_id=data["corp_id"],
                contact_type=data["contact_type"],
                value=data["value"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))
