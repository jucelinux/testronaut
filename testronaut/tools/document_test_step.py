from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional
import json
from loguru import logger

@dataclass
class TestStep:
    """Represents a single test step with its metadata."""
    step_name: str
    description: str
    expected_result: str
    actual_result: Optional[str] = None
    status: str = "pending"
    timestamp: datetime = field(default_factory=datetime.now)
    artifacts: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

class DocumentTestStep:
    """Tool for documenting test steps during test execution."""
    
    def __init__(self, test_name: str):
        self.test_name = test_name
        self.steps: List[TestStep] = []
        self.current_step: Optional[TestStep] = None
        
    def get_test_report(self) -> Dict[str, Any]:
        """Generate a complete test report.
            Returns:
                A dictionary containing the test report.
        """
        return {
            "test_name": self.test_name,
            "total_steps": len(self.steps),
            "passed_steps": len([s for s in self.steps if s.status == "passed"]),
            "failed_steps": len([s for s in self.steps if s.status == "failed"]),
            "pending_steps": len([s for s in self.steps if s.status == "pending"]),
            "steps": [
                {
                    "step_name": step.step_name,
                    "description": step.description,
                    "expected_result": step.expected_result,
                    "actual_result": step.actual_result,
                    "status": step.status,
                    "timestamp": step.timestamp.isoformat(),
                    "artifacts": step.artifacts,
                    "metadata": step.metadata
                }
                for step in self.steps
            ]
        }
    
    def export_report(self, file_path: str):
        """Export the test report to a JSON file.
            Args:
                file_path: The path to the file where the report will be exported.
            Returns:
                None
        """
        report = self.get_test_report()
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            logger.info(f"Test report exported to {file_path}")

document_test_step = DocumentTestStep("Test")

def start_step(step_name: str, description: str, expected_result: str):
        """Start a new test step.
            Args:
                step_name: The name of the test step.
                description: The description of the test step.
                expected_result: The expected result of the test step. Accepted values are "passed" or "failed".
            Returns:
                None
        """
        
        step = TestStep(
            step_name=step_name,
            description=description,
            expected_result=expected_result
        )
        
        logger.info(f"step started: {step}")
        
        document_test_step.current_step = step
        document_test_step.steps.append(step)
    
def complete_step(actual_result: str, status: str):
    """Complete the current test step with results.
        Args:
            actual_result: The actual result of the test step.
            status: The status of the test step. Accepted values are "passed" or "failed".
        Returns:
            None
    """
    if not document_test_step.current_step:
        raise ValueError("No test step currently in progress")
    
    document_test_step.current_step.actual_result = actual_result
    document_test_step.current_step.status = status
    document_test_step.current_step.timestamp = datetime.now()
    logger.info(f"step completed: {document_test_step.current_step}")
        
def finalize_test():
    """Finalize the test.
        Returns:
            None
    """
    logger.info(f"finalizing test: {document_test_step.get_test_report()}")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    document_test_step.export_report(f"snapshots/test_report_{timestamp}.json")
