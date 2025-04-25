"""
Testronaut Agent - Main Implementation
"""
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from testronaut.shared_libraries import constants
from testronaut.tools.test_planner import has_finished_all_test_steps, finish_test
from . import prompt

test_finisher_agent = Agent(
        model= LiteLlm(
            model=constants.MODEL
        ),
        name="testronaut_test_finisher",
        description="A helpful assistant for test execution.",
        instruction=prompt.TEST_EXECUTOR_PROMPT,
        tools=[has_finished_all_test_steps, finish_test],
        output_key="STATE_TEST_EXECUTOR"
    )


