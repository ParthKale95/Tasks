from pydantic import BaseModel
from typing import Optional


class Member(BaseModel):
    id: Optional[str] = None
    name: str
    age: int
    membership_type: str
    phone: str


class UpdateMember(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    membership_type: Optional[str] = None
    phone: Optional[str] = None
