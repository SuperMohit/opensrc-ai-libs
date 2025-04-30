import dspy


class SolutionSelectionSignature(dspy.Signature):
    """Select the best solution with confidence score."""
    
    query = dspy.InputField(desc="The original problem to solve")
    solutions = dspy.InputField(desc="Multiple solutions to choose from")
    analysis = dspy.InputField(desc="Analysis of inconsistencies and errors")
    best_solution_index = dspy.OutputField(desc="Index of the best solution (1-based)")
    confidence = dspy.OutputField(desc="Confidence score (0-10)")
    explanation = dspy.OutputField(desc="Explanation for the selection")