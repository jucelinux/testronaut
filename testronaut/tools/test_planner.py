from dataclasses import dataclass
from typing import Optional, List
from loguru import logger

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

def create_test_plan(test_description: dict):
  """
  Create a list of test steps from a test description and save into session state.
  
  Args:
    test_description: A dictionary containing the test description.
    
  Returns:
    None
  """
  test_plan = TestPlan(
    name=test_description['test_name'],
    description=test_description['description'],
    steps=[
        TestStep(
            step=step['step'],
            action=step['action'],
            expected_result=step['expected_result'],
        )
        for step in test_description['steps']
    ]
  )
  logger.info(f"Test plan created: {test_plan}")
