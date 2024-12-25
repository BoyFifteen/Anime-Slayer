import requests

url = "https://anslayer.com/anime/public/episodes/get-episodes-new"

payload = {
  'inf': "{\"a\": \"eCMq8CRVxeJx2fpLMj0qeHnDeQUQwioRoURF1jNL+set4n9ErdANL/9jgtOCR0iAZ51adz2ZCrhqPvUXHyRff5G7S8TO+W9w/SIBVt8zJ2T91aB4T7vmRH9QSRWJD1YBHQnrBTQAIOH6iLmUdXZH9w==\", \"b\": \"105.103.32.44\"}",
  'json': "{\"anime_id\":2365,\"episode_id\":\"42795\"}"
}

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Accept-Encoding': "gzip",
  'client-id': "android-app2",
  'client-secret': "7befba6263cc14c90d2f1d6da2c5cf9b251bfbbd",
  'accept': "application/*+json",
  'authorization': "Bearer e1deca491f5a64cbe5ec1de260a03639e56dbc73"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)