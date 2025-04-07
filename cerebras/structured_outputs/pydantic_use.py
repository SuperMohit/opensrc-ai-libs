from dotenv import load_dotenv
from pydantic import BaseModel
import os 
import openai

load_dotenv()

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key= os.environ.get("CEREBRAS_API_KEY")
)

# Define the schema using pydantic 
class Movie(BaseModel):
    title: str
    director: str
    year: int

movie_schema= Movie.model_json_schema()

completion = client.chat.completions.create(
    messages= [
        {"role": "system", "content": "You are a helpful assistant that generates movie recommendations."},
        {"role": "user", "content": "Suggest the best superhero movie of all time."}
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




# OUTPUT : 

# {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008}

