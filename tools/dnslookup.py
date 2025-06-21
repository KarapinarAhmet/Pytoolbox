# tools/dnslookup.py
import dns.message
import dns.query
import dns.rdatatype

def lookup(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    print(f"\n🔍 {domain} için DNS Kayıtları:\n")

    for rtype in record_types:
        try:
            query = dns.message.make_query(domain, getattr(dns.rdatatype, rtype))
            response = dns.query.udp(query, '8.8.8.8', timeout=5)

            print(f"🔸 {rtype} Kayıtları:")
            for answer in response.answer:
                for item in answer.items:
                    print(f"   ➤ {item.to_text()}")
        except Exception as e:
            print(f"   ⚠️ {rtype} sorgusu başarısız: {e}")
        print()
