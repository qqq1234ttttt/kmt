import requests

url = "https://www.tiktok.com/@tiktok"

headers = {
    "User-Agent": "Mozilla/5.0 Chrome/120",
    "Cookie": "531faee73c8404804e64000df54b3f56"
}

res = requests.get(url, headers=headers)

print(res.status_code)
print(res.text[:500])
