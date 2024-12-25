import requests

url = "https://anslayer.com/la/public/api/fw"

payload = {
  'n': "jujutsu_kaisen_tv\\1",
  'inf': "{\"a\": \"eCMq8CRVxeJx2fpLMj0qeHnDeQUQwioRoURF1jNL+set4n9ErdANL/9jgtOCR0iAZ51adz2ZCrhqPvUXHyRff5G7S8TO+W9w/SIBVt8zJ2T91aB4T7vmRH9QSRWJD1YBHQnrBTQAIOH6iLmUdXZH9w==\", \"b\": \"105.103.32.44\"}"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
  'Accept-Encoding': "gzip"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)