"""
Tag-related API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from emeritus_mcp.auth.authentication import mcp_auth
from emeritus_mcp.models.common import MCPResponse
from emeritus_mcp.models.tag import (
    ActivateTagGroupRequest,
    ActivateTagGroupResponse,
    AssignTagRequest,
    AssignTagResponse,
    CreateTagRequest,
    CreateTagResponse,
    DeactivateTagGroupRequest,
    DeactivateTagGroupResponse,
    ListUserTagsRequest,
    ListUserTagsResponse,
    TagGroupListRequest,
    TagGroupListResponse,
    UpdateTagGroupRequest,
    UpdateTagGroupResponse,
    UserTag,
)
from emeritus_mcp.services.tag_service import tag_service

# Create the router
router = APIRouter()


@router.post(
    "/tags/group/create",
    response_model=MCPResponse[CreateTagResponse],
    summary="Create tag group",
    description="Create a new tag group",
)
async def create_tag(
    request: CreateTagRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[CreateTagResponse]:
    """
    Create a tag group.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[CreateTagResponse]: The response.
    """
    try:
        data = await tag_service.create_tag(request)
        
        return MCPResponse.success_response(
            data=CreateTagResponse(
                tags_group_id=data["tags_group_id"],
                corp_id=data["corp_id"],
                name=data["name"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.get(
    "/tags/group/list",
    response_model=MCPResponse[TagGroupListResponse],
    summary="Get tag group list",
    description="Get a list of tag groups",
)
async def get_tag_group_list(
    corp_id: str,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[TagGroupListResponse]:
    """
    Get a list of tag groups.
    
    Args:
        corp_id: The corporation ID.
        
    Returns:
        MCPResponse[TagGroupListResponse]: The response.
    """
    try:
        request = TagGroupListRequest(corp_id=corp_id)
        data = await tag_service.get_tag_group_list(request)
        
        return MCPResponse.success_response(
            data=TagGroupListResponse(
                total=data["total"],
                rows=[
                    {
                        "tags_group_id": row["tags_group_id"],
                        "corp_id": row["corp_id"],
                        "name": row["name"],
                        "variable_name": row["variable_name"],
                        "description": row["description"],
                        "attribute": row["attribute"],
                        "category": row["category"],
                        "is_deleted": row["is_deleted"],
                    }
                    for row in data["rows"]
                ],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.post(
    "/tags/group/update",
    response_model=MCPResponse[UpdateTagGroupResponse],
    summary="Update tag group",
    description="Update a tag group",
)
async def update_tag_group(
    request: UpdateTagGroupRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[UpdateTagGroupResponse]:
    """
    Update a tag group.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[UpdateTagGroupResponse]: The response.
    """
    try:
        data = await tag_service.update_tag_group(request)
        
        return MCPResponse.success_response(
            data=UpdateTagGroupResponse(
                tags_group_id=data["tags_group_id"],
                corp_id=data["corp_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.post(
    "/tags/group/deactivate",
    response_model=MCPResponse[DeactivateTagGroupResponse],
    summary="Deactivate tag group",
    description="Deactivate a tag group",
)
async def deactivate_tag_group(
    request: DeactivateTagGroupRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[DeactivateTagGroupResponse]:
    """
    Deactivate a tag group.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[DeactivateTagGroupResponse]: The response.
    """
    try:
        data = await tag_service.deactivate_tag_group(request)
        
        return MCPResponse.success_response(
            data=DeactivateTagGroupResponse(
                tags_group_id=data["tags_group_id"],
                corp_id=data["corp_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.post(
    "/tags/group/activate",
    response_model=MCPResponse[ActivateTagGroupResponse],
    summary="Activate tag group",
    description="Activate a tag group",
)
async def activate_tag_group(
    request: ActivateTagGroupRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[ActivateTagGroupResponse]:
    """
    Activate a tag group.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[ActivateTagGroupResponse]: The response.
    """
    try:
        data = await tag_service.activate_tag_group(request)
        
        return MCPResponse.success_response(
            data=ActivateTagGroupResponse(
                tags_group_id=data["tags_group_id"],
                corp_id=data["corp_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.post(
    "/user/tags/assign",
    response_model=MCPResponse[AssignTagResponse],
    summary="Assign tag to user",
    description="Assign a tag to a user",
)
async def assign_tag(
    request: AssignTagRequest,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[AssignTagResponse]:
    """
    Assign a tag to a user.
    
    Args:
        request: The request data.
        
    Returns:
        MCPResponse[AssignTagResponse]: The response.
    """
    try:
        data = await tag_service.assign_tag(request)
        
        return MCPResponse.success_response(
            data=AssignTagResponse(
                entity_id=data["entity_id"],
                user_id=data["user_id"],
                tags_group_id=data["tags_group_id"],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))


@router.get(
    "/user/tags/list",
    response_model=MCPResponse[ListUserTagsResponse],
    summary="List user tags",
    description="List tags assigned to a user",
)
async def list_user_tags(
    corp_id: str,
    user_id: str,
    _: HTTPAuthorizationCredentials = Depends(mcp_auth),
) -> MCPResponse[ListUserTagsResponse]:
    """
    List tags assigned to a user.
    
    Args:
        corp_id: The corporation ID.
        user_id: The user ID.
        
    Returns:
        MCPResponse[ListUserTagsResponse]: The response.
    """
    try:
        request = ListUserTagsRequest(corp_id=corp_id, user_id=user_id)
        data = await tag_service.list_user_tags(request)
        
        return MCPResponse.success_response(
            data=ListUserTagsResponse(
                total=data["total"],
                rows=[
                    UserTag(
                        entity_id=row["entity_id"],
                        attribute=row["attribute"],
                        corp_id=row["corp_id"],
                        ctime=row["ctime"],
                        define_value=row["define_value"],
                        executor_id=row["executor_id"],
                        is_deleted=row["is_deleted"],
                        mtime=row["mtime"],
                        source=row["source"],
                        tags_group_id=row["tags_group_id"],
                        user_id=row["user_id"],
                        version=row["version"],
                    )
                    for row in data["rows"]
                ],
            )
        )
    except HTTPException as e:
        return MCPResponse.error_response(message=str(e.detail))
    except Exception as e:
        return MCPResponse.error_response(message=str(e))
