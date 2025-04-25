from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.loop_agent import LoopAgent
from testronaut.shared_libraries import constants
from testronaut.sub_agents.test_planner.agent import test_planner_agent
from testronaut.sub_agents.test_controller.agent import test_controller_agent_in_loop
from testronaut.sub_agents.test_executor.agent import test_executor_agent_in_loop
from testronaut.sub_agents.test_finisher.agent import test_finisher_agent

test_loop = LoopAgent(
    name="TestLoopController",
    sub_agents=[test_controller_agent_in_loop, test_executor_agent_in_loop, test_finisher_agent],
    max_iterations=50,
)

root_agent = SequentialAgent(
    name="TestronautEntrypointAgent",
    sub_agents=[test_planner_agent, test_loop],
)
