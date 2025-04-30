import dspy


class ConsistencyAnalysisSignature(dspy.Signature):
    """Analyze multiple solutions for inconsistencies and errors."""
    query = dspy.InputField(desc="The original problem to solve")
    solutions = dspy.InputField(desc="Multiple solutions to the same problem")
    inconsistencies = dspy.OutputField(desc="List of inconsistencies found across solutions")
    errors = dspy.OutputField(desc="List of potential errors found in solutions")
    corrections = dspy.OutputField(desc="Proposed corrections for identified errors")