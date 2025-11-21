"""Home ViewModel - Business logic for home screen.

This ViewModel manages the home screen state and user data.
"""
from .base_viewmodel import BaseViewModel
from models import User


class HomeViewModel(BaseViewModel):
    """ViewModel for home screen functionality.
    
    Manages user data and home screen state.
    Pure Python - can be tested without UI!
    """
    
    def __init__(self, user: User):
        """Initialize the home ViewModel.
        
        Args:
            user: The logged-in user
        """
        super().__init__()
        self._user = user
        self._welcome_message = f"Welcome back, {user.display_name}!"
    
    @property
    def user(self) -> User:
        """Get the current user."""
        return self._user
    
    @property
    def welcome_message(self) -> str:
        """Get the welcome message."""
        return self._welcome_message
    
    def update_user(self, user: User) -> None:
        """Update the user data.
        
        Args:
            user: Updated user object
        """
        self._user = user
        self._welcome_message = f"Welcome back, {user.display_name}!"
        self.notify_listeners()
    
    def get_user_info(self) -> dict:
        """Get user information as a dictionary.
        
        Returns:
            Dictionary containing user information
        """
        return {
            "email": self._user.email,
            "name": self._user.name,
            "display_name": self._user.display_name,
            "bio": self._user.bio,
        }
