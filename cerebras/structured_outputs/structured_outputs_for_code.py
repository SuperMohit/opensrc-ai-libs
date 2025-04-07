from dotenv import load_dotenv
import os 
import openai

load_dotenv()

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key= os.environ.get("CEREBRAS_API_KEY")
)

code_schema = {
    "type": "object",
    "properties": {
        "language": {"type": "string"},
        "description": {"type": "string"},
        "code_snippet": {"type": "string"}
    },
    "required": ["language", "description", "code_snippet"],
    "additionalProperties": False
}


completion = client.chat.completions.create(
    model="llama-3.3-70b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that provides programming-related information and code snippets."},
        {"role": "user", "content": "Explain how to implement a binary search algorithm in Python."}
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "code_schema",
            "strict": True,
            "schema": code_schema
        }
    }
)


code_data = completion.choices[0].message.content

print(code_data)




# OUTPUT: 

# {"language": "Python", "description": "Binary search algorithm implementation", "code_snippet": "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n\n# Example usage:\narr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]\ntarget = 23\nresult = binary_search(arr, target)\nif result != -1:\n    print(f\"Element {target} found at index {result}\")\nelse:\n    print(f\"Element {target} not found in the array\")"}