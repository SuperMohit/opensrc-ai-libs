import requests
import json

url = 'https://r.jina.ai/https://github.com/jina-ai/reader/blob/main/backend/functions/src/index.ts'
# headers = {
#     'Authorization': 'Bearer jina_7eff64765f6e4f7bba6711e1bfdc1c16u4hevZVzYf9Xq1g3bs2j4nAPqkQg'
# }

response = requests.get(url)
print(response.text)









