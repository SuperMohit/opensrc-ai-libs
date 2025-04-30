# CePO Quick Start Guide

This guide will help you get started with the CePO framework quickly.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cepo.git
   cd cepo
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

## Running CePO from the Command Line

The simplest way to use CePO is through the command-line interface:

```bash
# Run with a direct query
python main.py "Calculate the compound interest on $10,000 at 5% annual interest for 10 years, compounded quarterly."

# Run with a query from a file
python main.py -f problems/example.txt

# Run with custom parameters
python main.py -m gpt-4 -e 5 -t 0.8 -v "What is the most efficient algorithm for sorting a list of integers?"

# Save results to a file
python main.py -o results.txt "Find the maximum value of f(x) = -x² + 4x + 7."
```

### Command-Line Options

- `-f, --file`: Path to a file containing the problem
- `-m, --model`: OpenAI model to use (default: gpt-4)
- `-e, --executions`: Number of executions (default: 3)
- `-t, --temperature`: Temperature setting (default: 0.7)
- `-v, --verbose`: Enable verbose output with full analysis
- `-o, --output`: Save results to this file

## Using CePO in Your Code

Here's how to integrate CePO into your Python application:

```python
from cepo import CePOPipeline

# Initialize the pipeline
pipeline = CePOPipeline(
    openai_api_key="your_api_key",  # Or use os.environ.get("OPENAI_API_KEY")
    openai_model="gpt-4",           # Model to use
    temperature=0.7,                # Creativity level
    n_executions=3                  # Number of plan executions
)

# Run the pipeline
result = pipeline.run("Your problem statement here")

# Access components of the result
plan = result.plan
solutions = result.solutions
analysis = result.analysis
best_solution = result.selection.solution
confidence = result.selection.confidence

# Print the best solution
print(f"Best solution (confidence: {confidence}/10):")
print(best_solution.content)
```

## Example Problems

CePO works well with:

1. **Mathematical problems**:
   ```
   Calculate the area of a circle with radius 5 cm.
   ```

2. **Logical puzzles**:
   ```
   You have two hourglasses, one measures 7 minutes and one measures 4 minutes.
   How can you measure exactly 9 minutes?
   ```

3. **Step-by-step procedures**:
   ```
   What are the steps to convert a decimal number to binary?
   ```

4. **Analytical problems**:
   ```
   A box contains 10 red marbles, 20 blue marbles, and 15 green marbles.
   If you draw 3 marbles at random, what is the probability they are all the same color?
   ```

## Tips for Best Results

1. **Be specific**: Clearly state the problem and any constraints
2. **Request reasoning**: Add "Solve this step-by-step" to encourage detailed solutions
3. **Increase executions**: Use more executions (5-7) for complex problems
4. **Adjust temperature**: Use lower temperatures (0.3-0.5) for math problems
5. **Choose models**: GPT-4 generally provides better results than GPT-3.5

## Troubleshooting

- **API errors**: Check your API key and network connection
- **Low confidence**: Try increasing the number of executions
- **Inconsistent results**: Lower the temperature for more consistency
- **Long processing times**: Reduce the number of executions or use a faster model

For more details, see the full documentation in the README.md file.