"""Base ViewModel class for all ViewModels.

This provides the observer pattern implementation for UI updates.
Pure Python - no Flet dependencies.
"""
from typing import Callable, List


class BaseViewModel:
    """Base class for all ViewModels.
    
    Implements the observer pattern to notify views when data changes.
    This allows ViewModels to be developed and tested independently of the UI.
    """
    
    def __init__(self):
        """Initialize the base ViewModel."""
        self._listeners: List[Callable[[], None]] = []
    
    def add_listener(self, listener: Callable[[], None]) -> None:
        """Add a listener that will be called when data changes.
        
        Args:
            listener: Callback function to be called on data changes
        """
        if listener not in self._listeners:
            self._listeners.append(listener)
    
    def remove_listener(self, listener: Callable[[], None]) -> None:
        """Remove a listener.
        
        Args:
            listener: Callback function to remove
        """
        if listener in self._listeners:
            self._listeners.remove(listener)
    
    def notify_listeners(self) -> None:
        """Notify all listeners that data has changed.
        
        This should be called whenever the ViewModel's state changes
        and the UI needs to be updated.
        """
        for listener in self._listeners:
            listener()
    
    def dispose(self) -> None:
        """Clean up resources.
        
        Override this method to clean up any resources when the ViewModel
        is no longer needed.
        """
        self._listeners.clear()
