import dspy


class PlanExecutionSignature(dspy.Signature):
    """Execute a plan to produce a solution."""
        
    query = dspy.InputField(desc="The original problem to solve")
    plan = dspy.InputField(desc="Step-by-step plan to follow")
    solution = dspy.OutputField(desc="The solution produced by executing the plan")
