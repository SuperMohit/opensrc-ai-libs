import dspy
lm = dspy.LM('openai/gpt-4o-mini', api_key="OPENAI_API_KEY")
dspy.configure(lm=lm)

# Function to execute python code snippets
def execute_code(code_snippet: str):
    return dspy.PythonInterpreter({}).execute(code_snippet)

# Function to search Wikipedia for programming-related topics
def search_programming_wikipedia(query: str):
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)
    return [x['text'] for x in results]

# Define a ReAct model that handles code execution and Wikipedia search
code_react = dspy.ReAct(
    "code_snippet -> output: str",
    tools=[execute_code, search_programming_wikipedia]
)

code_samples = [
    "sum([x for x in range(1, 101)])",  # Python: Sum of numbers 1 to 100
    "sort([5, 3, 8, 1, 2])",  # Python: Sorting a list
    "def factorial(n): return 1 if n == 0 else n * factorial(n-1); print(factorial(5))",  # Python: Factorial calculation
]

# Run execution for each code snippet
for idx, code in enumerate(code_samples, 1):
    pred = code_react(code_snippet=code)
    print(f"Code Snippet {idx}:\n{code}\nOutput: {pred.output}\n")




# OUTPUT : 

# Code Snippet 1:
# sum([x for x in range(1, 101)])
# Output: 5050

# Code Snippet 2:
# sort([5, 3, 8, 1, 2])
# Output: [1, 2, 3, 5, 8]

# Code Snippet 3:
# def factorial(n): return 1 if n == 0 else n * factorial(n-1); print(factorial(5))
# Output: 120