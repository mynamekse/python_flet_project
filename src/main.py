"""Main application entry point - MVVM Pattern.

This file creates ViewModels and passes them to Views.
ViewModels contain business logic, Views contain UI code.
"""
import flet as ft
from views import LoginView, HomeView, SettingsView
from viewmodels import LoginViewModel, HomeViewModel, SettingsViewModel
from models import Settings
from utils import get_theme


def main(page: ft.Page):
    """Main application function.
    
    Creates ViewModels and manages navigation between Views.
    
    Args:
        page: The Flet page object
    """
    # Configure page
    page.title = "Flet Form App - MVVM"
    page.theme = get_theme()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window_width = 900
    page.window_height = 700
    page.window_resizable = True
    
    # Create ViewModels (can be created once and reused)
    login_vm = LoginViewModel()
    settings_vm = SettingsViewModel(Settings())
    
    # Home ViewModel will be created after login with user data
    home_vm = None
    
    # Navigation functions
    def go_to_home(user):
        """Navigate to home view.
        
        Args:
            user: The logged-in user from LoginViewModel
        """
        nonlocal home_vm
        
        # Create HomeViewModel with user data
        home_vm = HomeViewModel(user)
        
        page.views.clear()
        page.views.append(
            HomeView(
                page=page,
                viewmodel=home_vm,
                on_logout=go_to_login,
                on_settings=go_to_settings,
            )
        )
        page.update()
    
    def go_to_login():
        """Navigate to login view."""
        # Reset login ViewModel
        login_vm.logout()
        
        page.views.clear()
        page.views.append(
            LoginView(
                page=page,
                viewmodel=login_vm,
                on_login_success=go_to_home,
            )
        )
        page.update()
    
    def go_to_settings():
        """Navigate to settings view."""
        page.views.clear()
        page.views.append(
            SettingsView(
                page=page,
                viewmodel=settings_vm,
                on_back=lambda: go_to_home(home_vm.user) if home_vm else go_to_login(),
            )
        )
        page.update()
    
    # Start with login view
    go_to_login()


if __name__ == "__main__":
    ft.app(target=main)
