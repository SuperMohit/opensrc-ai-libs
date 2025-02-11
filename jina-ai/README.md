# JINA AI

## Overview

Jina AI offers a comprehensive suite of APIs to supercharge your search and data processing workflows:

`Reader API`: Extracts clean, LLM-friendly text from URLs.

`Embeddings API`: Generates embeddings for text and images.

`Reranker API`: Reorders search results to align with user intent.

`Classifier API`: Categorizes text and images using advanced models.

`Segmenter API`: Tokenizes and segments long texts for efficient processing.

## Reader API

Convert a URL to LLM-friendly input, by simply adding r.jina.ai in front.
The Reader API is free of charge and does not require an API key. Simply prepend `https://r.jina.ai/` to your URL.

`Example`: Your URL `https://google.com` => Reader URL `https://r.jina.ai/https://google.com`

Reader also reads `images` and `PDF's`.

```bash
import requests
import json

url = 'https://r.jina.ai/https://example.com'
headers = {
  'Authorization': ''
}

response = requests.get(url)
print(response.text)
```

## Reader for Search :

Reader allows you to feed your LLM with the latest information from the web. Simply prepend `https://s.jina.ai/` to your query, and Reader will search the web and return the top five results with their URLs and contents, each in clean, LLM-friendly text.

`Example`: your query - Explain about Cricket

Reader URL : `https://s.jina.ai/https://Explain` about Cricket

## Reader for Fact Checking :

The new grounding endpoint offers an end-to-end, near real-time fact-checking experience. It takes a given statement, grounds it using real-time web search results, and returns a factuality score and the exact references used.

Use `g.jina.ai` for grounding.

This will call grounding engine to do fact-checking.

## Embedding API :

Convert complex data like words, sentences, or images into numerical vectors that can capture important relationships between data points. These vectors often have fixed dimensions and are designed to preserve semantic meaning, so similar data points are mapped close to each other in this space.

Use URL : `https://api.jina.ai/v1/embeddings`

```bash
import requests
import json

url = 'https://api.jina.ai/v1/embeddings'
headers = {
    "Content-Type": "application/json",
    "Authorization": " "
}
data = {
    "model": "jina-clip-v2",
    "dimensions": 1024,
    "normalized": True,
    "embedding_type": "float",
    "input": [
        {
            "text": "A beautiful sunset over the beach"
        },
        {
            "text": "海滩上美丽的日落"
        },
        {
            "image": "https://i.ibb.co/nQNGqL0/beach1.jpg"
        },
    ]
}

response = requests.post(url, headers=headers, json=data)
print(json.dumps(response.json(), indent=4))

```

## Reranker API :

A reranker API is a type of API used in machine learning and search systems to re-rank or re-order a list of results based on specific criteria or relevance after an initial ranking or retrieval process.

Use URL : `https://api.jina.ai/v1/rerank`

```bash
import requests
import json

url = 'https://api.jina.ai/v1/rerank'
headers = {
    'Content-Type': 'application/json',
    'Authorization': ''  # Add your API key here
}

data = {
    "model": "jina-reranker-v2-base-multilingual",
    "query": "AI advancements in 2024",
    "top_n": 3,
    "documents": [
        "OpenAI announces GPT-5 with multimodal capabilities.",
        "SpaceX launches a new rocket for interplanetary travel.",
        "Apple unveils its first AI-powered iPhone with on-device learning.",
        "Scientists discover a new exoplanet with Earth-like conditions.",
    ]
}

# Make the API Request
response = requests.post(url, headers=headers, json=data)

# Pretty-print the JSON response
print(json.dumps(response.json(), indent=4))

```

## Classifier API :

Classify data into predefined categories or labels.

Use URL : `https://api.jina.ai/v1/classify`

```bash
import requests
import json

url = 'https://api.jina.ai/v1/classify'
headers = {
    'Content-Type': 'application/json',
    'Authorization': ' '
}

data = {
    "model": "jina-clip-v2",
    "input": [
        {"text": "A futuristic electric car with self-driving capabilities"}
    ],
    "labels": [
        "Technology and Gadgets",
        "Automobiles",
        "Nature and Outdoors"
    ]
}

response = requests.post(url, headers=headers, json=data)
print(json.dumps(response.json(), indent=4))

```

## Segmenter API :

Converts text into tokens or chunks.
Can also use Segmenter API to cut long documents into smaller chunks, making it easier to process them in embeddings or rerankers.

Use URL : `https://segment.jina.ai/`

```bash
import requests
import json

url = 'https://segment.jina.ai/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': ''  # Add your API key here
}

data = {
    "content": "Jina AI is revolutionizing search technology! 🚀",
    "return_tokens": True,
    "return_chunks": True,
    "max_chunk_length": 50
}

response = requests.post(url, headers=headers, json=data)
print(json.dumps(response.json(), indent=4))

```
