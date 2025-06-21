import requests

def shorten_url(url):
    try:
        response = requests.get("http://tinyurl.com/api-create.php", params={"url": url})
        response.raise_for_status()
        short_url = response.text.strip()
        if short_url.startswith("http"):
            print(f"Kısaltılmış URL: {short_url}")
        else:
            print("Beklenmedik cevap alındı:", short_url)
    except Exception as e:
        print(f"Hata oluştu: {e}")
