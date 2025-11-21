"""Custom card component."""
import flet as ft


class CustomCard(ft.Container):
    """A custom card component with consistent styling."""
    
    def __init__(
        self,
        content: ft.Control,
        title: str = None,
        padding: int = 20,
        **kwargs
    ):
        """
        Initialize the custom card.
        
        Args:
            content: The content to display in the card
            title: Optional title for the card
            padding: Padding around the content
            **kwargs: Additional Container properties
        """
        # Build the card content
        card_content = []
        
        if title:
            card_content.append(
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK87,
                )
            )
            card_content.append(ft.Divider(height=20, color=ft.Colors.TRANSPARENT))
        
        card_content.append(content)
        
        super().__init__(
            content=ft.Column(
                controls=card_content,
                spacing=0,
            ),
            padding=padding,
            border_radius=12,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.Colors.BLACK12,
                offset=ft.Offset(0, 2),
            ),
            **kwargs
        )
