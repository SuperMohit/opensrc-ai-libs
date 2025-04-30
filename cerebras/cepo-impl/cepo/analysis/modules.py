import dspy
from typing import List

from cepo.analysis.signatures import ConsistencyAnalysisSignature
from cepo.models import Solution, Analysis


class ConsistencyAnalyzer(dspy.Module):
    """Analyzes multiple solutions for inconsistencies and errors."""

    def __init__(self):
        super().__init__()
        self.analyzer = dspy.Predict(ConsistencyAnalysisSignature)

    def forward(self, query: str, solutions: List[Solution]) -> Analysis:
        """
        Analyze solutions for inconsistencies and errors.
        
        Args:
            query (str): The original problem
            solutions (List[Solution]): Multiple solutions to analyze
            
        Returns:
            Analysis: Analysis of inconsistencies and errors
        """

        solutions_text = "\n\n".join([
            f"Solution {i+1}:\n{solution.content}"
            for i, solution in enumerate(solutions)
        ])
        
        result = self.analyzer(
            query=query,
            solutions=solutions_text
        )
        
        inconsistencies = [i.strip() for i in result.inconsistencies.strip().split('\n') if i.strip()]
        errors = [e.strip() for e in result.errors.strip().split('\n') if e.strip()]
        corrections = [c.strip() for c in result.corrections.strip().split('\n') if c.strip()]
        
        return Analysis(
            inconsistencies=inconsistencies,
            errors=errors,
            corrections=corrections
        )