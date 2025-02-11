import pytest
import deepeval
from deepeval import assert_test
from deepeval.dataset import EvaluationDataset
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval

# To run this file: deepeval test run <file_name>.py

test_cases = [
    LLMTestCase(
        input="What if these shoes don't fit?",
        # Replace this with the actual output of your LLM application
        actual_output="We offer a 30-day full refund at no extra cost.",
        expected_output="You're eligible for a free full refund within 30 days of purchase.",
    )
]

dataset = EvaluationDataset(test_cases=test_cases)

@pytest.mark.parametrize(
    "test_case",
    dataset,
)
def test_everything(test_case: LLMTestCase):
   
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.7)

    # here we have created a custom metric. Giving a name of the metric, the evaluation criteria, and the parameters to evaluate.
    correctness_metric = GEval(
        name="Correctness",
        criteria="Correctness - determine if the actual output is correct according to the expected output.",
        evaluation_params=[
            LLMTestCaseParams.ACTUAL_OUTPUT,
            LLMTestCaseParams.EXPECTED_OUTPUT,
        ],
        # strict=True,
    )
    assert_test(test_case, [answer_relevancy_metric, correctness_metric])


@deepeval.log_hyperparameters(model="gpt-4", prompt_template="...")
def hyperparameters():
    return {"temperature": 1, "chunk size": 500}



# OUTPUT 

# Evaluating 1 test case(s) in parallel: |█████████████████████████|100% (1/1) [Time Taken: 00:14, 14.20s/test case]
# .Running teardown with pytest sessionfinish...

# ============================================== slowest 10 durations ==============================================
# 17.44s call     test_example.py::test_everything[test_case0]

# (2 durations < 0.005s hidden.  Use -vv to show these durations.)
# 1 passed, 4 warnings in 17.50s
#                                                    Test Results                                                    
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Test case                   ┃ Metric              ┃ Score                       ┃ Status ┃ Overall Success Rate ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
# │ test_everything             │                     │                             │        │ 100.0%               │
# │                             │ Answer Relevancy    │ 1.0 (threshold=0.7,         │ PASSED │                      │
# │                             │                     │ evaluation model=gpt-4o,    │        │                      │
# │                             │                     │ reason=The score is 1.00    │        │                      │
# │                             │                     │ because the actual output   │        │                      │
# │                             │                     │ perfectly addresses the     │        │                      │
# │                             │                     │ concern regarding shoe      │        │                      │
# │                             │                     │ fitment without any         │        │                      │
# │                             │                     │ irrelevant information.     │        │                      │
# │                             │                     │ Great job in maintaining    │        │                      │
# │                             │                     │ focus and providing useful  │        │                      │
# │                             │                     │ answers!, error=None)       │        │                      │
# │                             │ Correctness (GEval) │ 0.78 (threshold=0.5,        │ PASSED │                      │
# │                             │                     │ evaluation model=gpt-4o,    │        │                      │
# │                             │                     │ reason=Both outputs convey  │        │                      │
# │                             │                     │ a full refund within 30     │        │                      │
# │                             │                     │ days, but wording differs;  │        │                      │
# │                             │                     │ actual output lacks         │        │                      │
# │                             │                     │ 'eligible' and the '30      │        │                      │
# │                             │                     │ days' condition linked to   │        │                      │
# │                             │                     │ 'purchase'., error=None)    │        │                      │
# │ Note: Use Confident AI with │                     │                             │        │                      │
# │ DeepEval to analyze failed  │                     │                             │        │                      │
# │ test cases for more details │                     │                             │        │                      │
# └─────────────────────────────┴─────────────────────┴─────────────────────────────┴────────┴──────────────────────┘
