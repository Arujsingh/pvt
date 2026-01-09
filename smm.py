import time
import requests  # pip install requests

URL = "https://youtu.be/iq2iGMtpF58?si=Of_FLZAQYTJpQ0_F"

def hit_url_times(n: int, delay_seconds: float = 0.1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    for i in range(n):
        try:
            r = requests.get(URL, headers=headers, timeout=5)
            print(f"{i+1}: {r.status_code}")
        except Exception as e:
            print(f"{i+1}: error -> {e}")
        time.sleep(delay_seconds)

if __name__ == "__main__":
    hit_url_times(10, delay_seconds=0.2)  # small, controlled test
