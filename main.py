#!/usr/bin/env python3
"""
Jarvis2 - Educational Artificial Intelligence Assistant
Main entry point
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from jarvis import Jarvis2


def main():
    """
    Main function - starts the Jarvis2 assistant
    """
    print("="*60)
    print("Welcome to Jarvis2 - Educational AI Assistant")
    print("="*60)
    print()
    
    # Initialize Jarvis2
    jarvis = Jarvis2()
    
    print(f"Status: {jarvis.status}")
    print("Type 'help' for commands or 'exit' to quit.")
    print("-" * 60)
    print()
    
    # Main interaction loop
    try:
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Jarvis2. Goodbye!")
                break
            
            if user_input.lower() == 'help':
                jarvis.show_help()
                continue
            
            # Process user input
            response = jarvis.process(user_input)
            print(f"\nJarvis2: {response}\n")
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
