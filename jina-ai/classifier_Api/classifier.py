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
        {"text": """def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)"""},
        
        {"text": """async def fetch_data(url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.json()"""},
        
        {"text": """class BinaryTree:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None"""},
        
        {"text": """@pytest.fixture
            def test_database():
                db = Database('test.db')
                yield db
                db.cleanup()"""}
    ],
    "labels": [
        "Sorting Algorithms",
        "Asynchronous Programming",
        "Data Structures",
        "Testing",
        "Web Development",
        "Machine Learning"
    ]
}

response = requests.post(url, headers=headers, json=data)
# print(response.json())

print(json.dumps(response.json(), indent=4))



# Output:  

# {
#     "usage": {
#         "total_tokens": 261
#     },
#     "data": [
#         {
#             "object": "classification",
#             "index": 0,
#             "prediction": "Sorting Algorithms",
#             "score": 0.2034107893705368,
#             "predictions": [
#                 {
#                     "label": "Sorting Algorithms",
#                     "score": 0.2034107893705368
#                 },
#                 {
#                     "label": "Asynchronous Programming",
#                     "score": 0.16511741280555725
#                 },
#                 {
#                     "label": "Data Structures",
#                     "score": 0.16514666378498077
#                 },
#                 {
#                     "label": "Testing",
#                     "score": 0.16585001349449158
#                 },
#                 {
#                     "label": "Web Development",
#                     "score": 0.14804264903068542
#                 },
#                 {
#                     "label": "Machine Learning",
#                     "score": 0.15243254601955414
#                 }
#             ]
#         },
#         {
#             "object": "classification",
#             "index": 1,
#             "prediction": "Asynchronous Programming",
#             "score": 0.17949050664901733,
#             "predictions": [
#                 {
#                     "label": "Sorting Algorithms",
#                     "score": 0.1538964956998825
#                 },
#                 {
#                     "label": "Asynchronous Programming",
#                     "score": 0.17949050664901733
#                 },
#                 {
#                     "label": "Data Structures",
#                     "score": 0.16366107761859894
#                 },
#                 {
#                     "label": "Testing",
#                     "score": 0.17457976937294006
#                 },
#                 {
#                     "label": "Web Development",
#                     "score": 0.16760477423667908
#                 },
#                 {
#                     "label": "Machine Learning",
#                     "score": 0.16076737642288208
#                 }
#             ]
#         },
#         {
#             "object": "classification",
#             "index": 2,
#             "prediction": "Data Structures",
#             "score": 0.17511968314647675,
#             "predictions": [
#                 {
#                     "label": "Sorting Algorithms",
#                     "score": 0.16707676649093628
#                 },
#                 {
#                     "label": "Asynchronous Programming",
#                     "score": 0.15922032296657562
#                 },
#                 {
#                     "label": "Data Structures",
#                     "score": 0.17511968314647675
#                 },
#                 {
#                     "label": "Testing",
#                     "score": 0.17479465901851654
#                 },
#                 {
#                     "label": "Web Development",
#                     "score": 0.15284289419651031
#                 },
#                 {
#                     "label": "Machine Learning",
#                     "score": 0.17094576358795166
#                 }
#             ]
#         },
#         {
#             "object": "classification",
#             "index": 3,
#             "prediction": "Testing",
#             "score": 0.190588116645813,
#                     "score": 0.17372426390647888
#                 },
#                 {
#                     "label": "Testing",
#                     "score": 0.190588116645813
#                 },
#                 {
#                     "label": "Web Development",
#                     "score": 0.1619735062122345
#                 },
#                 {
#                     "label": "Machine Learning",
#                     "score": 0.1625068187713623
#                 }
#             ]
#         }
#     ]
# }