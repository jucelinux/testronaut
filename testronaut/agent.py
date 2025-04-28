from google.adk.agents.sequential_agent import SequentialAgent
from testronaut.sub_agents.test_planner.agent import test_planner_agent
from testronaut.sub_agents.test_executor.agent import test_executor_agent_in_loop


async def get_root_agent():
    test_executor_agent, exit_stack = await test_executor_agent_in_loop
        
    sequential_agent = SequentialAgent(
        name="TestronautEntrypointAgent",
        sub_agents=[test_planner_agent, test_executor_agent],
    )
        
    return sequential_agent, exit_stack

root_agent = get_root_agent()


