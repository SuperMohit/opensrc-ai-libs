<p align="center">
    <h1 align="center">DSPy</h1> 
</p>

DSPy is the framework for `programming—rather than prompting—language models`. 


## Getting Started

```
pip install -U dspy
```

You can authenticate by setting the `OPEN_API_KEY` env variable or passing `api_key` below.

```python
import dspy
lm = dspy.LM('openai/gpt-4o-mini', api_key='YOUR_OPENAI_API_KEY')
dspy.configure(lm=lm)
```

## Modules

DSPy provides different reasoning strategies for using large language models (LLMs) effectively in different scenarios.

### dspy.ChainOfThought

- `ChainOfThought (COT)` is a prompting strategy that enables step-by-step reasoning for solving complex problems.

- It is useful when a direct answer is not sufficient and a structured reasoning process is necessary.

```python
def search_wikipedia(query: str) -> list[str]:
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)
    return [x['text'] for x in results]

rag = dspy.ChainOfThought('context, question -> response')

question = "What's the name of the castle that David Gregory inherited?"
rag(context=search_wikipedia(question), question=question)
```

`When to use:`

- Best suited for multi-step reasoning problems like logical puzzles, mathematical derivations, and complex Q&A tasks that require justifications.

- Often used in Retrieval-Augmented Generation (RAG), where the model first retrieves relevant documents and then processes the context to generate an answer.

### dspy.Predict

- `Predict` is a generic model wrapper that directly predicts outputs based on input fields.

- It does not require intermediate reasoning steps like `ChainOfThought`; it simply learns from training data and gives the best output based on past knowledge.

- Best suited for classification, regression, and simple text generation tasks where no intermediate reasoning is needed.

- Commonly used for text classification, sentiment analysis, entity recognition, and structured output generation.

```python
from typing import Literal

class Classify(dspy.Signature):
    """Classify sentiment of a given sentence."""

    sentence: str = dspy.InputField()
    sentiment: Literal['positive', 'negative', 'neutral'] = dspy.OutputField()
    confidence: float = dspy.OutputField()

classify = dspy.Predict(Classify)
classify(sentence="This book was super fun to read, though not the last chapter.")
```

`When to use:`

- When no external context retrieval is required (i.e., self-contained tasks).

- When immediate predictions (e.g., labels or scores) are needed.

### dspy.ReAct

`ReAct` (Reasoning + Acting) is a framework that enables LLMs to reason and interact with external tools to refine their responses.

- It is particularly powerful when an AI model needs to:
  1. Think (Reasoning) - Analyze the problem and decide on the next step.
  2. Act (Calling external functions) - Retrieve or calculate information using external tools (e.g., search engines, calculators, APIs).

```python
def evaluate_math(expression: str):
    return dspy.PythonInterpreter({}).execute(expression)

def search_wikipedia(query: str):
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)
    return [x['text'] for x in results]

react = dspy.ReAct("question -> answer: float", tools=[evaluate_math, search_wikipedia])

pred = react(question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?")
print(pred.answer)
```

`When to use:`

- When multiple sources of knowledge and computation are needed.

- When external API calls, database queries, or complex calculations are required before answering.

### Conclusion

- Use `ChainOfThought` when you need `structured reasoning` to break down a problem before answering.
- Use `Predict` when you need a `quick classification or text generation` without reasoning.
- Use `ReAct` when you need `tool-assisted reasoning`, such as retrieving information or performing calculations before answering.
