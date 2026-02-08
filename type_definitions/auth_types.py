from enum import Enum

class SubscriptionTier(str, Enum):
    FREE = "free"
    PREMIUM = "premium"

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"