<p align="center">
    <h1 align="center">DEEPEVAL</h1> 
</p>

**DeepEval** is a simple-to-use, open-source LLM evaluation framework, for evaluating and testing large-language model systems.

## Installation

```
pip install -U deepeval
```

## Create an account

Deepeval runs evaluations locally on your environment. To keep your testing reports in a centralized place on the cloud, use Confident AI, the leading evaluation plaform for DeepEval.

To login, run:

```
deepeval login
```

## Custom Metrics

**Deepeval** provides G-Eval, a state-of-the-art LLM evaluation framework for anyone to create a custom LLM-evaluated metric using natural language. Here's an example:


## G-Eval

G-Eval is a framework that uses LLMs with chain-of-thoughts (CoT) to evaluate LLM outputs based on ANY custom criteria.

To create a custom metric that uses LLMs for evaluation, simply instantiate an **GEval** class an define an evaluation criteria in everyday language:

```python
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams

correctness_metric = GEval(
    name="Correctness",
    criteria="Determine whether the actual output is factually correct based on the expected output.",
    # NOTE: you can only provide either criteria or evaluation_steps, and not both
    evaluation_steps=[
        "Check whether the facts in 'actual output' contradicts any facts in 'expected output'",
        "You should also heavily penalize omission of detail",
        "Vague language, or contradicting OPINIONS, are OK"
    ],
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
)
```

G-Eval is a two-step algorithm that first generates a series of **evaluation_steps** using chain of thoughts (CoTs) based on the given **criteria**, before using the generated steps to determine the final score using the parameters presented in an **LLMTestCase**.

When you provide **evaluation_steps**, the **GEval** metric skips the first step and uses the provided steps to determine the final score instead.

## Answer Relevancy Metric

The answer relevancy metric measures the quality of your RAG pipeline's generator by evaluating how relevant the `actual_output` of your LLM application is compared to the provided `input`. `deepeval's` answer relevancy metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score.

To use the `AnswerRelevancyMetric`, you'll have to provide the following arguments when creating an `LLMTestCase`:

- **input**
- **actual_output**

```python
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# Replace this with the actual output from your LLM application
actual_output = "We offer a 30-day full refund at no extra cost."

metric = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4",
    include_reason=True
)
test_case = LLMTestCase(
    input="What if these shoes don't fit?",
    actual_output=actual_output
)

metric.measure(test_case)
print(metric.score)
print(metric.reason)

# or evaluate test cases in bulk
evaluate([test_case], [metric])
```

The `AnswerRelevancyMetric` first uses an LLM to extract all statements made in the `actual_output`, before using the same LLM to classify whether each statement is relevant to the `input`.

## Faithfulness Metric

The faithfulness metric measures the quality of your RAG pipeline's generator by evaluating whether the `actual_output` factually aligns with the contents of your `retrieval_context`. `deepeval's` faithfulness metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score.

To use the `FaithfulnessMetric`, you'll have to provide the following arguments when creating an `LLMTestCase`:

- **input**
- **actual_output**
- **retrieval_context**

```python
from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase

# Replace this with the actual output from your LLM application
actual_output = "We offer a 30-day full refund at no extra cost."

# Replace this with the actual retrieved context from your RAG pipeline
retrieval_context = ["All customers are eligible for a 30 day full refund at no extra cost."]

metric = FaithfulnessMetric(
    threshold=0.7,
    model="gpt-4",
    include_reason=True
)
test_case = LLMTestCase(
    input="What if these shoes don't fit?",
    actual_output=actual_output,
    retrieval_context=retrieval_context
)

metric.measure(test_case)
print(metric.score)
print(metric.reason)

# or evaluate test cases in bulk
evaluate([test_case], [metric])
```

The `FaithfulnessMetric` first uses an LLM to extract all claims made in the `actual_output`, before using the same LLM to classify whether each claim is truthful based on the facts presented in the `retrieval_context`.

A claim is considered truthful if it does not contradict any facts presented in the `retrieval_context`.
