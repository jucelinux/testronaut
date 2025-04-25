

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from testronaut.shared_libraries import constants
from testronaut.tools.test_planner import get_current_test_step
from . import prompt

test_controller_agent_in_loop = Agent(
        model= LiteLlm(
            model=constants.MODEL
        ),
        name="testronaut_test_controller",
        description="A helpful assistant for test controller.",
        instruction=prompt.TEST_CONTROLLER_PROMPT,
        tools=[get_current_test_step],
        output_key="STATE_TEST_CONTROLLER",
    )
