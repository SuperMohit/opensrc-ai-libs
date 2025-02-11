import requests
import json

url = 'https://api.jina.ai/v1/embeddings'
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer jina_7eff64765f6e4f7bba6711e1bfdc1c16u4hevZVzYf9Xq1g3bs2j4nAPqkQg"
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
            "text": "Un beau coucher de soleil sur la plage"
        },
        {
            "text": "海滩上美丽的日落"
        },
        {
            "text": "浜辺に沈む美しい夕日"
        },
        {
            "image": "https://i.ibb.co/nQNGqL0/beach1.jpg"
        },
        {
            "image": "https://i.ibb.co/r5w8hG8/beach2.jpg"
        },
        {
            "image": "R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7"
        },
        {
            "image": "https://images.pexels.com/photos/210019/pexels-photo-210019.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print(json.dumps(response.json(), indent=4))
