"""MCP (Model Context Protocol) toolset configuration."""

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from loguru import logger

async def get_playwright_mcp_toolset():
    """Create and configure the MCP toolset.
    
    Returns:
        Tuple[MCPToolset, AsyncExitStack]: The configured toolset and its exit stack.
    """
    print("Attempting to connect to MCP Playwright server...")
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command='npx',
            args=["@playwright/mcp@latest", 
                  "--headless",
                  "--caps=\"browser_wait,browser_handle_dialog,browser_file_upload,browser_press_key,browser_navigate,browser_navigate_back,browser_click,browser_drag,browser_hover,browser_type,browser_select_option,browser_take_screenshot\""
                  ],
        )
    )
    return tools, exit_stack 