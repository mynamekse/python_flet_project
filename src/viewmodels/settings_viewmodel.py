"""Settings ViewModel - Business logic for settings management.

This ViewModel manages application settings and user preferences.
"""
from .base_viewmodel import BaseViewModel
from models import Settings
from utils import validate_required


class SettingsViewModel(BaseViewModel):
    """ViewModel for settings functionality.
    
    Manages application settings and user preferences.
    Pure Python - can be tested without UI!
    """
    
    def __init__(self, settings: Settings = None):
        """Initialize the settings ViewModel.
        
        Args:
            settings: Initial settings object, creates new if None
        """
        super().__init__()
        self._settings = settings or Settings()
        self.display_name_error: str = ""
        self.save_message: str = ""
        self.is_saving: bool = False
    
    @property
    def settings(self) -> Settings:
        """Get the current settings."""
        return self._settings
    
    @property
    def dark_mode(self) -> bool:
        """Get dark mode setting."""
        return self._settings.dark_mode
    
    @dark_mode.setter
    def dark_mode(self, value: bool) -> None:
        """Set dark mode setting."""
        self._settings.dark_mode = value
        self.notify_listeners()
    
    @property
    def display_name(self) -> str:
        """Get display name."""
        return self._settings.display_name
    
    @display_name.setter
    def display_name(self, value: str) -> None:
        """Set display name."""
        self._settings.display_name = value
        self.notify_listeners()
    
    @property
    def bio(self) -> str:
        """Get bio."""
        return self._settings.bio
    
    @bio.setter
    def bio(self, value: str) -> None:
        """Set bio."""
        self._settings.bio = value
        self.notify_listeners()
    
    def toggle_dark_mode(self) -> None:
        """Toggle dark mode on/off."""
        self._settings.dark_mode = not self._settings.dark_mode
        self.notify_listeners()
    
    def validate_settings(self) -> bool:
        """Validate settings before saving.
        
        Returns:
            True if valid, False otherwise
        """
        self.display_name_error = ""
        
        # Validate display name if provided
        if self._settings.display_name:
            is_valid, error_msg = validate_required(
                self._settings.display_name, 
                "Display Name"
            )
            if not is_valid:
                self.display_name_error = error_msg
                self.notify_listeners()
                return False
        
        return True
    
    def save_settings(self) -> bool:
        """Save the current settings.
        
        This is where you would normally persist settings to storage.
        
        Returns:
            True if save successful, False otherwise
        """
        # Validate first
        if not self.validate_settings():
            return False
        
        # Set saving state
        self.is_saving = True
        self.save_message = ""
        self.notify_listeners()
        
        try:
            # In a real app, this would call a storage service
            # For demo, we just simulate success
            
            self.save_message = "Settings saved successfully!"
            self.is_saving = False
            self.notify_listeners()
            
            return True
            
        except Exception as e:
            self.save_message = f"Failed to save settings: {str(e)}"
            self.is_saving = False
            self.notify_listeners()
            return False
    
    def reset_to_defaults(self) -> None:
        """Reset settings to default values."""
        self._settings = Settings()
        self.display_name_error = ""
        self.save_message = ""
        self.notify_listeners()
    
    def load_settings(self, settings: Settings) -> None:
        """Load settings from storage.
        
        Args:
            settings: Settings object to load
        """
        self._settings = settings
        self.notify_listeners()
