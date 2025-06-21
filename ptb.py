import sys
from tools import webcheck, genpass, banner, convertpdf, httpheaders, imginfo, dnslookup, mdnote, urlshort, whoislookup, banner

def main():
    banner. print_banner()
    if len(sys.argv) < 2:
        print("Kullanım: ptb <komut> [parametreler]")
        print("Komutlar: webcheck, genpass, convertpdf, mdnote, imginfo, urlshort, whois, dnslookup, httpheaders")
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "webcheck":
        if len(sys.argv) < 3:
            print("Kullanım: ptb webcheck <url>")
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

    elif cmd == "convertpdf":
        if len(sys.argv) < 3:
            print("Kullanım: ptb convertpdf <txt_dosya>")
            sys.exit(1)
        txtfile = sys.argv[2]
        convertpdf.convert_to_pdf(txtfile)

    elif cmd == "mdnote":
        if len(sys.argv) < 3:
            print("Kullanım: ptb mdnote <not_icerigi>")
            sys.exit(1)
        content = sys.argv[2]
        mdnote.create_note(content)

    elif cmd == "imginfo":
        if len(sys.argv) < 3:
            print("Kullanım: ptb imginfo <resim_dosyasi>")
            sys.exit(1)
        filepath = sys.argv[2]
        imginfo.image_info(filepath)

    elif cmd == "urlshort":
        if len(sys.argv) < 3:
            print("Kullanım: ptb urlshort <url>")
            sys.exit(1)
        url = sys.argv[2]
        urlshort.shorten_url(url)

    elif cmd == "whois":
        if len(sys.argv) < 3:
            print("Kullanım: ptb whois <domain>")
            sys.exit(1)
        domain = sys.argv[2]
        info = whoislookup.domain_info(domain)
        if info:
            print(info)
        else:
            print("Domain bilgisi alınamadı.")

    elif cmd == "dnslookup":
        if len(sys.argv) < 3:
            print("Kullanım: ptb dnslookup <domain>")
            sys.exit(1)
        domain = sys.argv[2]
        dnslookup.lookup(domain)

    elif cmd == "httpheaders":
        if len(sys.argv) < 3:
            print("Kullanım: ptb httpheaders <url>")
            sys.exit(1)
        url = sys.argv[2]
        httpheaders.fetch_headers(url)

    else:
        print(f"Bilinmeyen komut: {cmd}")
        print("Komutlar: webcheck, genpass, convertpdf, mdnote, imginfo, urlshort, whois, dnslookup, httpheaders")

if __name__ == "__main__":
    main()
