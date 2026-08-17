"""
Jarvis2 - Main AI Assistant Class

Core logic for the educational AI assistant
"""

import logging
from datetime import datetime
from typing import Optional

# Setup logging
logger = logging.getLogger(__name__)


class Jarvis2:
    """
    Jarvis2 Educational AI Assistant
    
    Main class that handles all interactions and educational logic
    """
    
    def __init__(self, config: Optional[dict] = None):
        """
        Initialize Jarvis2
        
        Args:
            config: Optional configuration dictionary
        """
        self.name = "Jarvis2"
        self.version = "1.0.0"
        self.status = "✓ Ready"
        self.config = config or {}
        self.conversation_history = []
        self.created_at = datetime.now()
        
        logger.info(f"{self.name} v{self.version} initialized")
    
    def process(self, user_input: str) -> str:
        """
        Process user input and generate response
        
        Args:
            user_input: User's question or statement
            
        Returns:
            AI-generated response
        """
        # Store in conversation history
        self.conversation_history.append({
            "timestamp": datetime.now(),
            "role": "user",
            "content": user_input
        })
        
        # Process the input
        response = self._generate_response(user_input)
        
        # Store response in history
        self.conversation_history.append({
            "timestamp": datetime.now(),
            "role": "assistant",
            "content": response
        })
        
        return response
    
    def _generate_response(self, user_input: str) -> str:
        """
        Generate response based on user input
        
        Args:
            user_input: The user's question
            
        Returns:
            Generated response
        """
        response = (
            f"I understand your question: '{user_input}'\n"
            f"I'm Jarvis2, your educational AI assistant. "
            f"I'm here to help you learn and understand concepts better!"
        )
        
        return response
    
    def show_help(self) -> None:
        """
        Display help information
        """
        help_text = """
        Available Commands:
        ==================
        
        help    - Show this help message
        exit    - Exit the program
        status  - Show current status
        
        Ask any educational question and I'll try to help!
        """
        print(help_text)
    
    def get_conversation_history(self) -> list:
        """
        Get the current conversation history
        
        Returns:
            List of conversation turns
        """
        return self.conversation_history.copy()
    
    def clear_history(self) -> None:
        """
        Clear conversation history
        """
        self.conversation_history = []
        logger.info("Conversation history cleared")
