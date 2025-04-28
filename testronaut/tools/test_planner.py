from dataclasses import dataclass
from typing import Optional, List
from loguru import logger
from google.adk.tools import ToolContext


@dataclass
class TestStep:
    """A single test step."""
    step: int
    action: str
    expected_result: str
    target: Optional[str] = None
    input: Optional[str] = None 

@dataclass
class TestPlan:
    """A test plan."""
    name: str
    description: str
    steps: List[TestStep]
    
def create_test_plan(test_plan: dict, tool_context: ToolContext) -> dict:
  """
  Create a test plan from a test description.
  
  Args:
    test_plan: A dictionary containing a test plan.
    tool_context: ToolContext object.
  Returns:
    dict: A dictionary containing the status of creation of the test plan.
    
  """
  test_plan = TestPlan(**test_plan)
  tool_context.state["test_plan"] = test_plan
  logger.info(f"Test plan created: {tool_context.state.get('test_plan')}")
  return {"status": "completed"}

def get_test_plan(tool_context: ToolContext) -> dict:
  """
  Get the test plan from the session state.
  """
  test_plan = tool_context.state.get("test_plan")
  return test_plan

def get_current_test_step(tool_context: ToolContext) -> dict:
  """
  Get the test step from the session state.
  
  Returns:
    The test step json or {"status": "completed"} if all steps are completed.
  """
  
  test_plan = tool_context.state.get("test_plan")
  
  if len(test_plan.steps) == 0:
    return {"status": "finished_all_test_steps"}
  
  current_test_step = test_plan.steps.pop(0)
  logger.info(f"Current test step: {current_test_step}")

  tool_context.state["current_test_step"] = current_test_step
  tool_context.state["test_plan"] = test_plan

  return current_test_step

def has_finished_all_test_steps(tool_context: ToolContext) -> str:
  """Call this function ONLY when all test steps are completed."""
  
  test_plan = tool_context.state.get("test_plan")
  
  if len(test_plan.steps) == 0:
    print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
    return {"status": "finished_all_test_steps"}
  
  return {"status": "test_steps_not_completed"}

def finish_test(tool_context: ToolContext) -> str:
  """Call this function ONLY when all test steps are completed."""
  tool_context.actions.escalate = True
  return "ALL_TEST_STEPS_COMPLETED"
  
  
  


  