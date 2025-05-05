"""
Tag-related data models.
"""
from typing import List, Optional

from pydantic import BaseModel, Field


class CreateTagRequest(BaseModel):
    """Request model for creating a tag group."""
    
    name: str = Field(..., description="Tag name")
    variable_name: str = Field(..., description="Tag variable name")
    description: str = Field(..., description="Tag description")
    attribute: str = Field(..., description="Attribute (define/number/string)")
    category: str = Field(..., description="Category")
    corp_id: str = Field(..., description="Organization ID")


class CreateTagResponse(BaseModel):
    """Response model for creating a tag group."""
    
    tags_group_id: str = Field(..., description="The ID of tag group")
    corp_id: str = Field(..., description="Organization ID")
    name: str = Field(..., description="Tag group name")


class TagGroupListRequest(BaseModel):
    """Request model for fetching tag group list."""
    
    corp_id: str = Field(..., description="Organization ID")


class TagGroup(BaseModel):
    """Tag group model."""
    
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")
    name: str = Field(..., description="Tag group name")
    variable_name: str = Field(..., description="Tag variable name")
    description: str = Field(..., description="Tag description")
    attribute: str = Field(..., description="Attribute")
    category: str = Field(..., description="Category")
    is_deleted: bool = Field(..., description="Is deleted flag")


class TagGroupListResponse(BaseModel):
    """Response model for fetching tag group list."""
    
    total: int = Field(..., description="Total number of tag groups")
    rows: List[TagGroup] = Field(..., description="List of tag groups")


class UpdateTagGroupRequest(BaseModel):
    """Request model for updating a tag group."""
    
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")
    name: Optional[str] = Field(None, description="Tag group name")
    description: Optional[str] = Field(None, description="Tag description")
    category: Optional[str] = Field(None, description="Category")


class UpdateTagGroupResponse(BaseModel):
    """Response model for updating a tag group."""
    
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")


class DeactivateTagGroupRequest(BaseModel):
    """Request model for deactivating a tag group."""
    
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")


class DeactivateTagGroupResponse(BaseModel):
    """Response model for deactivating a tag group."""
    
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")


class ActivateTagGroupRequest(BaseModel):
    """Request model for activating a tag group."""
    
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")


class ActivateTagGroupResponse(BaseModel):
    """Response model for activating a tag group."""
    
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")


class AssignTagRequest(BaseModel):
    """Request model for assigning a tag to a user."""
    
    user_id: str = Field(..., description="User ID")
    tags_group_id: str = Field(..., description="Tag group ID")
    corp_id: str = Field(..., description="Organization ID")
    define_value: bool = Field(..., description="Define value")


class AssignTagResponse(BaseModel):
    """Response model for assigning a tag to a user."""
    
    entity_id: str = Field(..., description="Entity ID")
    user_id: str = Field(..., description="User ID")
    tags_group_id: str = Field(..., description="Tag group ID")


class ListUserTagsRequest(BaseModel):
    """Request model for listing user tags."""
    
    corp_id: str = Field(..., description="Organization ID")
    user_id: str = Field(..., description="User ID")


class UserTag(BaseModel):
    """User tag model."""
    
    entity_id: str = Field(..., description="Entity ID")
    attribute: str = Field(..., description="Attribute")
    corp_id: str = Field(..., description="Organization ID")
    ctime: str = Field(..., description="Creation time")
    define_value: bool = Field(..., description="Define value")
    executor_id: str = Field(..., description="Executor ID")
    is_deleted: bool = Field(..., description="Is deleted flag")
    mtime: str = Field(..., description="Modification time")
    source: str = Field(..., description="Source")
    tags_group_id: str = Field(..., description="Tag group ID")
    user_id: str = Field(..., description="User ID")
    version: int = Field(..., description="Version")


class ListUserTagsResponse(BaseModel):
    """Response model for listing user tags."""
    
    total: int = Field(..., description="Total number of tags")
    rows: List[UserTag] = Field(..., description="List of tags")
