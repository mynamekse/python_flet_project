"""User data model."""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    """User data model.
    
    This is a pure data class with no business logic.
    Used to represent user information throughout the application.
    """
    email: str
    name: str = ""
    bio: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    
    def __str__(self) -> str:
        """String representation of the user."""
        return f"User(email={self.email}, name={self.name})"
    
    @property
    def display_name(self) -> str:
        """Get display name, fallback to email if name is empty."""
        return self.name if self.name else self.email.split("@")[0]
