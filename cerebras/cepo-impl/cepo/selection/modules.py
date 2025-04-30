import dspy
from typing import List

from cepo.selection.signatures import SolutionSelectionSignature
from cepo.models import Solution, Analysis, Selection


class ResponseSelector(dspy.Module):
    """Selects the best solution from multiple candidates."""
    
    def __init__(self):
        super().__init__()
        self.selector = dspy.Predict(SolutionSelectionSignature)
    
    def forward(self, query: str, solutions: List[Solution], analysis: Analysis) -> Selection:
        """
        Select the best solution with confidence score.
        
        Args:
            query (str): The original problem
            solutions (List[Solution]): Multiple solutions to choose from
            analysis (Analysis): Analysis of inconsistencies and errors
            
        Returns:
            Selection: The selected best solution with confidence
        """
        solutions_text = "\n\n".join([
            f"Solution {i+1}:\n{solution.content}"
            for i, solution in enumerate(solutions)
        ])
        
        analysis_text = f"""
        Inconsistencies:
        {chr(10).join([f"- {inc}" for inc in analysis.inconsistencies])}
        
        Errors:
        {chr(10).join([f"- {err}" for err in analysis.errors])}
        
        Corrections:
        {chr(10).join([f"- {cor}" for cor in analysis.corrections])}
        """
        
        result = self.selector(
            query=query,
            solutions=solutions_text,
            analysis=analysis_text
        )
        
        confidence = float(result.confidence)
        index = int(result.best_solution_index) - 1
        selected_solution = solutions[index]
        
        return Selection(
            solution=selected_solution,
            confidence=confidence,
            explanation=result.explanation
        )
