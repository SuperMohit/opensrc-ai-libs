import requests
import json

url = 'https://api.jina.ai/v1/classify'
headers = {
    "Content-Type": "application/json",
    'Authorization': 'Bearer jina_7eff64765f6e4f7bba6711e1bfdc1c16u4hevZVzYf9Xq1g3bs2j4nAPqkQg'
}
data = {
    "model": "jina-clip-v2",
    "input": [
      {"text": "https://picsum.photos/id/1/300/300"}
    ],
    "labels": [
       "There is a woman in the photo.",
       "There is a man in the photo."
    ]
}

response = requests.post(url, headers=headers, json=data)

print(json.dumps(response.json(), indent=4))


# Output: 

# {
#     "usage": {
#         "total_tokens": 36
#     },
#     "data": [
#         {
#             "object": "classification",
#             "index": 0,
#             "prediction": "There is a man in the photo.",
#             "score": 0.5104886889457703,
#             "predictions": [
#                 {
#                     "label": "There is a woman in the photo.",
#                     "score": 0.48951131105422974
#                 },
#                 {
#                     "label": "There is a man in the photo.",
#                     "score": 0.5104886889457703
#                 }
#             ]
#         }
#     ]
# }
