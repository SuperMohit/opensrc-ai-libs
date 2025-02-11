import dspy
import os

lm = dspy.LM('openai/gpt-4o-mini', api_key="OPENAI_API_KEY")
dspy.configure(lm=lm)

class ExtractInfo(dspy.Signature):
    """Extract structured information from text."""

    text: str = dspy.InputField()
    title: str = dspy.OutputField()
    headings: list[str] = dspy.OutputField()
    entities: list[dict[str, str]] = dspy.OutputField(desc="a list of entities and their metadata")

module = dspy.Predict(ExtractInfo)

text = "Apple Inc. announced its latest iPhone 16 today." \
    "The CEO, Tim Cook, highlighted its new features in a press release."
response = module(text=text)

print(response.title)
print(response.headings)
print(response.entities)


###------Rerun with Anthropic----------------------------

claude_key = os.getenv('ANTHROPIC_API_KEY')
lm_anthropic = dspy.LM('anthropic/claude-3-opus-20240229', api_key=claude_key)
dspy.configure(lm=lm_anthropic)

module = dspy.Predict(ExtractInfo)
response = module(text=text)
print("-----------output with Anthropic-----------------")
print(response.title)
print(response.headings)
print(response.entities)

# OUTPUT : 

# Apple Inc. Announces iPhone 16
# ['Announcement', 'CEO Statement', 'New Features']
# [{'name': 'Apple Inc.', 'type': 'Organization'}, {'name': 'iPhone 16', 'type': 'Product'}, {'name': 'Tim Cook', 'type': 'Person'}]



# Apple Announces iPhone 16 with New Features
# ['Apple Inc. Announcement', 'iPhone 16 Release', 'New Features Highlighted', 'Tim Cook Press Release']
# [{'name': 'Apple Inc.', 'type': 'company'}, {'name': 'iPhone 16', 'type': 'product'}, {'name': 'Tim Cook', 'type': 'person', 'role': 'CEO'}]