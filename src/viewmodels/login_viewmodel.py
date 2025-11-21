"""Login ViewModel - Business logic for login functionality.

This ViewModel contains all login-related business logic and can be
developed and tested independently of the UI.
"""
from typing import Optional
from .base_viewmodel import BaseViewModel
from models import User
from utils import validate_email, validate_password


class LoginViewModel(BaseViewModel):
    """ViewModel for login functionality.
    
    Contains all business logic for user authentication.
    Pure Python - can be tested without UI!
    """
    
    def __init__(self):
        """Initialize the login ViewModel."""
        super().__init__()
        self.email: str = ""
        self.password: str = ""
        self.email_error: str = ""
        self.password_error: str = ""
        self.is_loading: bool = False
        self.login_error: str = ""
        self._current_user: Optional[User] = None
    
    @property
    def current_user(self) -> Optional[User]:
        """Get the current logged-in user."""
        return self._current_user
    
    def validate_form(self) -> bool:
        """Validate the login form.
        
        Returns:
            True if form is valid, False otherwise
        """
        # Reset errors
        self.email_error = ""
        self.password_error = ""
        self.login_error = ""
        
        # Validate email
        email_valid, email_msg = validate_email(self.email)
        if not email_valid:
            self.email_error = email_msg
        
        # Validate password
        password_valid, password_msg = validate_password(self.password)
        if not password_valid:
            self.password_error = password_msg
        
        # Notify listeners to update UI
        self.notify_listeners()
        
        return email_valid and password_valid
    
    def login(self) -> bool:
        """Perform login operation.
        
        This is where you would normally call an authentication service.
        For demo purposes, we accept any valid email/password.
        
        Returns:
            True if login successful, False otherwise
        """
        # Validate form first
        if not self.validate_form():
            return False
        
        # Set loading state
        self.is_loading = True
        self.notify_listeners()
        
        # Simulate authentication
        # In a real app, this would call an authentication service
        try:
            # For demo: accept any valid credentials
            # You can add specific checks here, e.g.:
            # if self.email == "demo@example.com" and self.password == "password123":
            
            # Create user object
            self._current_user = User(
                email=self.email,
                name=self.email.split("@")[0].capitalize()
            )
            
            # Clear form
            self.password = ""
            self.is_loading = False
            self.notify_listeners()
            
            return True
            
        except Exception as e:
            self.login_error = f"Login failed: {str(e)}"
            self.is_loading = False
            self.notify_listeners()
            return False
    
    def logout(self) -> None:
        """Logout the current user."""
        self._current_user = None
        self.email = ""
        self.password = ""
        self.email_error = ""
        self.password_error = ""
        self.login_error = ""
        self.notify_listeners()
    
    def clear_errors(self) -> None:
        """Clear all error messages."""
        self.email_error = ""
        self.password_error = ""
        self.login_error = ""
        self.notify_listeners()
