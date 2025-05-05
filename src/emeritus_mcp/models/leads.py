"""
Leads-related data models.
"""
from typing import List, Optional

from pydantic import BaseModel, Field


class ImportLeadsRequest(BaseModel):
    """Request model for importing leads."""
    
    corp_id: str = Field(..., description="Organization ID")
    user_id: Optional[str] = Field(None, description="User ID")
    area_code: Optional[str] = Field(None, description="Area code")
    mobile: Optional[str] = Field(None, description="Mobile number")
    name: Optional[str] = Field(None, description="User name")
    utm_source: Optional[str] = Field(None, description="UTM source")
    utm_medium: Optional[str] = Field(None, description="UTM medium")
    utm_campaign: Optional[str] = Field(None, description="UTM campaign")
    utm_channel: Optional[str] = Field(None, description="UTM channel")
    utm_keyword: Optional[str] = Field(None, description="UTM keyword")
    utm_term: Optional[str] = Field(None, description="UTM term")
    campaign: Optional[str] = Field(None, description="Campaign")
    is_corporate_training: Optional[bool] = Field(None, description="Is corporate training")
    form1_name: Optional[str] = Field(None, description="Form1 name")
    form1_value: Optional[str] = Field(None, description="Form1 value")
    form2_name: Optional[str] = Field(None, description="Form2 name")
    form2_value: Optional[str] = Field(None, description="Form2 value")
    form3_name: Optional[str] = Field(None, description="Form3 name")
    form3_value: Optional[str] = Field(None, description="Form3 value")
    form4_name: Optional[str] = Field(None, description="Form4 name")
    form4_value: Optional[str] = Field(None, description="Form4 value")
    entry_id: Optional[str] = Field(None, description="Entry ID")
    page_id: Optional[str] = Field(None, description="Page ID")
    course_code: Optional[str] = Field(None, description="Course code")
    bd_vid: Optional[str] = Field(None, description="Business Development VID")
    company_name: Optional[str] = Field(None, description="Company name")
    work_exp: Optional[str] = Field(None, description="Work experience")
    job_title: Optional[str] = Field(None, description="Job title")
    department: Optional[str] = Field(None, description="Department")
    city: Optional[str] = Field(None, description="City")
    owner_ids: Optional[List[str]] = Field(None, description="Owner IDs")
    oid: Optional[str] = Field(None, description="Owner ID (legacy)")
    
    class Config:
        """Pydantic model configuration."""
        
        validate_assignment = True
        
        @classmethod
        def get_validators(cls):
            """Get validators for the model."""
            yield cls.validate_user_identification
        
        @classmethod
        def validate_user_identification(cls, values):
            """
            Validate that either user_id or (area_code and mobile) are provided.
            
            Args:
                values: The values to validate.
                
            Returns:
                The validated values.
                
            Raises:
                ValueError: If neither user_id nor (area_code and mobile) are provided.
            """
            user_id = values.get("user_id")
            area_code = values.get("area_code")
            mobile = values.get("mobile")
            
            if not user_id and not (area_code and mobile):
                raise ValueError(
                    "Either user_id or both area_code and mobile must be provided"
                )
            
            return values


class ImportLeadsResponse(BaseModel):
    """Response model for importing leads."""
    
    lead_id: str = Field(..., description="Lead ID")
