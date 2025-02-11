import requests
import json

url = 'https://segment.jina.ai/'
headers = {
    'Content-Type': 'application/json',
    # 'Authorization': 'Bearer jina_7eff64765f6e4f7bba6711e1bfdc1c16u4hevZVzYf9Xq1g3bs2j4nAPqkQg'
}
data = {
     "content": """

    # React Component
    const UserProfile = ({ userId, userData }) => {
        const [loading, setLoading] = useState(true);
        
        useEffect(() => {
            fetchUserData(userId)
                .then(data => {
                    setUserData(data);
                    setLoading(false);
                });
        }, [userId]);
        
        return (
            <div className="profile-container">
                {loading ? <Spinner /> : (
                    <UserDetails data={userData} />
                )}
            </div>
        );
    };


    """,
    "return_tokens": True,
    "return_chunks": True,
    "max_chunk_length": 1000
}

response = requests.post(url, headers=headers, json=data)

print(json.dumps(response.json(), indent=4))



# Output :

# {
#     "num_tokens": 102,
#     "tokenizer": "cl100k_base",
#     "usage": {
#         "tokens": 0
#     },
#     "num_chunks": 2,
#     "chunk_positions": [
#         [
#             1,
#             576
#         ],
#         [
#             577,
#             582
#         ]
#     ],
#     "tokens": [
#         [
#             [
#                 "\n",
#                 [
#                     198
#                 ]
#             ],
#             [
#                 "   ",
#                 [
#                     262
#                 ]
#             ],
#             [
#                 " #",
#                 [
#                     674
#                 ]
#             ],
#             [
#                 " React",
#                 [
#                     3676
#                 ]
#             ],
#             [
#                 " Component",
#                 [
#                     5695
#                 ]
#             ],
#             [
#                 "\n",
#                 [
#                     198
#                 ]
#             ],
#             [
#                 "   ",
#                 [
#                     262
#                 ]
#             ],
#             [
#                 " const",
#                 [
#                     738
#                 ]
#             ],
#             [
#                 " UserProfile",
#                 [
#                     56199
#                 ]
#             ],
#             [
#                 " =",
#                 [
#                     284
#                 ]
#             ],
#             [
#                 " ({",
#                 [
#                     9657
#                 ]
#             ],
#             [
#                 " userId",
#                 [
#                     10542
#                 ]
#             ],
#             [
#                 ",",
#                 [
#                     11
#                 ]
#             ],
#             [
#                 " userData",
#                 [
#                     35485
#                 ]
#             ],
#             [
#                 " })",
#                 [
#                     6547
#                 ]
#             ],
#             [
#                 " =>",
#                 [
#                     591
#                 ]
#             ],
#             [
#                 " {\n",
#                 [
#                     341
#                 ]
#             ],
#             [
#                 "       ",
#                 [
#                     286
#                 ]
#             ],
#             [
#                 " const",
#                 [
#                     738
#                 ]
#             ],
#             [
#                 " [",
#                 [
#                     510
#                 ]
#             ],
#             [
#                 "loading",
#                 [
#                     10853
#                 ]
#             ],
#             [
#                 ",",
#                 [
#                     11
#                 ]
#             ],
#             [
#                 " setLoading",
#                 [
#                     49689
#                 ]
#             ],
#             [
#                 "]",
#                 [
#                     60
#                 ]
#             ],
#             [
#                 " =",
#                 [
#                     284
#                 ]
#             ],
#             [
#                 " useState",
#                 [
#                     8264
#                 ]
#             ],
#             [
#                 "(true",
#                 [
#                     3800
#                 ]
#             ],
#             [
#                 ");\n",
#                 [
#                     317
#                 ]
#             ],
#             [
#                 "        \n",
#                 [
#                     1827
#                 ]
#             ],
#             [
#                 "       ",
#                 [
#                     286
#                 ]
#             ],
#             [
#                 " useEffect",
#                 [
#                     14567
#                 ]
#             ],
#             [
#                 "(()",
#                 [
#                     5175
#                 ]
#             ],
#             [
#                 " =>",
#                 [
#                     591
#                 ]
#             ],
#             [
#                 " {\n",
#                 [
#                     341
#                 ]
#             ],
#             [
#                 "           ",
#                 [
#                     310
#                 ]
#             ],
#             [
#                 " fetch",
#                 [
#                     7963
#                 ]
#             ],
#             [
#                 "UserData",
#                 [
#                     40585
#                 ]
#             ],
#             [
#                 "(userId",
#                 [
#                     25484
#                 ]
#             ],
#             [
#                 ")\n",
#                 [
#                     340
#                 ]
#             ],
#             [
#                 "               ",
#                 [
#                     394
#                 ]
#             ],
#             [
#                 " .",
#                 [
#                     662
#                 ]
#             ],
#             [
#                 "then",
#                 [
#                     3473
#                 ]
#             ],
#             [
#                 "(data",
#                 [
#                     2657
#                 ]
#             ],
#             [
#                 " =>",
#                 [
#                     591
#                 ]
#             ],
#             [
#                 " {\n",
#                 [
#                     341
#                 ]
#             ],
#             [
#                 "                   ",
#                 [
#                     504
#                 ]
#             ],
#             [
#                 " set",
#                 [
#                     743
#                 ]
#             ],
#             [
#                 "UserData",
#                 [
#                     40585
#                 ]
#             ],
#             [
#                 "(data",
#                 [
#                     2657
#                 ]
#             ],
#             [
#                 ");\n",
#                 [
#                     317
#                 ]
#             ],
#             [
#                 "                   ",
#                 [
#                     504
#                 ]
#             ],
#             [
#                 " setLoading",
#                 [
#                     49689
#                 ]
#             ],
#             [
#                 "(false",
#                 [
#                     3660
#                 ]
#             ],
#             [
#                 ");\n",
#                 [
#                     317
#                 ]
#             ],
#             [
#                 "               ",
#                 [
#                     394
#                 ]
#             ],
#             [
#                 " });\n",
#                 [
#                     1657
#                 ]
#             ],
#             [
#                 "       ",
#                 [
#                     286
#                 ]
#             ],
#             [
#                 " },",
#                 [
#                     2529
#                 ]
#             ],
#             [
#                 " [",
#                 [
#                     510
#                 ]
#             ],
#             [
#                 "userId",
#                 [
#                     13816
#                 ]
#             ],
#             [
#                 "]);\n",
#                 [
#                     2622
#                 ]
#             ],
#             [
#                 "        \n",
#                 [
#                     1827
#                 ]
#             ],
#             [
#                 "       ",
#                 [
#                     286
#                 ]
#             ],
#             [
#                 " return",
#                 [
#                     471
#                 ]
#             ],
#             [
#                 " (\n",
#                 [
#                     2456
#                 ]
#             ],
#             [
#                 "           ",
#                 [
#                     310
#                 ]
#             ],
#             [
#                 " <",
#                 [
#                     366
#                 ]
#             ],
#             [
#                 "div",
#                 [
#                     614
#                 ]
#             ],
#             [
#                 " className",
#                 [
#                     2022
#                 ]
#             ],
#             [
#                 "=\"",
#                 [
#                     429
#                 ]
#             ],
#             [
#                 "profile",
#                 [
#                     5478
#                 ]
#             ],
#             [
#                 "-container",
#                 [
#                     12863
#                 ]
#             ],
#             [
#                 "\">\n",
#                 [
#                     891
#                 ]
#             ],
#             [
#                 "               ",
#                 [
#                     394
#                 ]
#             ],
#             [
#                 " {",
#                 [
#                     314
#                 ]
#             ],
#             [
#                 "loading",
#                 [
#                     10853
#                 ]
#             ],
#             [
#                 " ?",
#                 [
#                     949
#                 ]
#             ],
#             [
#                 " <",
#                 [
#                     366
#                 ]
#             ],
#             [
#                 "Spinner",
#                 [
#                     32181
#                 ]
#             ],
#             [
#                 " />",
#                 [
#                     6338
#                 ]
#             ],
#             [
#                 " :",
#                 [
#                     551
#                 ]
#             ],
#             [
#                 " (\n",
#                 [
#                     2456
#                 ]
#             ],
#             [
#                 "                   ",
#                 [
#                     504
#                 ]
#             ],
#             [
#                 " <",
#                 [
#                     366
#                 ]
#             ],
#             [
#                 "User",
#                 [
#                     1502
#                 ]
#             ],
#             [
#                 "Details",
#                 [
#                     7955
#                 ]
#             ],
#             [
#                 " data",
#                 [
#                     828
#                 ]
#             ],
#             [
#                 "={",
#                 [
#                     1185
#                 ]
#             ],
#             [
#                 "userData",
#                 [
#                     43626
#                 ]
#             ],
#             [
#                 "}",
#                 [
#                     92
#                 ]
#             ],
#             [
#                 " />\n",
#                 [
#                     2662
#                 ]
#             ],
#             [
#                 "               ",
#                 [
#                     394
#                 ]
#             ],
#             [
#                 " )}\n",
#                 [
#                     18026
#                 ]
#             ],
#             [
#                 "           ",
#                 [
#                     310
#                 ]
#             ],
#             [
#                 " </",
#                 [
#                     694
#                 ]
#             ],
#             [
#                 "div",
#                 [
#                     614
#                 ]
#             ],
#             [
#                 ">\n",
#                 [
#                     397
#                 ]
#             ],
#             [
#                 "       ",
#                 [
#                     286
#                 ]
#             ],
#             [
#                 " );\n",
#                 [
#                     1465
#                 ]
#             ],
#             [
#                 "   ",
#                 [
#                     262
#                 ]
#             ],
#             [
#                 " };\n",
#                 [
#                     2670
#                 ]
#             ]
#         ],
#         [
#             [
#                 "\n",
#                 [
#                     198
#                 ]
#             ],
#             [
#                 "    ",
#                 [
#                     257
#                 ]
#             ]
#         ]
#     ],
#     "chunks": [
#         "\n    # React Component\n    const UserProfile = ({ userId, userData }) => {\n        const [loading, setLoading] = useState(true);\n        \n        useEffect(() => {\n            fetchUserData(userId)\n                .then(data => {\n                    setUserData(data);\n             
#        setLoading(false);\n                });\n        }, [userId]);\n        \n        return (\n            <div className=\"profile-container\">\n                {loading ? <Spinner /> : (\n                    <UserDetails data={userData} />\n                )}\n            </div>\n        );\n    };\n",
#         "\n    "
#     ]
# }