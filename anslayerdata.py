import requests

url = "https://anslayer.com/anime/public/anime/get-anime-details"

params = {
  'anime_id': "2365",
  'fetch_episodes': "No",
  'more_info': "Yes"
}

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Accept-Encoding': "gzip",
  'client-id': "android-app2",
  'client-secret': "7befba6263cc14c90d2f1d6da2c5cf9b251bfbbd",
  'accept': "application/*+json",
  'authorization': "Bearer e1deca491f5a64cbe5ec1de260a03639e56dbc73"
}

response = requests.get(url, params=params, headers=headers)

print(response.text)