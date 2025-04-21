import base64
from fastmcp import Client
from fastmcp.client.transports import NpxStdioTransport
from loguru import logger
import asyncio
from typing import Optional, Dict, Any
from functools import wraps

class PlaywrightMCPClient:
    _instance = None
    _client = None
    _mcp = None
    _tools = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._client:
          transport = NpxStdioTransport("@playwright/mcp@latest", ["--headless"])
          self._client = Client(transport=transport)
    
    @classmethod
    async def get_instance(cls) -> 'PlaywrightMCPClient':
        """Gets the singleton instance of the class"""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
    
    async def __aenter__(self):
        """Manages the async context"""
        if not self._mcp:
            self._mcp = await self._client.__aenter__()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Cleans up resources when exiting context"""
        if self._mcp:
            await self._client.__aexit__(exc_type, exc_val, exc_tb)
            self._mcp = None
    
    async def list_tools(self) -> Dict:
        """Lists all available tools"""
        if not self._mcp:
            raise RuntimeError("MCP client not initialized. Use 'async with' to initialize.")
        
        if not self._tools:
            self._tools = await self._mcp.list_tools()
            return self._tools
        else:
            return self._tools
    
    async def call_tool(self, tool_name: str, tool_args: Dict[str, Any]) -> Any:
        """
        Calls a specific tool with the provided arguments
        
        Args:
            tool_name: Name of the tool to call
            tool_args: Dictionary with the tool arguments
            
        Returns:
            Result of the tool execution
        """
        if not self._mcp:
            raise RuntimeError("MCP client not initialized. Use 'async with' to initialize.")
        return await self._mcp.call_tool(tool_name, tool_args)

async def example_usage():
    """Example of how to use the PlaywrightMCP class"""
    async with await PlaywrightMCPClient.get_instance() as mcp:
        # List all available tools
        tools = await mcp.list_tools()
        print("\nAvailable tools:")
        print(tools)
        browser_navigate = await mcp.call_tool("browser_navigate", {"url": "https://github.com/ollama/ollama-python"})
        print(browser_navigate)
        browser_take_screenshot = await mcp.call_tool("browser_take_screenshot", {"raw": False})
        with open("screenshot.jpeg", "wb") as f:
            f.write(base64.b64decode(browser_take_screenshot[0].data))
        print("Screenshot saved as 'screenshot.png'")
        
if __name__ == "__main__":
    asyncio.run(example_usage())
