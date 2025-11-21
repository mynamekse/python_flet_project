"""Login view with form validation - MVVM Pattern.

This view is responsible ONLY for UI presentation.
All business logic is in LoginViewModel.
"""
import flet as ft
from components import CustomCard, CustomButton, CustomInput
from viewmodels import LoginViewModel


class LoginView(ft.View):
    """Login view with email and password form.
    
    This view binds to LoginViewModel and updates UI when ViewModel changes.
    Contains NO business logic - only UI code.
    """
    
    def __init__(self, page: ft.Page, viewmodel: LoginViewModel, on_login_success):
        """Initialize the login view.
        
        Args:
            page: The Flet page object
            viewmodel: The LoginViewModel instance
            on_login_success: Callback function when login is successful
        """
        self.page = page
        self.viewmodel = viewmodel
        self.on_login_success = on_login_success
        
        # Listen to ViewModel changes
        self.viewmodel.add_listener(self.on_viewmodel_changed)
        
        # Create input fields
        self.email_input = CustomInput(
            label="Email",
            hint_text="Enter your email (demo@example.com)",
            prefix_icon=ft.Icons.EMAIL,
            on_change=self.on_email_changed,
        )
        
        self.password_input = CustomInput(
            label="Password",
            hint_text="Enter your password (password123)",
            prefix_icon=ft.Icons.LOCK,
            password=True,
            on_change=self.on_password_changed,
        )
        
        # Error text
        self.error_text = ft.Text(
            "",
            color=ft.Colors.RED_700,
            size=14,
            visible=False,
        )
        
        # Create buttons
        self.login_button = CustomButton(
            text="Login",
            icon=ft.Icons.LOGIN,
            width=200,
            on_click=self.handle_login,
        )
        
        # Create the form card
        form_card = CustomCard(
            title="Login",
            content=ft.Column(
                controls=[
                    self.email_input,
                    self.password_input,
                    self.error_text,
                    ft.Container(height=10),
                    ft.Row(
                        controls=[self.login_button],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=15,
                width=400,
            ),
        )
        
        # Initialize the view
        super().__init__(
            route="/login",
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(height=50),
                            ft.Text(
                                "Welcome Back!",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_700,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(height=20),
                            form_card,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            ],
            bgcolor=ft.Colors.GREY_50,
        )
    
    def on_email_changed(self, e):
        """Handle email input change."""
        self.viewmodel.email = e.control.value
        self.viewmodel.clear_errors()
    
    def on_password_changed(self, e):
        """Handle password input change."""
        self.viewmodel.password = e.control.value
        self.viewmodel.clear_errors()
    
    def on_viewmodel_changed(self):
        """Called when ViewModel data changes - update UI."""
        # Update error messages
        self.email_input.error_text = self.viewmodel.email_error or None
        self.password_input.error_text = self.viewmodel.password_error or None
        
        # Update general error
        if self.viewmodel.login_error:
            self.error_text.value = self.viewmodel.login_error
            self.error_text.visible = True
        else:
            self.error_text.visible = False
        
        # Update loading state
        self.login_button.disabled = self.viewmodel.is_loading
        self.login_button.text = "Logging in..." if self.viewmodel.is_loading else "Login"
        
        # Update UI
        self.page.update()
    
    def handle_login(self, e):
        """Handle login button click - delegate to ViewModel."""
        # Call ViewModel's login method (business logic)
        success = self.viewmodel.login()
        
        if success:
            # Show success message
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Login successful!"),
                bgcolor=ft.Colors.GREEN_700,
            )
            self.page.snack_bar.open = True
            self.page.update()
            
            # Call success callback
            if self.on_login_success:
                self.on_login_success(self.viewmodel.current_user)
    
    def dispose(self):
        """Clean up when view is destroyed."""
        self.viewmodel.remove_listener(self.on_viewmodel_changed)
