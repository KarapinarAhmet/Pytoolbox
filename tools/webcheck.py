import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} erişilebilir.")
        else:
            print(f"{url} erişilemiyor, durum kodu: {response.status_code}")
    except Exception as e:
        print(f"{url} kontrol edilirken hata oluştu: {e}")
