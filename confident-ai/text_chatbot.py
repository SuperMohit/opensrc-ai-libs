import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


def test_case():
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        # Replace this with the actual output from your LLM application
        actual_output="We offer a 30-day full refund at no extra costs.",
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra costs."]
    )
    assert_test(test_case, [answer_relevancy_metric])




# OUTPUT 

# Evaluating 1 test case(s) in parallel: |████████████████████|100% (1/1) [Time Taken: 00:06,  6.88s/test case]
# .Running teardown with pytest sessionfinish...

# =========================================== slowest 10 durations ============================================
# 8.56s call     test_chatbot.py::test_case

# (2 durations < 0.005s hidden.  Use -vv to show these durations.)
# 1 passed, 4 warnings in 8.59s
#                                                  Test Results                                                 
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Test case                  ┃ Metric           ┃ Score                      ┃ Status ┃ Overall Success Rate ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
# │ test_case                  │                  │                            │        │ 100.0%               │
# │                            │ Answer Relevancy │ 1.0 (threshold=0.5,        │ PASSED │                      │
# │                            │                  │ evaluation model=gpt-4o,   │        │                      │
# │                            │                  │ reason=The score is 1.00   │        │                      │
# │                            │                  │ because the response       │        │                      │
# │                            │                  │ directly addresses the     │        │                      │
# │                            │                  │ concern about the shoe     │        │                      │
# │                            │                  │ fit, and there are no      │        │                      │
# │                            │                  │ irrelevant statements in   │        │                      │
# │                            │                  │ the output. Great job      │        │                      │
# │                            │                  │ staying focused and on     │        │                      │
# │                            │                  │ point!, error=None)        │        │                      │
# │ Note: Use Confident AI     │                  │                            │        │                      │
# │ with DeepEval to analyze   │                  │                            │        │                      │
# │ failed test cases for more │                  │                            │        │                      │
# │ details                    │                  │                            │        │                      │
# └────────────────────────────┴──────────────────┴────────────────────────────┴────────┴──────────────────────┘
