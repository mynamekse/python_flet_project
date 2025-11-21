"""Custom button component."""
import flet as ft


class CustomButton(ft.ElevatedButton):
    """A custom button with consistent styling."""
    
    def __init__(
        self,
        text: str,
        on_click=None,
        icon: str = None,
        width: int = None,
        variant: str = "primary",
        **kwargs
    ):
        """
        Initialize the custom button.
        
        Args:
            text: Button text
            on_click: Click event handler
            icon: Optional icon name
            width: Button width
            variant: Button style variant ('primary', 'secondary', 'outline')
            **kwargs: Additional ElevatedButton properties
        """
        # Set Colors based on variant
        if variant == "primary":
            bgcolor = ft.Colors.BLUE_700
            color = ft.Colors.WHITE
        elif variant == "secondary":
            bgcolor = ft.Colors.BLUE_400
            color = ft.Colors.WHITE
        elif variant == "outline":
            bgcolor = ft.Colors.TRANSPARENT
            color = ft.Colors.BLUE_700
        else:
            bgcolor = ft.Colors.BLUE_700
            color = ft.Colors.WHITE
        
        super().__init__(
            text=text,
            icon=icon,
            on_click=on_click,
            width=width,
            bgcolor=bgcolor,
            color=color,
            elevation=2 if variant != "outline" else 0,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=ft.padding.symmetric(horizontal=20, vertical=12),
            ),
            **kwargs
        )
