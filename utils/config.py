from pydantic import BaseModel
from typing import Dict, Optional

class MCPConfig(BaseModel):
    url: str = "http://localhost:8931/sse"

class OllamaConfig(BaseModel):
    model: str = "dolphin3"

class Config(BaseModel):
    mcp: MCPConfig = MCPConfig()
    ollama: OllamaConfig = OllamaConfig()

# Default configuration
config = Config() 