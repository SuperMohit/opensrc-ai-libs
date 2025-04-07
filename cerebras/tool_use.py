from dotenv import load_dotenv
import os
import openai
import re
import json

load_dotenv()

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY")
)

# Defining the tool that the AI will use

def calculate(expression):
    expression= re.sub(r'[^0-9+\-*/().]', '', expression)

    try:
        result = eval(expression)
        return str(result)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError, OverflowError):
        return "Error: Invalid expression"
    

# Defining the tool schema

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "A calculator tool that can perform basic arithmetic operations. Use this when you need to compute mathematical expressions or solve numerical problems.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

messages = [
    {"role": "system", "content": "You are a helpful assistant with access to a calculator. Use the calculator tool to compute mathematical expressions when needed."},
    {"role": "user", "content": "What's the result of 15 multiplied by 7?"},
]

response = client.chat.completions.create(
    model="llama-3.3-70b",
    messages=messages,
    tools=tools,
)

# print(response)

choice = response.choices[0].message

if choice.tool_calls:
    function_call = choice.tool_calls[0].function
    if function_call.name == "calculate":
        # Logging that the model is executing a function named "calculate".
        print(f"Model executing function '{function_call.name}' with arguments {function_call.arguments}")

        # Parse the arguments from JSON format and perform the requested calculation.
        arguments = json.loads(function_call.arguments)
        result = calculate(arguments["expression"])

        # Note: This is the result of executing the model's request (the tool call), not the model's own output.
        print(f"Calculation result sent to model: {result}")
       
       # Send the result back to the model to fulfill the request.
        messages.append({
            "role": "tool",
            "content": json.dumps(result),
            "tool_call_id": choice.tool_calls[0].id
        })
 
       # Request the final response from the model, now that it has the calculation result.
        final_response = client.chat.completions.create(
            model="llama-3.3-70b",
            messages=messages,
        )
        
        # Handle and display the model's final response.
        if final_response:
            print("Final model output:", final_response.choices[0].message.content)
        else:
            print("No final response received")
else:
    # Handle cases where the model's response does not include expected tool calls.
    print("Unexpected response from the model")




# OUTPUT: 

# Model executing function 'calculate' with arguments {"expression": "15*7"}
# Calculation result sent to model: 105
# Final model output: The result of 15 multiplied by 7 is 105.
