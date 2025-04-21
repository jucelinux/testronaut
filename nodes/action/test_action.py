import json
import asyncio

from nodes.action.parser import CommandParserNode

async def test_action_system():
    """Tests the complete action system."""
    parser = CommandParserNode()
    
    test_commands = [
        "navigate to https://example.com",
        "take a screenshot of the page"
    ]
    
    print("\n=== Action System Test ===\n")
    
    for cmd in test_commands:
        print(f"\n>> Command: {cmd}")
        
        # Step 1: Interpret the command
        action = parser.exec(cmd)
        print(f"1. Structured Action: {json.dumps(action, indent=2, ensure_ascii=False)}")
        
        # TODO: integrating with dolphin-mcp
        
if __name__ == "__main__":
    asyncio.run(test_action_system()) 