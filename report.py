import requests
import re

print("\n🔥 KMT TikTok DOWNGRADE TOOL\n")

username = input("Enter username: ").replace("@","")

# 👉 mobile endpoint (less strict than desktop)
url = f"https://m.tiktok.com/@{username}"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12)",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

print("[*] Requesting mobile page...")

try:
    res = requests.get(url, headers=headers, timeout=10)
    html = res.text
except:
    print("❌ Network error")
    exit()

# =====================
# BLOCK CHECK
# =====================
if "slardar" in html.lower() or len(html) < 1500:
    print("❌ Blocked / Empty response")
    exit()

# =====================
# SAFE EXTRACTION (loose patterns)
# =====================
def find(pattern):
    m = re.search(pattern, html)
    return m.group(1) if m else "N/A"

print("\n===== RESULT (LIMITED DATA) =====")

print("User ID:", find(r'"id":"(\d+)"'))
print("Nickname:", find(r'"nickname":"([^"]+)"'))
print("SecUID:", find(r'"secUid":"([^"]+)"'))

# sometimes available
followers = find(r'"followerCount":(\d+)')
following = find(r'"followingCount":(\d+)')
videos = find(r'"videoCount":(\d+)')

print("Followers:", followers)
print("Following:", following)
print("Videos:", videos)

print("\n⚠️ Note: Limited data due to TikTok protection")
