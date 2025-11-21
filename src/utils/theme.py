"""Theme configuration for the application."""
import flet as ft


# Color palette
PRIMARY_COLOR = ft.Colors.BLUE_700
SECONDARY_COLOR = ft.Colors.BLUE_400
BACKGROUND_COLOR = ft.Colors.GREY_50
SURFACE_COLOR = ft.Colors.WHITE
ERROR_COLOR = ft.Colors.RED_700
SUCCESS_COLOR = ft.Colors.GREEN_700
TEXT_PRIMARY = ft.Colors.BLACK87
TEXT_SECONDARY = ft.Colors.BLACK54


def get_theme() -> ft.Theme:
    """
    Get the application theme.
    
    Returns:
        Flet Theme object
    """
    return ft.Theme(
        color_scheme_seed=PRIMARY_COLOR,
        use_material3=True,
    )


def get_dark_theme() -> ft.Theme:
    """
    Get the dark theme for the application.
    
    Returns:
        Flet Theme object for dark mode
    """
    return ft.Theme(
        color_scheme_seed=PRIMARY_COLOR,
        use_material3=True,
    )
