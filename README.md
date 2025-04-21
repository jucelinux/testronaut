# Testronaut 🚀

> Autonomous testing powered by LLMs

Testronaut is an intelligent testing platform that understands natural language commands and executes them as precise browser interactions. Think of it as your AI testing companion that can navigate web applications like a real user.

## Features

- 🧠 Natural language test commands
- 🌐 Reliable browser automation
- 🤖 Local LLM-powered decision making
- 📊 Detailed execution logging
- ⚡ Async-first architecture

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) with dolphin3 model
- [Playwright](https://playwright.dev) MCP server

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/testronaut.git
cd testronaut
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the MCP server:
```bash
playwright run-server
```

4. Start Ollama (if not running):
```bash
ollama run dolphin3
```

## Quick Start

1. Create a test script:

```python
from testronaut import TestonautAgent

async def main():
    agent = TestonautAgent()
    await agent.start()
    
    try:
        # Navigate and interact
        await agent.navigate("https://example.com")
        content = await agent.get_page_content()
        print(content)
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

2. Run your script:
```bash
python your_script.py
```

## Configuration

Configuration is managed through `config.py` using Pydantic models. You can override settings via environment variables:

```bash
export MCP_URL="http://localhost:8931/sse"
export OLLAMA_MODEL="dolphin3"
```

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
