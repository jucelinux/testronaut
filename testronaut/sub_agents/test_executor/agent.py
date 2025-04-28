"""
Testronaut Agent - Main Implementation
"""
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from testronaut.shared_libraries import constants
from testronaut.tools.playwright_mcp import get_playwright_mcp_toolset
from testronaut.tools.test_planner import get_test_plan

from . import prompt

async def get_test_executor_agent():
    tools, exit_stack = await get_playwright_mcp_toolset()
    test_executor_agent = Agent(
        model= LiteLlm(
            model=constants.MODEL
        ),
        name="testronaut_test_executor",
        description="A helpful assistant for test execution.",
        instruction=prompt.TEST_EXECUTOR_PROMPT,
        output_key="STATE_TEST_EXECUTOR",
        tools=[get_test_plan, *tools]
    )
    return test_executor_agent, exit_stack

test_executor_agent_in_loop = get_test_executor_agent()


