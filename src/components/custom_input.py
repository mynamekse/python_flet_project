"""Custom input field component."""
import flet as ft


class CustomInput(ft.TextField):
    """A custom input field with validation support."""
    
    def __init__(
        self,
        label: str,
        hint_text: str = None,
        password: bool = False,
        validator=None,
        prefix_icon: str = None,
        multiline: bool = False,
        max_lines: int = 1,
        value: str = "",
        on_change=None,
        **kwargs
    ):
        """
        Initialize the custom input field.
        
        Args:
            label: Input label
            hint_text: Placeholder text
            password: Whether this is a password field
            validator: Validation function that returns (is_valid, error_message)
            prefix_icon: Optional icon to show before the input
            multiline: Whether to allow multiple lines
            max_lines: Maximum number of lines for multiline input
            value: Initial value
            on_change: Change event handler
            **kwargs: Additional TextField properties
        """
        self.validator_func = validator
        
        super().__init__(
            label=label,
            hint_text=hint_text,
            password=password,
            can_reveal_password=password,
            prefix_icon=prefix_icon,
            multiline=multiline,
            max_lines=max_lines,
            value=value,
            on_change=on_change,
            border_radius=8,
            border_color=ft.Colors.BLUE_200,
            focused_border_color=ft.Colors.BLUE_700,
            filled=True,
            bgcolor=ft.Colors.BLUE_50,
            **kwargs
        )
    
    def validate_input(self) -> bool:
        """
        Validate the input using the provided validator.
        
        Returns:
            True if valid, False otherwise
        """
        if self.validator_func:
            is_valid, error_msg = self.validator_func(self.value or "")
            if not is_valid:
                self.error_text = error_msg
                self.update()
                return False
            else:
                self.error_text = None
                self.update()
                return True
        return True
