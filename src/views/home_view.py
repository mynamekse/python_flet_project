"""Home view - MVVM Pattern.

This view is responsible ONLY for UI presentation.
All business logic is in HomeViewModel.
"""
import flet as ft
from components import CustomCard, CustomButton
from viewmodels import HomeViewModel


class HomeView(ft.View):
    """Home view with welcome message.
    
    This view binds to HomeViewModel and updates UI when ViewModel changes.
    Contains NO business logic - only UI code.
    """
    
    def __init__(self, page: ft.Page, viewmodel: HomeViewModel, on_logout, on_settings):
        """Initialize the home view.
        
        Args:
            page: The Flet page object
            viewmodel: The HomeViewModel instance
            on_logout: Callback function for logout
            on_settings: Callback function to navigate to settings
        """
        self.page = page
        self.viewmodel = viewmodel
        self.on_logout = on_logout
        self.on_settings = on_settings
        
        # Listen to ViewModel changes
        self.viewmodel.add_listener(self.on_viewmodel_changed)
        
        # Welcome text (will be updated from ViewModel)
        self.welcome_text = ft.Text(
            self.viewmodel.welcome_message,
            size=18,
            color=ft.Colors.BLACK87,
        )
        
        # User info text
        user_info = self.viewmodel.get_user_info()
        self.user_info_text = ft.Text(
            f"Email: {user_info['email']}\nDisplay Name: {user_info['display_name']}",
            size=14,
            color=ft.Colors.BLACK54,
        )
        
        # Create welcome card
        welcome_card = CustomCard(
            title="Dashboard",
            content=ft.Column(
                controls=[
                    self.welcome_text,
                    ft.Container(height=10),
                    self.user_info_text,
                    ft.Container(height=10),
                    ft.Text(
                        "This is a simple Flet application demonstrating MVVM pattern.",
                        size=14,
                        color=ft.Colors.BLACK54,
                    ),
                    ft.Container(height=20),
                    ft.Row(
                        controls=[
                            CustomButton(
                                text="Settings",
                                icon=ft.Icons.SETTINGS,
                                variant="secondary",
                                on_click=lambda _: on_settings(),
                            ),
                            CustomButton(
                                text="Logout",
                                icon=ft.Icons.LOGOUT,
                                variant="outline",
                                on_click=lambda _: on_logout(),
                            ),
                        ],
                        spacing=10,
                    ),
                ],
                spacing=10,
                width=500,
            ),
        )
        
        # Initialize the view
        super().__init__(
            route="/home",
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(height=50),
                            ft.Text(
                                "Home",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_700,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(height=20),
                            welcome_card,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            ],
            bgcolor=ft.Colors.GREY_50,
        )
    
    def on_viewmodel_changed(self):
        """Called when ViewModel data changes - update UI."""
        # Update welcome message
        self.welcome_text.value = self.viewmodel.welcome_message
        
        # Update user info
        user_info = self.viewmodel.get_user_info()
        self.user_info_text.value = f"Email: {user_info['email']}\nDisplay Name: {user_info['display_name']}"
        
        # Update UI
        self.page.update()
    
    def dispose(self):
        """Clean up when view is destroyed."""
        self.viewmodel.remove_listener(self.on_viewmodel_changed)
