import requests
import re
import time

print("\n🔥 KMT TikTok INFO TOOL v3 (Auto Fallback)\n")

username = input("Enter username: ").replace("@","")

# =====================
# METHODS LIST (fallback system)
# =====================
urls = [
    f"https://www.tiktok.com/@{username}",
    f"https://m.tiktok.com/@{username}"
]

headers_list = [
    {
        "User-Agent": "Mozilla/5.0 Chrome/120",
        "Accept-Language": "en-US,en;q=0.9"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12)",
        "Referer": "https://www.google.com/"
    }
]

# =====================
# FETCH FUNCTION
# =====================
def fetch(url, headers):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        return res.text, res.status_code
    except:
        return None, None

# =====================
# EXTRACT FUNCTION
# =====================
def extract(html, pattern):
    match = re.search(pattern, html)
    return match.group(1) if match else "N/A"

# =====================
# AUTO TRY SYSTEM
# =====================
html = None
status = None

for url in urls:
    for headers in headers_list:

        print(f"[*] Trying {url}")

        html, status = fetch(url, headers)

        if html and len(html) > 2000 and "slardar" not in html.lower():
            print("[+] Got valid response")
            break

    if html and len(html) > 2000:
        break

# =====================
# CHECK RESULT
# =====================
if not html or len(html) < 2000 or "slardar" in html.lower():
    print("\n❌ Blocked by TikTok (WAF detected)")
    exit()

# =====================
# PARSE DATA
# =====================
user_id = extract(html, r'"id":"(\d+)"')
nickname = extract(html, r'"nickname":"([^"]+)"')
followers = extract(html, r'"followerCount":(\d+)')
following = extract(html, r'"followingCount":(\d+)')
videos = extract(html, r'"videoCount":(\d+)')
secuid = extract(html, r'"secUid":"([^"]+)"')

# =====================
# OUTPUT
# =====================
print("\n===== RESULT =====")
print("User ID:", user_id)
print("Nickname:", nickname)
print("Followers:", followers)
print("Following:", following)
print("Videos:", videos)
print("SecUID:", secuid)
print("\nStatus:", status)
