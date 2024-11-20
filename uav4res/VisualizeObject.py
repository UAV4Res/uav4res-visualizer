from abc import ABC, abstractmethod


# Abstract class for a game state
class VisualizeObject(ABC):
    @abstractmethod
    def handle_events(self):
        """Handle user input."""
        pass

    @abstractmethod
    def update(self):
        """Update the game logic."""
        pass

    @abstractmethod
    def draw(self):
        """Render the game state."""
        pass

    @abstractmethod
    def clean(self):
        """Clean the game state."""
        pass
