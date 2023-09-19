from pydantic import BaseModel, Field
import pytest

class Post(BaseModel):
    company_id: int = Field(le=4)
    company_name: str
    company_address: str
    company_status: str

# = Field(le=4)
