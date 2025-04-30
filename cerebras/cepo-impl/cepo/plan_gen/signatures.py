import dspy


class PlanGenerationSignature(dspy.Signature):
    """Generate a detailed step-by-step plan to solve a problem."""
    
    query = dspy.InputField(desc="The problem to solve")
    plan = dspy.OutputField(desc="A numbered list of detailed step-by-step instructions")