from dotenv import load_dotenv
import os
import openai

load_dotenv()

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key= os.environ.get("CEREBRAS_API_KEY")
)

stream = client.chat.completions.create(
    messages=[
        {'role': 'user', 'content': 'What is a callback function?'}
    ],
    model="llama3.1-8b",
    stream= True
)

# for chunk in stream: 
#     print(chunk.choices[0].delta.content or "", end="")

response_content= ""

for chunk in stream: 
    response_content += chunk.choices[0].delta.content or ""


# Enhance the response for better readability
print("\n" + "=" * 50 + "\n")
print("Response:\n")
print(response_content.strip())
print("\n" + "=" * 50 + "\n")




# OUTPUT : 


# ==================================================

# Response:

# **Callback Functions: A Deeper Dive**

# A callback function is a function that is passed as an argument to another function, typically expected to be executed later. It's a way for one function to notify another function that a specific operation has been completed or to perform a specific action.

# **How Callbacks Work**

# When a callback function is passed to another function, it becomes a first-class citizen of that function. This means it can be stored, retrieved, and executed like any other variable. The function that receives the callback function is responsible for executing it when the necessary operation is complete.

# **Example Use Cases**

# 1. **Event-handling**: When a button is clicked, the click event can trigger a callback function to be executed.
# 2. **Asynchronous operations**: When making an HTTP request, a callback function can be used to handle the response.
# 3. **User authentication**: When a user logs in or out, a callback function can be executed to update the application state.

# **Benefits of Callbacks**

# 1. **Decoupling**: Callbacks allow for loose coupling between functions, making it easier to modify and extend code.
# 2. **Concurrency**: Callbacks enable background tasks to notify the main thread when they're complete, improving responsiveness.
# 3. **Error handling**: Callbacks make it easier to handle errors in asynchronous operations.

# **Example Code**

# ```javascript
# function greet(name, callback) {
#   console.log(`Hello, ${name}!`);
#   callback();
# }

# function sayThanks() {
#   console.log("Thanks for visiting!");
# }

# greet("Alice", sayThanks);
# // Output:
# // Hello, Alice!
# // Thanks for visiting!
# ```

# In this example, the `greet` function takes two arguments: `name` and `callback`. The `greet` function logs a greeting message and then calls the `callback` function, passing no arguments.

# **Best Practices**

# 1. **Use meaningful names**: Name your callback functions to clearly indicate their purpose.
# 2. **Avoid unnecessary complexity**: Keep callback functions simple and focused on a single task.
# 3. **Test thoroughly**: Verify that your callbacks are executed as expected.

# By understanding callback functions and using them effectively, you can write more modular, concurrent, and maintainable code.

# ==================================================