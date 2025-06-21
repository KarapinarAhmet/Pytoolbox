# tools/whoislookup.py
import whois

def domain_info(domain):
    try:
        w = whois.whois(domain)
        print(f"\n📄 Alan Adı Bilgileri: {domain}\n")
        print(f"🔹 Alan Adı: {w.domain_name}")
        print(f"🔹 Kayıt Eden: {w.registrar}")
        print(f"🔹 Kayıt Tarihi: {w.creation_date}")
        print(f"🔹 Bitiş Tarihi: {w.expiration_date}")
        print(f"🔹 Güncelleme Tarihi: {w.updated_date}")
        print(f"🔹 DNS Sunucuları: {w.name_servers}")
        print(f"🔹 Ülke: {w.country}")
        print(f"🔹 E-posta: {w.emails}")
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
