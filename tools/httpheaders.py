# tools/httpheaders.py
import requests

def fetch_headers(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        print(f"\n🔍 {url} için HTTP Header Bilgileri:\n")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
