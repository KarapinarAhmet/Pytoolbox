import sys
from tools import webcheck, genpass

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python ptb.py <komut> [parametreler]")
        print("Komutlar: webcheck, genpass")
        sys.exit(1)
    
    cmd = sys.argv[1].lower()

    if cmd == "webcheck":
        if len(sys.argv) < 3:
            print("Kullanım: python ptb.py webcheck <url>")
            sys.exit(1)
        url = sys.argv[2]
        webcheck.check_website(url)
    
    elif cmd == "genpass":
        length = 12
        if len(sys.argv) > 3 and sys.argv[2] == "-l":
            try:
                length = int(sys.argv[3])
            except ValueError:
                print("Geçersiz uzunluk değeri, varsayılan 12 kullanılacak.")
        genpass.generate_password(length)
    
    else:
        print(f"Bilinmeyen komut: {cmd}")
        print("Komutlar: webcheck, genpass")

if __name__ == "__main__":
    main()
