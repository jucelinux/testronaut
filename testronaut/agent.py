from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from testronaut.shared_libraries import constants
from testronaut.sub_agents.test_planner.agent import test_planner_agent
from . import prompt

root_agent = Agent(
        model= LiteLlm(
            model=constants.MODEL
        ),
        name=constants.AGENT_NAME,
        description=constants.DESCRIPTION,
        instruction=prompt.ROOT_PROMPT,
        sub_agents=[test_planner_agent],
    )