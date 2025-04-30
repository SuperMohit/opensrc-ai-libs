import dspy
import random
from typing import List

from cepo.executor.signatures import PlanExecutionSignature
from cepo.models import Plan, Solution


class PlanExecutor(dspy.Module):
    """Executes a plan multiple times to produce diverse solutions."""
    
    def __init__(self):
        super().__init__()
        self.executor = dspy.Predict(PlanExecutionSignature)
    
    def forward(self, query: str, plan: Plan, n_executions: int = 3) -> List[Solution]:
        """
        Execute a plan multiple times to produce diverse solutions.
        
        Args:
            query (str): The original problem
            plan (Plan): The step-by-step plan to execute
            n_executions (int): Number of executions to perform
            
        Returns:
            List[Solution]: List of solutions from multiple executions
        """
        solutions = []
        
        for i in range(n_executions):
            plan_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(plan.steps)])
            result = self.executor(query=query, plan=plan_text)           
            solution = Solution(
                content=result.solution,
                metadata={"execution_number": i+1}
            )            
            solutions.append(solution)          
        return solutions
