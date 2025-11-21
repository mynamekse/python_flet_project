"""Settings data model."""
from dataclasses import dataclass


@dataclass
class Settings:
    """Application settings data model.
    
    This is a pure data class with no business logic.
    Used to represent user preferences and application settings.
    """
    dark_mode: bool = False
    display_name: str = ""
    bio: str = ""
    language: str = "en"
    notifications_enabled: bool = True
    
    def __str__(self) -> str:
        """String representation of settings."""
        return f"Settings(dark_mode={self.dark_mode}, display_name={self.display_name})"
    
    def to_dict(self) -> dict:
        """Convert settings to dictionary for serialization."""
        return {
            "dark_mode": self.dark_mode,
            "display_name": self.display_name,
            "bio": self.bio,
            "language": self.language,
            "notifications_enabled": self.notifications_enabled,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Settings":
        """Create Settings instance from dictionary."""
        return cls(
            dark_mode=data.get("dark_mode", False),
            display_name=data.get("display_name", ""),
            bio=data.get("bio", ""),
            language=data.get("language", "en"),
            notifications_enabled=data.get("notifications_enabled", True),
        )
