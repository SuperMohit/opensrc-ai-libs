import dspy
from typing import Literal
import os

openai_key = os.getenv('OPENAI_API_KEY')

lm = dspy.LM('openai/gpt-4o-mini', api_key=openai_key)
dspy.configure(lm=lm)

class Classify(dspy.Signature):
    """Classify sentiment of a given sentence."""

    sentence: str = dspy.InputField()
    sentiment: Literal['positive', 'negative', 'neutral'] = dspy.OutputField()
    confidence: float = dspy.OutputField()

classify = dspy.Predict(Classify)
response = classify(sentence="This book was super fun to read, though not the last chapter.")

print(response)
# OUTPUT: 

# Prediction(
#     sentiment='positive',
#     confidence=0.85
# )

### -----------------Anthropic------------------- ###
claude_key = os.getenv('ANTHROPIC_API_KEY')
lm_anthropic = dspy.LM('anthropic/claude-3-opus-20240229', api_key=claude_key)
dspy.configure(lm=lm_anthropic)

classify = dspy.Predict(Classify)
response = classify(sentence="This book was super fun to read, though not the last chapter.")

print(response)

# Prediction(
#     sentiment='positive',
#     confidence=0.8
# )

