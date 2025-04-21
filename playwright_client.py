from fastmcp import Client
from fastmcp.client.transports import NpxStdioTransport
from loguru import logger
import asyncio
from typing import Optional, Dict, Any
from functools import wraps

class PlaywrightMCP:
    _instance = None
    _client = None
    _mcp = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._client:
          transport = NpxStdioTransport("@playwright/mcp@latest", ["--headless"])
          self._client = Client(transport=transport)
    
    @classmethod
    async def get_instance(cls) -> 'PlaywrightMCP':
        """Obtém a instância singleton da classe"""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
    
    async def __aenter__(self):
        """Gerencia o contexto assíncrono"""
        if not self._mcp:
            self._mcp = await self._client.__aenter__()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Limpa recursos ao sair do contexto"""
        if self._mcp:
            await self._client.__aexit__(exc_type, exc_val, exc_tb)
            self._mcp = None
    
    async def list_tools(self) -> Dict:
        """Lista todas as ferramentas disponíveis"""
        if not self._mcp:
            raise RuntimeError("Cliente MCP não inicializado. Use 'async with' para inicializar.")
        return await self._mcp.list_tools()
    
    async def call_tool(self, tool_name: str, tool_args: Dict[str, Any]) -> Any:
        """
        Chama uma ferramenta específica com os argumentos fornecidos
        
        Args:
            tool_name: Nome da ferramenta a ser chamada
            tool_args: Dicionário com os argumentos da ferramenta
            
        Returns:
            Resultado da execução da ferramenta
        """
        if not self._mcp:
            raise RuntimeError("Cliente MCP não inicializado. Use 'async with' para inicializar.")
        return await self._mcp.call_tool(tool_name, tool_args)

    # Métodos de conveniência para ações comuns
    async def navigate(self, url: str):
        """Navega para uma URL específica"""
        return await self.call_tool("browser_navigate", {"url": url})
    
    async def click(self, element: str, ref: str):
        """Clica em um elemento na página"""
        return await self.call_tool("browser_click", {
            "element": element,
            "ref": ref
        })
    
    async def type(self, element: str, ref: str, text: str, submit: bool = False):
        """Digite texto em um elemento"""
        return await self.call_tool("browser_type", {
            "element": element,
            "ref": ref,
            "text": text,
            "submit": submit
        })
    
    async def take_snapshot(self):
        """Captura um snapshot da página atual"""
        return await self.call_tool("browser_snapshot", {})
    
    async def take_screenshot(self):
        """Captura um screenshot da página atual"""
        return await self.call_tool("browser_take_screenshot", {})

async def example_usage():
    """Exemplo de como usar a classe PlaywrightMCP"""
    async with await PlaywrightMCP.get_instance() as mcp:
        # Lista todas as tools disponíveis
        tools = await mcp.list_tools()
        print("\nTools disponíveis:")
        print(tools)
        
        # Exemplo de navegação
        print("\nNavegando para google.com...")
        await mcp.navigate("https://www.google.com")
        
        # Captura snapshot da página
        print("\nCapturando snapshot da página...")
        snapshot = await mcp.take_snapshot()
        
        print(f"Snapshot capturado: {snapshot}")
        
        # Captura screenshot da página
        print("\nCapturando screenshot da página...")
        screenshot = await mcp.take_screenshot()
        print(f"Screenshot capturado: {screenshot}")
        
        # Salva o screenshot em um arquivo
        import base64
        with open("screenshot.jpg", "wb") as f:
            f.write(base64.b64decode(screenshot[0].data))
        
if __name__ == "__main__":
    asyncio.run(example_usage())
