# dspy library: It is a python library for working with large language models (LLMs). The dspy library provides a simple and intuitive API for interacting with LLMs, making it earier to use them for various tasks.

import dspy
lm = dspy.LM('openai/gpt-4o-mini', api_key="OPENAI_API_KEY")
dspy.configure(lm=lm)

math = dspy.ChainOfThought("question -> answer: float")
response = math(question="Two dice are tossed. What is the probability that the sum equals two?")

print(response)


# OUTPUT : 

# Prediction(
#     reasoning='When two dice are tossed, each die has 6 faces, resulting in a total of 6 * 6 = 36 possible outcomes. The only way to achieve a sum of 2 is if both dice show a 1 (1,1). There is only 1 favorable outcome for this event. Therefore, the probability of the sum equaling 2 is the number of favorable outcomes divided by the total number of outcomes, which is 1/36.',
#     answer=0.027777777777777776
# )