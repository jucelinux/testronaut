"""
Testronaut Agent - Main Implementation
"""
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from testronaut.shared_libraries import constants

from . import prompt

test_executor_agent_in_loop = Agent(
        model= LiteLlm(
            model=constants.MODEL
        ),
        name="testronaut_test_executor",
        description="A helpful assistant for test execution.",
        instruction=prompt.TEST_EXECUTOR_PROMPT,
        output_key="STATE_TEST_EXECUTOR"
    )


