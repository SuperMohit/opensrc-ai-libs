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
      {"text": "https://masterpiecer-images.s3.yandex.net/644619ca68e111eebe1c96e999421984:upscaled"}
    ],
    "labels": [
        "the blue car is on the left, the red car is on the right",
        "the blue car is on the right, the red car is on the left",
        "the blue car is on top of the red car",
        "the blue car is below the red car"
    ]
}

response = requests.post(url, headers=headers, json=data)
print(json.dumps(response.json(), indent=4))


# Output: 

# {
#     "usage": {
#         "total_tokens": 94
#     },
#     "data": [
#         {
#             "object": "classification",
#             "index": 0,
#             "prediction": "the blue car is on the left, the red car is on the right",
#             "score": 0.2582927346229553,
#             "predictions": [
#                 {
#                     "label": "the blue car is on the left, the red car is on the right",
#                     "score": 0.2582927346229553
#                 },
#                 {
#                     "label": "the blue car is on the right, the red car is on the left",
#                     "score": 0.2575545907020569
#                 },
#                 {
#                     "label": "the blue car is on top of the red car",
#                     "score": 0.2407442033290863
#                 },
#                 {
#                     "label": "the blue car is below the red car",
#                     "score": 0.24340853095054626
#                 }
#             ]
#         }
#     ]
# }
