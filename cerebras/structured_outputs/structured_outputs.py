from dotenv import load_dotenv
import os 
import openai

load_dotenv()

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key= os.environ.get("CEREBRAS_API_KEY")
)


# To insure structured response we'll use a JSON schema to define our output structure.
movie_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "director": {"type": "string"},
        "year": {"type": "number"}
    },
    "required": ["title", "director", "year"],
    "additionalProperties": False
}

completion = client.chat.completions.create(
    messages= [
        {"role": "system", "content": "You are a helpful assistant that generates movie recommendations."},
        {"role": "user", "content": "Suggest the best sci-fi movie of all time."}
    ],
    model="llama-3.3-70b",

    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "movie_schema",
            "strict": True,
            "schema": movie_schema
        }
    }
)


movie_data = completion.choices[0].message.content

print(movie_data)



# OUTPUT: 

# {"title": "Blade Runner", "director": "Ridley Scott", "year": 1982}