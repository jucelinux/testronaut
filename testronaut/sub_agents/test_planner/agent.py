"""
Testronaut Agent - Main Implementation
"""
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from testronaut.shared_libraries import constants

from . import prompt
from testronaut.tools.test_planner import create_test_plan


test_planner_agent = Agent(
        model= LiteLlm(
            model=constants.MODEL
        ),
        name="testronaut_test_planner",
        description="A helpful assistant for test planning.",
        instruction=prompt.TEST_PLANNER_PROMPT,
        tools=[create_test_plan],
    )


