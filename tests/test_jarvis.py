"""
Tests for Jarvis2 AI Assistant
"""

import sys
from pathlib import Path
import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jarvis import Jarvis2


class TestJarvis2:
    """
    Test suite for Jarvis2
    """
    
    def test_initialization(self):
        """Test Jarvis2 initialization"""
        jarvis = Jarvis2()
        assert jarvis.name == "Jarvis2"
        assert jarvis.version == "1.0.0"
        assert jarvis.status == "✓ Ready"
    
    def test_process_input(self):
        """Test processing user input"""
        jarvis = Jarvis2()
        response = jarvis.process("What is Python?")
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_conversation_history(self):
        """Test conversation history tracking"""
        jarvis = Jarvis2()
        assert len(jarvis.conversation_history) == 0
        
        jarvis.process("Hello")
        assert len(jarvis.conversation_history) == 2
    
    def test_clear_history(self):
        """Test clearing conversation history"""
        jarvis = Jarvis2()
        jarvis.process("Test message")
        assert len(jarvis.conversation_history) > 0
        
        jarvis.clear_history()
        assert len(jarvis.conversation_history) == 0
