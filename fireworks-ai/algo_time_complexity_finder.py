import openai
import json

client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>")

# Define the function tool for retrieving algorithm time complexity
tools = [
    {
        "type": "function",
        "function": {
            # The name of the function
            "name": "get_algorithm_complexity",
            # A detailed description of what the function does
            "description": "Retrieve the time complexity of a given algorithm.",
            # Define the JSON schema for the function parameters
            "parameters": {
                # Always declare a top-level object for parameters
                "type": "object",
                # Properties define the arguments for the function
                "properties": {
                    "algorithm_name": {
                        # JSON Schema type
                        "type": "string",
                        # A detailed description of the property
                        "description": "The name of the algorithm, e.g., 'QuickSort'."
                    },
                },
                # Specify which properties are required
                "required": ["algorithm_name"],
            },
        },
    }
]

# Define a comprehensive system prompt
prompt = f"""
You have access to the following function:

Function Name: '{tools[0]["function"]["name"]}'
Purpose: '{tools[0]["function"]["description"]}'
Parameters Schema: {json.dumps(tools[0]["function"]["parameters"], indent=4)}

Instructions for Using Functions:
1. Use the function '{tools[0]["function"]["name"]}' to retrieve the time complexity of an algorithm.
2. If a function call is necessary, reply ONLY in the following format:
   <function={tools[0]["function"]["name"]}>{{"algorithm_name": "example_algorithm"}}</function>
3. Adhere strictly to the parameters schema. Ensure all required fields are provided.
4. Use the function only when you cannot directly answer using general knowledge.
5. If no function is necessary, respond to the query directly without mentioning the function.

Examples:
- For a query like "What is the time complexity of QuickSort?" respond with:
  <function=get_algorithm_complexity>{{"algorithm_name": "QuickSort"}}</function>
- For "What is an algorithm?" respond with general knowledge and do NOT use the function.
"""

# Initial message context
messages = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": "What is the time complexity of QuickSort?"}
]

# Call the model
chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=messages,
    tools=tools,
    temperature=0.1
)

print(chat_completion.choices[0].message.model_dump_json(indent=4))


# Define function implementation for retrieving algorithm complexity
def get_algorithm_complexity(algorithm_name: str):
    complexities = {
        "QuickSort": "O(n log n) on average, O(n²) in worst case",
        "MergeSort": "O(n log n)",
        "BubbleSort": "O(n²)",
        "BinarySearch": "O(log n)",
        "Dijkstra": "O((V + E) log V)"
    }
    return {"complexity": complexities.get(algorithm_name, "Unknown algorithm")}

# Extract function call details
function_call = chat_completion.choices[0].message.tool_calls[0].function
tool_response = locals()[function_call.name](**json.loads(function_call.arguments))

print(tool_response)

# Append the response from the agent
messages.append(
    {
        "role": chat_completion.choices[0].message.role, 
        "content": "",
        "tool_calls": [
            tool_call.model_dump()
            for tool_call in chat_completion.choices[0].message.tool_calls
        ]
    }
)

# Append the response from the tool 
messages.append(
    {
        "role": "tool",
        "content": json.dumps(tool_response)
    }
)

# Generate the final response
next_chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=messages,
    tools=tools,
    temperature=0.1
)

print(next_chat_completion.choices[0].message.model_dump_json(indent=4))





# OUTPUT 


# {
#     "content": "The time complexity of QuickSort is O(n log n) on average, O(n²) in worst case.",
#     "refusal": null,
#     "role": "assistant",
#     "audio": null,
#     "function_call": null,
#     "tool_calls": null
# }