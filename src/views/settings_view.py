"""Settings view - MVVM Pattern.

This view is responsible ONLY for UI presentation.
All business logic is in SettingsViewModel.
"""
import flet as ft
from components import CustomCard, CustomButton, CustomInput
from viewmodels import SettingsViewModel


class SettingsView(ft.View):
    """Settings view with user preferences.
    
    This view binds to SettingsViewModel and updates UI when ViewModel changes.
    Contains NO business logic - only UI code.
    """
    
    def __init__(self, page: ft.Page, viewmodel: SettingsViewModel, on_back):
        """Initialize the settings view.
        
        Args:
            page: The Flet page object
            viewmodel: The SettingsViewModel instance
            on_back: Callback function to go back
        """
        self.page = page
        self.viewmodel = viewmodel
        self.on_back = on_back
        
        # Listen to ViewModel changes
        self.viewmodel.add_listener(self.on_viewmodel_changed)
        
        # Create input fields
        self.name_input = CustomInput(
            label="Display Name",
            hint_text="Enter your name",
            prefix_icon=ft.Icons.PERSON,
            value=self.viewmodel.display_name,
            on_change=self.on_name_changed,
        )
        
        self.bio_input = CustomInput(
            label="Bio",
            hint_text="Tell us about yourself",
            prefix_icon=ft.Icons.INFO,
            multiline=True,
            max_lines=3,
            value=self.viewmodel.bio,
            on_change=self.on_bio_changed,
        )
        
        # Theme toggle
        self.dark_mode_switch = ft.Switch(
            label="Dark Mode",
            value=self.viewmodel.dark_mode,
            on_change=self.on_dark_mode_changed,
        )
        
        # Save message
        self.save_message = ft.Text(
            "",
            color=ft.Colors.GREEN_700,
            size=14,
            visible=False,
        )
        
        # Create settings card
        settings_card = CustomCard(
            title="Settings",
            content=ft.Column(
                controls=[
                    self.name_input,
                    self.bio_input,
                    ft.Container(height=10),
                    self.dark_mode_switch,
                    self.save_message,
                    ft.Container(height=20),
                    ft.Row(
                        controls=[
                            CustomButton(
                                text="Save",
                                icon=ft.Icons.SAVE,
                                on_click=self.handle_save,
                            ),
                            CustomButton(
                                text="Back",
                                icon=ft.Icons.ARROW_BACK,
                                variant="outline",
                                on_click=lambda _: on_back(),
                            ),
                        ],
                        spacing=10,
                    ),
                ],
                spacing=15,
                width=500,
            ),
        )
        
        # Initialize the view
        super().__init__(
            route="/settings",
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(height=50),
                            ft.Text(
                                "Settings",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_700,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(height=20),
                            settings_card,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            ],
            bgcolor=ft.Colors.GREY_50,
        )
    
    def on_name_changed(self, e):
        """Handle name input change."""
        self.viewmodel.display_name = e.control.value
    
    def on_bio_changed(self, e):
        """Handle bio input change."""
        self.viewmodel.bio = e.control.value
    
    def on_dark_mode_changed(self, e):
        """Handle dark mode toggle."""
        self.viewmodel.dark_mode = e.control.value
        # Apply theme change immediately
        self.page.theme_mode = (
            ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT
        )
        self.page.update()
    
    def on_viewmodel_changed(self):
        """Called when ViewModel data changes - update UI."""
        # Update error messages
        self.name_input.error_text = self.viewmodel.display_name_error or None
        
        # Update save message
        if self.viewmodel.save_message:
            self.save_message.value = self.viewmodel.save_message
            self.save_message.visible = True
        else:
            self.save_message.visible = False
        
        # Update UI
        self.page.update()
    
    def handle_save(self, e):
        """Handle save button click - delegate to ViewModel."""
        # Call ViewModel's save method (business logic)
        success = self.viewmodel.save_settings()
        
        if success:
            # Show success snackbar
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Settings saved successfully!"),
                bgcolor=ft.Colors.GREEN_700,
            )
            self.page.snack_bar.open = True
            self.page.update()
    
    def dispose(self):
        """Clean up when view is destroyed."""
        self.viewmodel.remove_listener(self.on_viewmodel_changed)
