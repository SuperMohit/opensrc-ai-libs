import dspy
from .signatures import PlanGenerationSignature
from cepo.models import Plan


class PlanGenerator(dspy.Module):
    """Generates a structured step-by-step plan to solve a problem using an LLM."""
        
    def __init__(self):
        super().__init__()
        self.planner = dspy.Predict(PlanGenerationSignature)
    
    def forward(self, query):
        """
        Generate a step-by-step plan from a query.
        
        Args:
            query (str): The problem to solve
            
        Returns:
            Plan: A structured plan with steps
        """
        result = self.planner(query=query)
        
        # Parse the plan into individual steps
        steps = []
        for line in result.plan.strip().split('\n'):
            line = line.strip()
            if line:
                # Remove numbering if present
                if line[0].isdigit() and '. ' in line[:4]:
                    line = line[line.index('. ')+2:]
                steps.append(line)
        
        return Plan(steps=steps)