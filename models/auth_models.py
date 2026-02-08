from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, NonNegativeInt, StrictBool

from type_definitions.auth_types import SubscriptionTier, UserRole

class UserDTO(BaseModel):
    id: NonNegativeInt
    email: EmailStr
    username: str = Field(min_length=3, max_length=32)
    subscription_tier: SubscriptionTier
    role: UserRole
    is_banned: StrictBool | None = None
    created_at: datetime

class AuthCredentials(BaseModel):
    user: UserDTO
    token: str

class AuthResponseDTO(BaseModel):
    success: StrictBool
    message: str
    data: AuthCredentials