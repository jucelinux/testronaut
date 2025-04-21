from pocketflow import Node
from loguru import logger
import ollama
import json
from typing import Dict, Optional
from utils.config import config

class CommandParserNode(Node):
    """Node responsible for interpreting natural language commands into structured actions."""
    
    def __init__(self, model_name: str = config.ollama.model):
        """
        Initializes the CommandParserNode.
        
        Args:
            model_name (str): Name of the Ollama model to be used. Default: "dolphin3"
        """
        super().__init__()
        self.model_name = model_name
        
    def exec(self, command: str) -> Optional[Dict]:
        """
        Interprets a natural language command into a structured action.
        
        Args:
            command (str): Natural language command (e.g., "click the login button")
            
        Returns:
            Dict: Structured action in the format:
                {
                    "action": str,      # Action type (click, type, navigate, etc)
                    "target": str,      # Element selector or URL
                    "value": str,       # Optional value (e.g., text to type)
                    "description": str  # Natural language description of the action
                }
        """
        try:
            # Prompt for Ollama to interpret the command
            prompt = f"""You are an assistant specialized in converting test commands into structured actions for web automation.

Analyze the following command and convert it into a structured action:

Command: {command}

The action must follow EXACTLY this JSON format:
{{
    "action": "action_type",    // click, type, navigate, wait, etc
    "target": "selector",       // CSS Selector, XPath or URL
    "value": "optional_value",  // Text to type, time to wait, etc
    "description": "description" // Clear description of the action in English
}}

Important rules:
1. For clicks: use "click" as action and the element selector as target
2. For typing: use "type" as action, field selector as target and the text as value
3. For navigation: use "navigate" as action and the URL as target
4. For waiting: use "wait" as action and time in seconds as value
5. Use specific selectors (IDs, names, etc) when possible
6. The description must be clear and in English

Return ONLY the JSON, without additional explanations."""

            # Call Ollama to interpret the command
            logger.debug(f"Sending command for interpretation: {command}")
            response = ollama.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
            )
            
            # Extract and validate JSON response
            try:
                action_json = json.loads(response.message.content)
                required_fields = ["action", "target", "description"]
                
                # Validate required fields
                if not all(field in action_json for field in required_fields):
                    missing = [f for f in required_fields if f not in action_json]
                    logger.error(f"Missing required fields in response: {missing}")
                    return None
                
                # Add empty value if not present
                if "value" not in action_json:
                    action_json["value"] = ""
                
                logger.info(f"Command interpreted successfully: {action_json}")
                return action_json
                
            except json.JSONDecodeError as e:
                logger.error(f"Error decoding JSON from response: {e}")
                logger.debug(f"Received response: {response.message.content}")
                return None
                
        except Exception as e:
            logger.error(f"Error interpreting command: {e}")
            return None 