import dspy
from typing import Literal
import os


openai_key = os.getenv('OPENAI_API_KEY')

lm = dspy.LM('openai/gpt-4o-mini', api_key=openai_key)
dspy.configure(lm=lm)

class ClassifyCode(dspy.Signature):
    """Classify a given code snippet into a programming language."""

    code_snippet: str = dspy.InputField()
    language: Literal['Python', "JavaScript", "Java", "C++", "C#", "Go", "Rust", "Other"] = dspy.OutputField()
    confidence: float = dspy.OutputField()

# Create the classification model
classify_code = dspy.Predict(ClassifyCode)

# Example code snippets for classification
code_samples = [
    "def add(a, b):\n    return a + b",  
    "function add(a, b) { return a + b; }",  
    "public int add(int a, int b) { return a + b; }", 
    "int add(int a, int b) { return a + b; }",
]
print("--------With Claude-3-opus-20240229--------\n")
# Run classification on each code snippet
for code in code_samples: 
    response = classify_code(code_snippet= code)
    print(f"Code:\n{code}\nPredicted Language: {response.language} (Confidence: {response.confidence:.2f})\n")




# OUTPUT : 

# Code:
# def add(a, b):
#     return a + b
# Predicted Language: Python (Confidence: 0.95)

# Code:
# function add(a, b) { return a + b; }
# Predicted Language: JavaScript (Confidence: 0.95)

# Code:
# public int add(int a, int b) { return a + b; }
# Predicted Language: Java (Confidence: 0.95)

# Code:
# int add(int a, int b) { return a + b; }
# Predicted Language: C++ (Confidence: 0.95)


### -----------------Anthropic------------------- ###
claude_key = os.getenv('ANTHROPIC_API_KEY')
lm_anthropic = dspy.LM('anthropic/claude-3-opus-20240229', api_key=claude_key)
dspy.configure(lm=lm_anthropic)

classify_code = dspy.Predict(ClassifyCode)
for code in code_samples: 
    response = classify_code(code_snippet= code)
    print(f"Code:\n{code}\nPredicted Language: {response.language} (Confidence: {response.confidence:.2f})\n")



# --------With Claude-3-opus-20240229--------

# Code:
# def add(a, b):
#     return a + b
# Predicted Language: Python (Confidence: 0.95)

# Code:
# function add(a, b) { return a + b; }
# Predicted Language: JavaScript (Confidence: 0.95)

# Code:
# public int add(int a, int b) { return a + b; }
# Predicted Language: Java (Confidence: 0.95)

# Code:
# int add(int a, int b) { return a + b; }
# Predicted Language: C++ (Confidence: 0.95)

# Code:
# def add(a, b):
#     return a + b
# Predicted Language: Python (Confidence: 0.95)

# Code:
# function add(a, b) { return a + b; }
# Predicted Language: JavaScript (Confidence: 0.95)

# Code:
# public int add(int a, int b) { return a + b; }
# Predicted Language: Java (Confidence: 0.95)

# Code:
# int add(int a, int b) { return a + b; }
# Predicted Language: C++ (Confidence: 0.95)