# PyToolbox

PyToolbox, geliştiriciler ve günlük kullanıcılar için hazırlanmış Python tabanlı kullanışlı bir CLI araçlar paketidir.

## Özellikler

- `webcheck`: Verilen web sitesinin erişilebilirliğini kontrol eder.
- `genpass`: Belirtilen uzunlukta güvenli rastgele parola oluşturur.
- İlerleyen sürümlerde daha fazla araç eklenecek.

## Kurulum

Bu projeyi kullanmak için Python 3 yüklü olmalıdır.

```bash
git clone https://github.com/KarapinarAhmet/Pytoolbox.git
cd Pytoolbox
python ptb.py <komut> [parametreler]

``` 
--- 

🔖 Sürüm

v0.1 – İlk sürüm, temel 6 modül içerir.

---

📚 Komutlar

🔍 webcheck

Bir web sitesinin çevrimiçi olup olmadığını kontrol eder.

python ptb.py webcheck https://example.com

---

🔐 genpass

Rastgele güçlü bir parola üretir.

python ptb.py genpass -l 16

---

📝 mdnote

Markdown formatında hızlı not alır. Notlar notes/ klasörüne kaydedilir.

python ptb.py mdnote "Bugün hava çok güzeldi."

--- 

🖼️ imginfo

Bir görsel dosyasının format, boyut ve mod bilgilerini gösterir.

python ptb.py imginfo foto.jpg

--- 

📄 convertpdf

.txt uzantılı bir metin dosyasını PDF'e dönüştürür.

python ptb.py convertpdf notlar.txt

---

🔗 urlshort

TinyURL API kullanarak uzun URL’yi kısaltır.

python ptb.py urlshort https://youtube.com/watch?v=xyz

---

🧾 Gereksinimler

requests

Pillow

fpdf


Hepsi requirements.txt dosyasına dahildir

---

👨‍💻 Geliştirici

Ahmet Karapınar
(https://github.com/Karapinarahmrt)

 💻 PROJE ADRESİ 
(https://github.com/Karapinarahmet/Pytoolbox)

---

📄 Lisans

MIT Lisansı – Açık kaynak, dilediğiniz gibi kullanabilirsiniz.

---
