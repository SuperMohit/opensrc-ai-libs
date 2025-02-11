import requests
import json

url = 'https://api.jina.ai/v1/rerank'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer jina_7eff64765f6e4f7bba6711e1bfdc1c16u4hevZVzYf9Xq1g3bs2j4nAPqkQg'
}
data = {
    "model": "jina-reranker-v2-base-multilingual",
    "query": "Find code that implements a binary search algorithm",
    "top_n": 3,
    "documents": [
        
        """def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1""",
        
        
        """def linear_search(arr, target):
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
            return -1""",
        
        
        """def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr""",
        
        
        """def binary_search_recursive(arr, target, low, high):
            if high >= low:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    return binary_search_recursive(arr, target, low, mid - 1)
                else:
                    return binary_search_recursive(arr, target, mid + 1, high)
            return -1""",
        
       
        """def jump_search(arr, target):
            import math
            n = len(arr)
            step = int(math.sqrt(n))
            prev = 0
            while arr[min(step, n) - 1] < target:
                prev = step
                step += int(math.sqrt(n))
                if prev >= n:
                    return -1
            while arr[prev] < target:
                prev += 1
                if prev == min(step, n):
                    return -1
            if arr[prev] == target:
                return prev
            return -1""",
        
        
        """def interpolation_search(arr, target):
            low = 0
            high = len(arr) - 1
            while low <= high and target >= arr[low] and target <= arr[high]:
                pos = low + ((high - low) * (target - arr[low]) // 
                           (arr[high] - arr[low]))
                if arr[pos] == target:
                    return pos
                if arr[pos] < target:
                    low = pos + 1
                else:
                    high = pos - 1
            return -1"""
    ]
}

response = requests.post(url, headers=headers, json=data)

print(json.dumps(response.json(), indent=4))




# Output:  {
#     "model": "jina-reranker-v2-base-multilingual",
#     "usage": {
#         "total_tokens": 556
#     },
#     "results": [
#         {
#             "index": 0,
#             "document": {
#                 "text": "def binary_search(arr, target):\n            left, right = 0, len(arr) - 1\n            while left <= right:\n                mid = (left + right) // 2\n                if arr[mid] == target:\n                    return mid\n                elif arr[mid] < target:\n                    left = mid + 1\n                else:\n                    right = mid - 1\n            return -1"
#             },
#             "relevance_score": 0.6297746300697327
#         },
#         {
#             "index": 3,
#             "document": {
#                 "text": "def binary_search_recursive(arr, target, low, high):\n            if high >= low:\n                mid = (low + high) // 2\n                if arr[mid] == target:\n                    return mid\n                elif arr[mid] > target:\n                    return binary_search_recursive(arr, target, low, mid - 1)\n                else:\n                    return binary_search_recursive(arr, target, mid + 1, high)\n            return -1"
#             },
#             "relevance_score": 0.5846269130706787
#         },
#         {
#             "index": 4,
#             "document": {
#                 "text": "def jump_search(arr, target):\n            import math\n            n = len(arr)\n            step = int(math.sqrt(n))\n            prev = 0\n            while arr[min(step, n) - 1] < target:\n                prev = step\n                step += int(math.sqrt(n))\n                if prev >= n:\n                    return -1\n            while arr[prev] < target:\n                prev += 1\n                if prev == min(step, n):\n                    return -1\n            if arr[prev] == target:\n                return prev\n            return -1"
#             },
#             "relevance_score": 0.18010666966438293
#         }
#     ]
# }