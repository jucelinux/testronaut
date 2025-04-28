from pydantic import BaseModel, Field
from typing import Optional, Union

from google.genai import types

json_response_config = types.GenerateContentConfig(
    response_mime_type="application/json"
)

class TestStep(BaseModel):
    """A single test step."""
    step: int = Field(description="The step number of the test.")
    action: str = Field(description="The action to be performed in the test.")
    expected_result: str = Field(description="The expected result of the action.")

class TestPlan(BaseModel):
    """A test plan."""
    name: str = Field(description="The name of the test.")
    description: str = Field(description="The description of the test.")
    steps: list[TestStep] = Field(description="The steps of the test.")