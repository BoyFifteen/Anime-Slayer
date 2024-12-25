from os import name
import requests

url = "https://anslayer.com/anime/public/animes/get-published-animes"

params = {
  'json': "{\"_offset\":0,\"_limit\":30,\"_order_by\":\"latest_first\",\"list_type\":\"filter\",\"anime_name\":\"juju\",\"just_info\":\"Yes\"}"
}

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Accept-Encoding': "gzip",
  'client-id': "android-app2",
  'client-secret': "7befba6263cc14c90d2f1d6da2c5cf9b251bfbbd",
  'accept': "application/*+json",
  'authorization': "Bearer e1deca491f5a64cbe5ec1de260a03639e56dbc73"
}

response = requests.get(url, params=params, headers=headers).json()

res=response['response']['data']
for id in res:
    i=id['anime_id']
    name=id['anime_name']
    year=id['anime_release_year']
    print(f'[{i}] {name} / {year}')
