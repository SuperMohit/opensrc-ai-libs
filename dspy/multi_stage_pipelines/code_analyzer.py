import dspy
from typing import List, Dict

lm = dspy.LM('openai/gpt-4o-mini', api_key="OPENAI_API_KEY")
dspy.configure(lm=lm)

class CodeAnalysis(dspy.Signature):
    """Analyze the structure and components of a code snippet."""
    
    code: str = dspy.InputField()
    title: str = dspy.OutputField()
    components: List[str] = dspy.OutputField()
    component_details: Dict[str, List[str]] = dspy.OutputField(desc="mapping from components to their details")

class AnalyzeComponent(dspy.Signature):
    """Analyze a specific component of the code."""
    
    code: str = dspy.InputField()
    component_name: str = dspy.InputField()
    component_details: List[str] = dspy.InputField()
    analysis: str = dspy.OutputField(desc="detailed analysis of the component")

class CodeAnalyzer(dspy.Module):
    def __init__(self):
        self.analyze_structure = dspy.ChainOfThought(CodeAnalysis)
        self.analyze_component = dspy.ChainOfThought(AnalyzeComponent)

    def forward(self, code):
        analysis = self.analyze_structure(code=code)
        components = []
        for component, details in analysis.component_details.items():
            component_header = f"## {component}"
            component_analysis = self.analyze_component(
                code=code,
                component_name=component,
                component_details=details
            )
            components.append(f"{component_header}\n{component_analysis.analysis}")
        return dspy.Prediction(title=analysis.title, components=components)

# Example usage
code_analyzer = CodeAnalyzer()

# Example code snippets
code_snippets = [
    """
    class DataProcessor:
        def __init__(self, data):
            self.data = data
            
        def process(self):
            return [x * 2 for x in self.data if x > 0]
            
        @property
        def data_length(self):
            return len(self.data)
    """,
    
]

# Analyze each code snippet
for i, code in enumerate(code_snippets, 1):
    print(f"\n{'='*50}")
    print(f"Code Snippet #{i}")
    print(f"{'='*50}")
    analysis = code_analyzer(code=code)
    print(f"\nTitle: {analysis.title}")
    print("\nAnalysis:")
    for component in analysis.components:
        print(f"\n{component}")



# OUTPUT : 

# ==================================================
# Code Snippet #1
# ==================================================

# Title: DataProcessor Class

# Analysis:

# ## DataProcessor
# The `DataProcessor` class encapsulates data processing logic in a straightforward manner. The constructor (`__init__`) initializes the instance with a data list, which is stored as an instance variable. The `process` method employs a list comprehension to iterate over the `data`, doubling each element that is greater than zero. This method is efficient and Pythonic, leveraging the power of list comprehensions for concise and readable code.

# The `data_length` property provides a simple interface to access the length of the data list. By using the `@property` decorator, it allows users to retrieve the length as if it were an attribute, enhancing usability and readability.

# Overall, the `DataProcessor` class is well-structured for its intended purpose, promoting clean code practices and encapsulation. However, it could be improved by adding error handling for cases where the input data is not a list or contains non-numeric values, which would make the class more robust in real-world applications.

# ## __init__
# The `__init__` method in the `DataProcessor` class takes a single parameter, `data`, which is expected to be a collection (like a list) of numerical values. The method assigns this parameter to the instance variable `self.data`. This allows other methods within the class, such as `process` and the `data_length` property, to access and manipulate the `data` attribute.

# The design of the constructor is straightforward and effective. It ensures that every instance of `DataProcessor` has its own `data` attribute, which can be processed later by the `process` method. The constructor does not perform any validation on the input data, which could be a potential area for improvement. For instance, it could check if the input is indeed a list or if it contains only numerical values. This would enhance the robustness of the class and prevent runtime errors during processing.

# Overall, the `__init__` method serves its purpose well by initializing the `data` attribute, but additional input validation could be beneficial for ensuring the integrity of the data being processed.

# ## process
# The `process` method utilizes a list comprehension to iterate over the `self.data` attribute. The condition `if x > 0` ensures that only positive integers are considered for processing. This is an efficient way to filter data, as list comprehensions are generally faster and more concise than traditional for-loops in Python. The multiplication by two indicates a transformation that could be useful in various contexts, such as scaling or preparing data for further analysis.

# One potential area for improvement could be the handling of non-numeric data types. Currently, if `self.data` contains any non-numeric values, the method will raise a `TypeError`. Implementing type checking or exception handling could enhance the robustness of this method. Additionally, the method could be extended to allow for different types of transformations or to accept parameters that dictate the transformation behavior, making it more flexible for various use cases.

# Overall, the `process` method is a straightforward and effective implementation for processing a list of numbers, but it could benefit from additional error handling and flexibility to accommodate a wider range of input scenarios.

# ## data_length
# The `data_length` property is a simple yet effective feature of the `DataProcessor` class. It encapsulates the logic for determining the length of the `data` attribute, which is a list. This property is accessed like an attribute, making it intuitive for users of the class.

# When the `data_length` property is accessed, it executes the `len(self.data)` function, which computes the number of elements in the `data` list. This is efficient, as it operates in O(1) time complexity, meaning it retrieves the length without needing to iterate through the list.

# Additionally, the use of a property here is beneficial because it allows for future enhancements. If the logic for determining the length of the data were to change (for example, if the data were to be filtered or transformed), the implementation could be modified within the property without affecting the external interface of the class.

# Overall, the `data_length` property contributes to the encapsulation and abstraction principles of object-oriented programming, making the `DataProcessor` class more user-friendly and maintainable.
