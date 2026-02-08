from pydantic import BaseModel

class UserDTO(BaseModel):
    id: int
    email: str
    username: str
    subscription_tier: str
    role: str
    is_banned: bool | None = None
    created_at: str

class AuthCredentials(BaseModel):
    user: UserDTO
    token: str

class AuthResponseDTO(BaseModel):
    success: bool
    message: str
    data: AuthCredentials