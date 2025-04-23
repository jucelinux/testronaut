# Testronaut 🚀
<div align="center">
  <img src="./assets/testronaut.svg" alt="testronaut" width="400" />
</div>

> Autonomous testing powered by LLMs

Testronaut is an intelligent testing platform that understands natural language commands and executes them as precise browser interactions. Think of it as your AI testing companion that can navigate web applications like a real user, while maintaining detailed documentation of every step.

> 📜 Read our [Manifesto](MANIFESTO.md) to understand our vision, principles, and future roadmap.

## Features

- 🧠 Natural language test commands
- 🌐 Reliable browser automation with Playwright
- 📝 Automatic test documentation
- 📸 Automated screenshot capture
- 🔍 Step-by-step test tracking
- 📊 JSON test reports
- ⚡ Async-first architecture

## Core Components

Testronaut is built on these powerful technologies:

### Foundation
- [Google ADK](https://github.com/google/adk) - Agent Development Kit for building AI agents
- [LiteLLM](https://github.com/litellm/litellm) - Universal API for LLM providers
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - Model Context Protocol for browser automation

### Key Features
- **Test Documentation System**: Automatic tracking and documentation of test steps
- **Screenshot Integration**: Visual evidence capture at key test points
- **JSON Reports**: Structured test results with timestamps and metadata
- **Headless Support**: Full support for headless browser testing

## Prerequisites

- Python 3.12+
- Node.js (for Playwright MCP)
- OpenAI API key (or other supported LLM provider)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/testronaut.git
cd testronaut
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright MCP:
```bash
npm install -g @playwright/mcp
```

## Configuration

1. Set up your environment variables:
```bash
export OPENAI_API_KEY="your-api-key"
```

2. Optional: Configure test output directory in `.env`:
```bash
TEST_OUTPUT_DIR="./snapshots"
```

## Usage

1. Start the ADK web interface:
```bash
adk web
```

2. Open http://localhost:8000 in your browser

3. Select the "testronaut" agent from the dropdown menu

4. Start creating and running tests using natural language commands

## Example Test Commands

```plaintext
Navigate to https://example.com and verify the homepage loads
Fill the login form with test@example.com and password123
Click the submit button and check for error messages
Take a screenshot of the error state
```

## Project Structure

```
testronaut/
├── testronaut/
│   ├── __init__.py
│   ├── agent.py              # Main agent implementation
│   └── tools/
│       ├── __init__.py
│       ├── document_test_step.py   # Test documentation tools
│       └── playwright_mcp.py       # Browser automation setup
├── snapshots/                # Test reports and screenshots
├── assets/                  # Project assets
└── requirements.txt         # Python dependencies
```

## Test Documentation

Tests are automatically documented with:
- Step-by-step descriptions
- Expected vs actual results
- Timestamps for each action
- Screenshot captures
- JSON report generation

Example report structure:
```json
{
  "test_name": "Login Test",
  "total_steps": 3,
  "passed_steps": 2,
  "failed_steps": 1,
  "steps": [
    {
      "step_name": "Navigate to Login",
      "description": "Open the login page",
      "status": "passed",
      "timestamp": "2024-04-23T12:34:56"
    }
  ]
}
```

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
