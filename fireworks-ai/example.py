import openai
import json

client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>"
)

# Define the function tool for getting city population
tools = [
    {
        "type": "function",
        "function": {
            # The name of the function
            "name": "get_city_population",
            # A detailed description of what the function does
            "description": "Retrieve the current population data for a specified city.",
            # Define the JSON schema for the function parameters
            "parameters": {
                # Always declare a top-level object for parameters
                "type": "object",
                # Properties define the arguments for the function
                "properties": {
                    "city_name": {
                        # JSON Schema type
                        "type": "string",
                        # A detailed description of the property
                        "description": "The name of the city for which population data is needed, e.g., 'San Francisco'."
                    },
                },
                # Specify which properties are required
                "required": ["city_name"],
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
1. Use the function '{tools[0]["function"]["name"]}' to retrieve population data when required.
2. If a function call is necessary, reply ONLY in the following format:
   <function={tools[0]["function"]["name"]}>{{"city_name": "example_city"}}</function>
3. Adhere strictly to the parameters schema. Ensure all required fields are provided.
4. Use the function only when you cannot directly answer using general knowledge.
5. If no function is necessary, respond to the query directly without mentioning the function.

Examples:
- For a query like "What is the population of Toronto?" respond with:
  <function=get_city_population>{{"city_name": "Toronto"}}</function>
- For "What is the population of the Earth?" respond with general knowledge and do NOT use the function.
"""

# Initial message context
messages = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": "What is the population of San Francisco?"}
]

# Call the model
chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=messages,
    tools=tools,
    temperature=0.1
)

# Print the model's response
# print(chat_completion.choices[0].message.model_dump_json(indent=4))

def get_city_population(city_name: str):
    print(f"{city_name=}")
    if city_name == "San Francisco":
        return {"population": 883305}
    else:
        raise NotImplementedError()

function_call = chat_completion.choices[0].message.tool_calls[0].function
tool_response = locals()[function_call.name](**json.loads(function_call.arguments))
# print(tool_response)

agent_response = chat_completion.choices[0].message

# Append the response from the agent
messages.append(
    {
        "role": agent_response.role, 
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

next_chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=messages,
    tools=tools,
    temperature=0.1
)

print(next_chat_completion.choices[0].message.model_dump_json(indent=4))



# OUTPUT of Line 76

# {
#     "content": null,
#     "refusal": null,
#     "role": "assistant",
#     "audio": null,
#     "function_call": null,
#     "tool_calls": [
#         {
#             "id": "call_v9mUOSU3VfKIPC6lHvyQN44w",
#             "function": {
#                 "arguments": "{\"city_name\": \"San Francisco\"}",
#                 "name": "get_city_population"
#             },
#             "type": "function",
#             "index": 0
#         }
#     ]
# }


# Final OUTPUT

# {
#     "content": "The population of San Francisco is 883305.",
#     "refusal": null,
#     "role": "assistant",
#     "audio": null,
#     "function_call": null,
#     "tool_calls": null
# }

