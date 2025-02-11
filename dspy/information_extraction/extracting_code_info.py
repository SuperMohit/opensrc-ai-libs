import dspy
from typing import List, Dict, Any
import os


class ExtractInfo(dspy.Signature):
    """Extract structured information from code snippets."""
    
    code_snippet: str = dspy.InputField(desc="Python code to analyze")
    title: str = dspy.OutputField(desc="Brief description of the code")
    structure: List[str] = dspy.OutputField(desc="Code structure elements")
    analysis: Dict[str, Any] = dspy.OutputField(desc="Code analysis details")

class CodeAnalyzer:
    def __init__(self, d: dspy):
        self.module = d.Predict(ExtractInfo)
        # self.interpreter = dspy.PythonInterpreter({})
    
    def analyze(self, code_snippet: str) -> None:
        # Analyze code structure
        analysis = self.module(code_snippet=code_snippet)
        
        print(f"\n{'='*50}")
        print("Code Analysis:")
        print(f"{'='*50}")
        print(f"Code:\n{code_snippet}")
        print(f"\nTitle: {analysis.title}")
        print(f"Structure: {analysis.structure}")
        print(f"Analysis: {analysis.analysis}")

# Example usage
if __name__ == "__main__":
    openai_key = os.getenv('OPENAI_API_KEY')
    # Initialize DSPy
    lm = dspy.LM('openai/gpt-4o-mini', api_key=openai_key)
    dspy.configure(lm=lm)
    analyzer = CodeAnalyzer(dspy)
    
    # Define code snippets
    code_snippets = [
        # List comprehension with filtering
        """
        numbers = range(1, 11)
        evens = [x for x in numbers if x % 2 == 0]
        evens
        """,
        
        # Class definition with methods
        """
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height
            
            def area(self):
                return self.width * self.height
        
        rect = Rectangle(5, 3)
        rect.area()
        """,
        
        # Dictionary manipulation
        """
        data = {'a': 1, 'b': 2}
        data.update({'c': 3})
        {k: v*2 for k, v in data.items()}
        """
    ]
    
    # Analyze and execute each snippet
    for snippet in code_snippets:
        analyzer.analyze(snippet)

    #---Anthropic---#
    claude_key = os.getenv('ANTHROPIC_API_KEY')
    lm_anthropic = dspy.LM('anthropic/claude-3-opus-20240229', api_key=claude_key)
    dspy.configure(lm=lm_anthropic)

    analyzer = CodeAnalyzer(dspy)

    print("---------Anthropic Analysis--------------")
    for snippet in code_snippets:
        analyzer.analyze(snippet) 


# OUTPUT : 

# ==================================================
# Code Analysis:
# ==================================================
# Code:

#         numbers = range(1, 11)
#         evens = [x for x in numbers if x % 2 == 0]
#         evens
        

# Title: List Comprehension to Filter Even Numbers
# Structure: ['variable_assignment', 'list_comprehension', 'conditional_expression']
# Analysis: {'variables': ['numbers', 'evens'], 'range': {'start': 1, 'end': 11}, 'filter_condition': 'x % 2 == 0', 'output': 'list of even numbers from 1 to 10'}

# ==================================================
# Code Analysis:
# ==================================================
# Code:

#         class Rectangle:
#             def __init__(self, width, height):
#                 self.width = width
#                 self.height = height

#             def area(self):
#                 return self.width * self.height

#         rect = Rectangle(5, 3)
#         rect.area()


# Title: Rectangle Class Implementation
# Structure: ['class definition', 'constructor (__init__)', 'instance variables', 'method (area)', 'object instantiation', 'method call']
# Analysis: {'class_name': 'Rectangle', 'methods': [{'name': '__init__', 'parameters': ['width', 'height'], 'description': 'Initializes the width and height of the rectangle.'}, {'name': 'area', 'parameters': [], 'description': 'Calculates and returns the area of the rectangle.'}], 'instance': {'width': 5, 'height': 3, 'area': 15}, 'usage': 'An instance of Rectangle is created with width 5 and height 3, and its area is calculated.'}

# ==================================================
# Code Analysis:
# ==================================================
# Code:

#         data = {'a': 1, 'b': 2}
#         data.update({'c': 3})
#         {k: v*2 for k, v in data.items()}


# Title: Dictionary Update and Comprehension
# Structure: ['dictionary', 'update method', 'dictionary comprehension', 'key-value pairs']
# Analysis: {'data_initial': {'a': 1, 'b': 2}, 'data_updated': {'a': 1, 'b': 2, 'c': 3}, 'comprehension_result': {'a': 2, 'b': 4, 'c': 6}, 'steps': ['Create a dictionary with initial values.', 'Update the dictionary with a new key-value pair.', 'Use dictionary comprehension to double the values.']}



# ---------Anthropic Analysis--------------

# ==================================================
# Code Analysis:
# ==================================================
# Code:

#         numbers = range(1, 11)
#         evens = [x for x in numbers if x % 2 == 0]
#         evens
        

# Title: Generate a list of even numbers from 1 to 10 using a list comprehension
# Structure: ['Create range object from 1 to 11', 'Use list comprehension to filter even numbers', 'Implicitly print the resulting list']
# Analysis: {'range_object': 'range(1, 11) generates numbers from 1 to 10', 'list_comprehension': '[x for x in numbers if x % 2 == 0] filters even numbers', 'modulo_operator': 'x % 2 == 0 checks if x is divisible by 2 (even)', 'implicit_print': 'evens at the end prints the list', 'result': [2, 4, 6, 8, 10]}

# ==================================================
# Code Analysis:
# ==================================================
# Code:

#         class Rectangle:
#             def __init__(self, width, height):
#                 self.width = width
#                 self.height = height
            
#             def area(self):
#                 return self.width * self.height
        
#         rect = Rectangle(5, 3)
#         rect.area()
        

# Title: Rectangle class with area calculation
# Structure: ['class definition', 'constructor', 'instance method', 'object instantiation', 'method invocation']
# Analysis: {'class_name': 'Rectangle', 'attributes': [{'name': 'width', 'type': 'numeric'}, {'name': 'height', 'type': 'numeric'}], 'methods': [{'name': '__init__', 'parameters': ['width', 'height'], 'purpose': 'constructor to initialize attributes'}, {'name': 'area', 'parameters': [], 'return_value': {'type': 'numeric', 'description': 'area of the rectangle'}, 'purpose': 'calculate the area of the rectangle'}], 'object_name': 'rect', 'object_creation': {'class': 'Rectangle', 'arguments': [5, 3]}, 'method_call': {'object': 'rect', 'method': 'area', 'arguments': []}}

# ==================================================
# Code Analysis:
# ==================================================
# Code:

#         data = {'a': 1, 'b': 2}
#         data.update({'c': 3})
#         {k: v*2 for k, v in data.items()}
        

# Title: Updating and transforming a dictionary
# Structure: ['Initialize dictionary', 'Update dictionary', 'Dictionary comprehension']
# Analysis: {'data_initialization': {'description': "Initializes a dictionary 'data' with key-value pairs 'a': 1 and 'b': 2", 'type': 'dict'}, 'data_update': {'description': "Updates the 'data' dictionary with a new key-value pair 'c': 3 using the update() method", 'type': 'dict.update'}, 'dict_comprehension': {'description': "Creates a new dictionary by doubling the values of the 'data' dictionary using a dictionary comprehension", 'type': 'dict comprehension', 'result': {'a': 2, 'b': 4, 'c': 6}}}