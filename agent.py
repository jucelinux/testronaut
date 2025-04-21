from ollama import Client
from loguru import logger
from config import config
import asyncio

class TestonautAgent:
    def __init__(self):
        self.mcp = sse_client(config.mcp.url)
        self.ollama = Client(host=config.ollama.url)
        self.current_page = None
        
    async def start(self):
        """Initialize connection and create a new page"""
        try:
            self.current_page = await self.mcp.new_page()
            logger.info("Agent started successfully")
        except Exception as e:
            logger.error(f"Failed to start agent: {e}")
            raise

    async def stop(self):
        """Clean up resources"""
        try:
            if self.current_page:
                await self.current_page.close()
            logger.info("Agent stopped successfully")
        except Exception as e:
            logger.error(f"Failed to stop agent cleanly: {e}")

    async def navigate(self, url: str):
        """Navigate to a URL"""
        try:
            await self.current_page.goto(url)
            logger.info(f"Navigated to {url}")
        except Exception as e:
            logger.error(f"Failed to navigate to {url}: {e}")
            raise

    async def get_page_content(self) -> str:
        """Get the current page content for analysis"""
        try:
            content = await self.current_page.content()
            return content
        except Exception as e:
            logger.error(f"Failed to get page content: {e}")
            raise

async def main():
    """Example usage of the TestonautAgent"""
    agent = TestonautAgent()
    try:
        await agent.start()
        await agent.navigate("https://example.com")
        await asyncio.sleep(2)  # Give some time to see the result
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main()) 