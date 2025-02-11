import dspy
from rich.console import Console
from rich.markdown import Markdown

console = Console()      # Initialize the console for rich printing.

lm = dspy.LM('openai/gpt-4o-mini', api_key="OPENAI_API_KEY")
dspy.configure(lm=lm)

def search_wikipedia(query: str) -> list[str]:
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)      # The url is a custom endpoint for a Wikipedia dataset
    return [x['text'] for x in results]

rag = dspy.ChainOfThought('context, question -> response')

question = "How do i sort a list in python?"
response = rag(context=search_wikipedia(question), question=question)
# print(response)      # From this the generated response was in a single paragraph. So below i have enhanced the response.

# Extract only the 'response' field from the pridiction
response_text = response.response.strip()   # Remove extra spaces/newlines
console.print(Markdown(response_text))      # Print the response using Rich Markdown for better formatting



# OUTPUT : 

# To sort a list in Python, you can use either of the following methods:

#  1 Using the sort() method:
   
#     my_list = [3, 1, 4, 1, 5, 9]
#     my_list.sort()  # This will sort the list in place
#     print(my_list)  # Output: [1, 1, 3, 4, 5, 9]
   
#  2 Using the sorted() function:
   
#     my_list = [3, 1, 4, 1, 5, 9]
#     sorted_list = sorted(my_list)  # This returns a new sorted list
#     print(sorted_list)  # Output: [1, 1, 3, 4, 5, 9]
   

# You can also sort in reverse order by passing the reverse=True argument to either method.