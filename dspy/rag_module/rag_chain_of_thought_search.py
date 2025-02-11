import dspy
lm = dspy.LM('openai/gpt-4o-mini', api_key="OPENAI_API_KEY")
dspy.configure(lm=lm)

def search_wikipedia(query: str) -> list[str]:
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)      # The url is a custom endpoint for a Wikipedia dataset
    return [x['text'] for x in results]

rag = dspy.ChainOfThought('context, question -> response')

question = "Which team was the winner of the first men's cricket world cup tournament ?"
response = rag(context=search_wikipedia(question), question=question)

print(response)


# OUTPUT : 

# Prediction(
#     reasoning="The first men's Cricket World Cup was held in 1975, and it was won by the West Indies, who defeated Australia in the final. This information is derived from the context provided about the 1975 English cricket season.",
#     response="The winner of the first men's cricket world cup tournament was the West Indies."      
