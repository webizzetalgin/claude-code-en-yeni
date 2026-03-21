---
name: seo-content-generator
description: "Google Türkiye SERP analizi yaparak SEO uyumlu Türkçe içerik üretir. Kullanıcı bir veya birden fazla anahtar kelime verdiğinde bu skill tetiklenir. Tetikleyiciler: 'anahtar kelime', 'SEO içerik yaz', 'içerik üret', 'makale yaz', 'blog yazısı oluştur', 'Google analizi yap', 'SERP analizi', 'AI özeti analiz et', 'içerik oluştur', herhangi bir Türkçe anahtar kelime verilmesi. Çıktı olarak Word (.docx) formatında SEO içerik + Excel (.xlsx) formatında konu önerileri tablosu üretir. Bu skill her anahtar kelime bazlı içerik talebi için kullanılmalıdır — kullanıcı açıkça 'SEO' demese bile, bir konu hakkında içerik/makale/yazı istiyorsa bu skill tetiklenmelidir."
---

# SEO İçerik Üretici — Google Türkiye SERP Analizi ile

## Genel Bakış

Bu skill, kullanıcının verdiği anahtar kelime(ler) için Google Türkiye arama sonuçlarını derinlemesine analiz eder ve bu analizlere dayalı olarak SEO uyumlu, kapsamlı Türkçe içerik üretir. Çıktı olarak iki dosya verir:
1. **Word (.docx)** — Ana içerik dosyası
2. **Excel (.xlsx)** — Konuyla ilgisi olmayan ama yazılabilecek yeni konu önerileri

İçerik onaylandıktan sonra kullanıcının WordPress sitesine taslak olarak ekler.

## Dil ve Üslup

- Dil: Türkçe
- Üslup: SEO odaklı ve teknik
- Ton: Bilgilendirici, profesyonel, otoriter
- Kişi: Genel hitap (siz/sen duruma göre)

---

## İŞ AKIŞI — Adım Adım Uygula

Kullanıcı bir veya birden fazla anahtar kelime verdiğinde, aşağıdaki adımları SIRAyla uygula. Her adımı mutlaka tamamla, hiçbir adımı atlama.

### ADIM 1: Google Türkiye SERP Analizi

Verilen her anahtar kelime için aşağıdaki aramaları `web_search` tool ile yap:

```
Arama 1: "[anahtar kelime]" (Ana arama — AI özeti ve organik sonuçlar için)
Arama 2: "[anahtar kelime] nedir" (Diğer sorular / People Also Ask için)
Arama 3: "[anahtar kelime] nasıl" (Farklı soru varyasyonları için)
```

Her arama sonucunda şunları topla ve analiz et:

#### 1.1 AI Özeti Analizi
- AI özetinde verilen açıklamayı oku
- Açıklamanın yaklaşık kelime sayısını tespit et
- AI özetinin alt başlıklarını ve bahsettiği konuları listele
- AI özetinin hangi bilgileri öne çıkardığını belirle

#### 1.2 İlk 5 Organik Sonuç Analizi
İlk 5 sonucun her biri için `web_fetch` ile sayfayı aç ve şunları analiz et:
- Sayfanın toplam kelime sayısı (yaklaşık)
- Kullanılan alt başlık yapısı (H2, H3 hiyerarşisi)
- Yazım stili (teknik mi, sohbet mi, liste mi, paragraf mı)
- İçeriğin derinlik seviyesi

5 sonucun ortalamasını al → Bu, yazılacak içeriğin hedef kelime sayısını ve stilini belirler.

#### 1.3 "Diğer Sorular" (People Also Ask) Analizi
- İlk 4 soruyu kaydet
- Her soruya tıklayarak (yeni aramalar yaparak) açılan ek soruları da topla
- Toplamda en az 8-12 soru topla
- Bu sorulardan SADECE konuyla doğrudan ilgili olanları alt başlık olarak kullan
- Konuyla ilgisi olmayan soruları ayrı bir listeye al (Excel tablosu için)

#### 1.4 "Kullanıcıların Yaptığı Diğer Aramalar" Analizi
- Sayfanın altındaki ilgili aramalar bölümünü incele
- Konuyla ilgili olan ve henüz alt başlık olarak geçirmediğin konuları ekle

#### 1.5 Görseller Sekmesi Semantik Analizi
- Anahtar kelimeyi görseller sekmesinde arat:
  ```
  "[anahtar kelime] görseller"
  ```
- Görseller sekmesindeki üst kısımdaki filtre kutucuklarındaki (chip/tag) semantik anlamlı kelimeleri topla
- Bu kelimeleri içerikte doğal bir şekilde geçir (zoraki keyword stuffing yapma)

---

### ADIM 2: İçerik Planı Oluşturma

Analiz verilerini sentezle ve şu planı oluştur:

#### 2.1 Hedef Kelime Sayısı Belirleme
- İlk 5 sonucun ortalama kelime sayısını baz al
- Ortalamadan %10-20 fazla yaz (daha kapsamlı olmak için)

#### 2.2 Alt Başlık Yapısı Belirleme
- Kelime sayısına göre alt başlık adedini belirle:
  - 1000-1500 kelime → 4-6 alt başlık
  - 1500-2500 kelime → 6-10 alt başlık
  - 2500-4000 kelime → 10-15 alt başlık
  - 4000+ kelime → 15+ alt başlık

- Alt başlık kaynakları (öncelik sırasıyla):
  1. AI özeti alt başlıkları
  2. "Diğer Sorular" (People Also Ask) — konuyla ilgili olanlar
  3. "Kullanıcıların Yaptığı Diğer Aramalar" — konuyla ilgili olanlar
  4. Rakip içeriklerden çıkarılan ortak başlıklar

#### 2.3 Soru Formatındaki Alt Başlıklar İçin Kural
- Soru başlıklı alt başlıkların açıklamaları: **İlk cümle maksimum 30 kelime** olmalı
- İlk cümleden sonra yeni paragrafla detaylara geçilmeli
- Örnek format:
  ```
  ## [Anahtar kelime] Nedir?
  
  [Anahtar kelime], [30 kelimelik özet tanım cümlesi].
  
  [Yeni paragrafta detaylı açıklama devam eder...]
  ```

#### 2.4 Long-Tail Anahtar Kelime Kuralı (3+ Kelimelik Anahtar Kelimeler)

**KRİTİK KURAL:** Anahtar kelime 3, 4, 5 veya daha fazla kelimeden oluşuyorsa (long-tail keyword), içerikte genel tanımlara kesinlikle GİRME. Doğrudan konuyu anlat.

**Neden?** Long-tail anahtar kelimeyle arayan kişi zaten konunun ne olduğunu biliyordur. Genel tanıma ihtiyacı yoktur. Doğrudan spesifik bilgiye ulaşmak ister.

**Nasıl tespit edilir?**
- Anahtar kelimeyi kelime sayısına göre değerlendir
- 1-2 kelime → Normal akış (genel tanım verilebilir)
- 3+ kelime → Long-tail kuralı devreye girer

**Yapılmaması gereken (YANLIŞ):**
```
Anahtar kelime: "bebek odası dekorasyon fikirleri"

## Bebek Odası Dekorasyonu Nedir?
Bebek odası dekorasyonu, bebeğinizin odasını güzel ve fonksiyonel hale getirme sürecidir...
→ Bu YANLIŞ. Kullanıcı zaten bunu biliyor.
```

**Yapılması gereken (DOĞRU):**
```
Anahtar kelime: "bebek odası dekorasyon fikirleri"

## Renk Paleti Seçimi
Pastel tonlar 2024'te hâlâ en popüler tercih. Ancak son trend olarak...
→ Bu DOĞRU. Direkt konuya giriyor, pratik bilgi veriyor.
```

**Giriş paragrafı kuralı (long-tail için):**
- Giriş paragrafı kalsın ama çok kısa olsun (2-3 cümle)
- Kesinlikle "[Anahtar kelime], ... demektir/anlamına gelir" gibi tanım cümlesi içermemeli
- Bunun yerine konunun neden önemli olduğunu veya yazıda ne bulacaklarını söyle
- Örnek: "Bebek odası dekorasyon fikirlerinde 2024'ün en popüler trendlerini ve uygulamalı önerilerini bir araya getirdik. İşte bütçeye göre sıralanmış ilham kaynakları."

---

### ADIM 3: İçerik Yazımı

#### 3.1 Yazım Kuralları
- Üslup: SEO odaklı, teknik, bilgilendirici
- **Long-tail kontrol:** Anahtar kelime 3+ kelimeden oluşuyorsa → ADIM 2.4'teki kurallara uy. Genel tanımlara girme, direkt konuyu anlat.
- İlk paragraf: Anahtar kelimeyi ilk 100 kelime içinde doğal şekilde geçir
- İlk paragraf (long-tail için): 2-3 cümle, tanım içermemeli, konunun neden önemli olduğunu veya yazıda ne bulacaklarını söylemeli
- Her alt başlıkta anahtar kelimeyi veya varyasyonlarını doğal şekilde kullan
- Görseller sekmesinden toplanan semantik kelimeleri içeriğe serpiştir
- Rakip analizinden çıkan yazım stilini takip et (paragraf ağırlıklı mı, liste ağırlıklı mı vb.)
- Teknik terimleri açıklayıcı şekilde kullan
- Kısa ve uzun cümleleri dengeleyerek yaz
- Aktif cümle yapısını tercih et

#### 3.2 İçerik Yapısı
```
# [Ana Başlık — H1] (Anahtar kelimeyi içermeli)

[Giriş paragrafı — 100-150 kelime, anahtar kelime ilk cümlede]

## [Alt Başlık 1 — H2]
[İçerik...]

### [Varsa Alt-alt Başlık — H3]
[İçerik...]

## [Alt Başlık 2 — H2]
[İçerik...]

... (devam eder)

## Sonuç / Özet
[Kapanış paragrafı — anahtar kelimeyi tekrar geçir]
```

#### 3.3 SEO Kontrol Listesi (yazarken uygula)
- [ ] Anahtar kelime başlıkta var mı?
- [ ] Anahtar kelime ilk 100 kelimede var mı?
- [ ] Alt başlıklarda anahtar kelime varyasyonları var mı?
- [ ] Soru formatındaki başlıkların ilk cümlesi ≤30 kelime mi?
- [ ] Semantik kelimeler doğal şekilde geçiyor mu?
- [ ] Kelime sayısı hedefe uygun mu?
- [ ] Paragraflar çok uzun değil mi? (max 4-5 cümle per paragraf)
- [ ] Long-tail anahtar kelimeyse genel tanım yapılmamış mı? (ADIM 2.4)

#### 3.4 FAQ Schema (JSON-LD) Üretimi

İçerikteki soru formatındaki alt başlıklardan (People Also Ask kaynaklı olanlar) bir FAQ Schema oluştur.

**Kurallar:**
- En az 3, en fazla 8 soru-cevap çifti seç
- Sadece içerikte gerçekten cevaplanan soruları dahil et
- Cevaplar 150-300 karakter arası olmalı (Google'ın tercih ettiği uzunluk)
- Cevap, içerikteki ilgili bölümün özetlenmiş hali olmalı (birebir kopyalama)

**Format:**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Soru metni buraya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cevap metni buraya. 150-300 karakter arası."
      }
    },
    {
      "@type": "Question",
      "name": "İkinci soru metni?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "İkinci cevap metni."
      }
    }
  ]
}
</script>
```

**Çıktı:** FAQ Schema kodunu Word dosyasının en sonuna ayrı bir bölüm olarak ekle:
```
## FAQ Schema Kodu (WordPress'e Eklenecek)

Aşağıdaki kodu yazınızın HTML editöründe en alta veya Yoast/Rank Math'in "Head" bölümüne ekleyin:

[JSON-LD kodu buraya]
```

#### 3.5 İç Link (Internal Link) Önerileri

İçerik yazıldıktan sonra, kullanıcının mevcut sitesindeki diğer içeriklere iç link verilecek yerleri belirle.

**Adımlar:**
1. Kullanıcının site adresini biliyorsan (WordPress bilgileri alındıysa), `web_search` ile sitedeki ilgili sayfaları bul:
   ```
   site:kullanicisitesi.com [alt başlık konusu]
   ```
2. Site adresi henüz bilinmiyorsa, iç link önerilerini **"anchor text → önerilen hedef konu"** formatında Word dosyasına ekle. Kullanıcı daha sonra kendi sitesindeki ilgili sayfayı eşleştirir.

**Format (Word dosyasında ayrı bölüm olarak):**
```
## İç Link Önerileri

| # | Anchor Text (Bağlantı Metni) | Bulunduğu Alt Başlık | Önerilen Hedef Konu/Sayfa |
|---|-------------------------------|----------------------|---------------------------|
| 1 | "SSL sertifikası"            | Güvenlik Önlemleri   | SSL Sertifikası Nedir?    |
| 2 | "sayfa hızı optimizasyonu"   | Teknik SEO           | PageSpeed Rehberi         |
```

**Kurallar:**
- En az 3, en fazla 8 iç link önerisi yap
- Anchor text doğal olmalı (tam eşleşme anahtar kelime zorlaması yapma)
- Her alt başlıktan en fazla 2 iç link öner
- İç linkler içerikteki konuyla gerçekten ilgili olmalı, zoraki ekleme yapma

---

### ADIM 4: Word (.docx) Dosyası Oluşturma

**ÖNEMLİ: Önce `/mnt/skills/public/docx/SKILL.md` dosyasını oku ve oradaki talimatları izle.**

Word dosyası şu formatta olmalı:
- Sayfa boyutu: A4
- Font: Arial
- Başlık (H1): 16pt, Bold
- Alt başlık (H2): 14pt, Bold
- Alt-alt başlık (H3): 12pt, Bold
- Gövde metin: 11pt, Regular
- Satır aralığı: 1.5
- Paragraf arası boşluk: 6pt before, 6pt after

Dosya adı formatı: `[anahtar-kelime]-seo-icerik.docx`

---

### ADIM 5: Excel (.xlsx) Konu Önerileri Tablosu

**ÖNEMLİ: Önce `/mnt/skills/public/xlsx/SKILL.md` dosyasını oku ve oradaki talimatları izle.**

Konuyla ilgisi olmayan ama potansiyel içerik konusu olan sorular ve kelimeleri Excel tablosuna yaz.

Excel dosyası şu sütunları içermeli:

| Sütun | Açıklama |
|-------|----------|
| A: Konu/Soru | Konuyla ilgisi olmayan ama yazılabilecek konu |
| B: Kaynak | Nereden geldi (Diğer Sorular, İlgili Aramalar, Görseller vb.) |
| C: Tahmini Arama Hacmi | Düşük / Orta / Yüksek (tahmine dayalı) |
| D: Öncelik | 1-5 arası (1=en yüksek) |
| E: Not | Varsa ek notlar |

Dosya adı formatı: `[anahtar-kelime]-yeni-konular.xlsx`

---

### ADIM 6: Sonuçları Kullanıcıya Sunma ve Onay İsteme

Her iki dosyayı `/mnt/user-data/outputs/` dizinine kopyala ve `present_files` tool ile kullanıcıya sun.

Sunumda kısa bir özet ver:
- Hedeflenen kelime sayısı ve neden
- Kaç alt başlık kullanıldığı
- Hangi semantik kelimelerin içeriğe eklendiği
- Excel'de kaç potansiyel yeni konu önerisi olduğu

#### 6.1 İçerik Onayı İsteme (ZORUNLU)

Dosyaları sunduktan sonra kullanıcıdan **açık onay** iste. İçeriği WordPress'e yüklemeden ÖNCE mutlaka onay alınmalıdır.

Kullanıcıya şu şekilde sor:

```
İçeriği inceleyebilir misiniz? Değiştirmek veya düzeltmek istediğiniz yerler varsa belirtebilirsiniz.

İçerik uygunsa, WordPress sitenize taslak olarak yükleyebilirim.
Onaylıyor musunuz?
```

**Onay durumları:**
- **Kullanıcı "evet/onay/tamam/yükle" derse** → ADIM 7'ye geç
- **Kullanıcı düzeltme isterse** → İstenen değişiklikleri yap, dosyaları güncelle, tekrar sun ve tekrar onay iste
- **Kullanıcı "hayır/istemiyorum" derse** → WordPress yükleme adımını atla, süreci sonlandır

**KRİTİK: Kullanıcıdan açık onay almadan ASLA ADIM 7'ye geçme. Onay olmadan WordPress bilgilerini sorma.**

---

### ADIM 7: WordPress Site Bilgilerini Toplama

Kullanıcı içeriği onayladıktan sonra, WordPress sitesine yazıyı yüklemek için gerekli bilgileri topla.

#### 7.1 Gerekli Bilgileri İsteme

Kullanıcıdan şu bilgileri iste:

```
İçeriği WordPress sitenize taslak olarak yüklemem için aşağıdaki bilgilere ihtiyacım var:

1. WordPress site adresi (örn: https://siteniz.com)
2. WordPress kullanıcı adı
3. WordPress şifresi (veya uygulama şifresi)
```

**Uygulama şifresi tercihi:** Kullanıcıya mümkünse WordPress "Uygulama Şifresi" (Application Password) kullanmasını öner. Bu, ana şifreyi paylaşmaktan daha güvenlidir. Uygulama şifresi oluşturmak için:
- WordPress Yönetim Paneli → Kullanıcılar → Profil → Uygulama Şifreleri bölümünden oluşturulabilir.

#### 7.2 Bilgi Doğrulama

Bilgiler alındıktan sonra:
1. Site adresinin geçerli bir URL formatında olduğunu kontrol et (https:// ile başlamalı)
2. Kullanıcı adı ve şifre boş olmamalı
3. Eksik bilgi varsa tekrar sor

#### 7.3 Güvenlik Uyarısı

Bilgileri aldıktan sonra kullanıcıya şu uyarıyı göster:

```
⚠️ Güvenlik notu: Giriş bilgileriniz yalnızca bu işlem için kullanılacak ve 
saklanmayacaktır. İşlem tamamlandıktan sonra, güvenliğiniz için uygulama 
şifrenizi WordPress panelinizden silmenizi öneriyorum.
```

---

### ADIM 8: WordPress'e Yazıyı Taslak Olarak Ekleme

Kullanıcının verdiği bilgilerle WordPress REST API üzerinden yazıyı taslak olarak ekle.

#### 8.1 WordPress REST API ile Bağlantı

WordPress REST API endpoint'i:
```
POST {site_adresi}/wp-json/wp/v2/posts
```

Kimlik doğrulama: Basic Authentication (Base64 encoded kullanıcı_adı:şifre)

#### 8.2 Yazıyı Oluşturma

API'ye gönderilecek veri yapısı:

```python
import requests
import base64
import json

site_url = "{kullanıcının_verdiği_site_adresi}"
username = "{kullanıcı_adı}"
password = "{şifre}"

# Kimlik doğrulama
credentials = base64.b64encode(f"{username}:{password}".encode()).decode()

headers = {
    "Authorization": f"Basic {credentials}",
    "Content-Type": "application/json"
}

# İçeriği HTML formatına dönüştür
# Markdown → HTML dönüşümü yap (başlıklar, paragraflar, listeler)
post_data = {
    "title": "{H1 başlık}",
    "content": "{HTML formatında içerik}",
    "status": "draft",           # ZORUNLU: Her zaman taslak olarak ekle
    "categories": [],             # Boş bırak, kullanıcı sonra ayarlar
    "tags": []                    # Boş bırak, kullanıcı sonra ayarlar
}

response = requests.post(
    f"{site_url}/wp-json/wp/v2/posts",
    headers=headers,
    data=json.dumps(post_data)
)
```

#### 8.3 Markdown → HTML Dönüşümü Kuralları

İçeriği WordPress'e göndermeden önce Markdown'dan HTML'e dönüştür:

| Markdown | HTML |
|----------|------|
| `# Başlık` | `<h1>Başlık</h1>` |
| `## Alt Başlık` | `<h2>Alt Başlık</h2>` |
| `### Alt-alt Başlık` | `<h3>Alt-alt Başlık</h3>` |
| `Paragraf metni` | `<p>Paragraf metni</p>` |
| `**kalın**` | `<strong>kalın</strong>` |
| `*italik*` | `<em>italik</em>` |
| `- liste öğesi` | `<ul><li>liste öğesi</li></ul>` |
| `1. sıralı öğe` | `<ol><li>sıralı öğe</li></ol>` |

**NOT:** WordPress editörü Gutenberg blok yapısını kullanır. Mümkünse içeriği Gutenberg blok formatında gönder:
```html
<!-- wp:heading -->
<h2>Alt Başlık</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Paragraf içeriği burada yer alır.</p>
<!-- /wp:paragraph -->
```

#### 8.4 Hata Yönetimi

API yanıtına göre işlem yap:

| HTTP Kodu | Durum | Yapılacak İşlem |
|-----------|-------|-----------------|
| 201 | Başarılı | Yazı oluşturuldu, ADIM 9'a geç |
| 401 | Yetkisiz | Kullanıcı adı/şifre hatalı — bilgileri tekrar iste |
| 403 | Yasak | Kullanıcının yeterli yetkisi yok — admin yetkisi gerekebilir bilgisini ver |
| 404 | Bulunamadı | REST API aktif değil — kullanıcıya permalink ayarlarını kontrol etmesini söyle |
| 500 | Sunucu hatası | Sunucu sorunu — daha sonra tekrar denemesini öner |

Başarısız durumda kullanıcıya hatanın nedenini açıkla ve çözüm önerisinde bulun.

---

### ADIM 9: Yazıyı noindex/nofollow Olarak Ayarlama

Yazı başarıyla taslak olarak eklendikten sonra, SEO ayarlarını yap.

#### 9.1 Yoast SEO veya Rank Math Kontrolü

Önce sitede hangi SEO eklentisinin aktif olduğunu kontrol et:

```python
# Yoast SEO kontrolü
yoast_check = requests.get(
    f"{site_url}/wp-json/yoast/v1/get_head?url={site_url}",
    headers=headers
)

# Rank Math kontrolü
rankmath_check = requests.get(
    f"{site_url}/wp-json/rankmath/v1/getHead?url={site_url}",
    headers=headers
)
```

#### 9.2 noindex/nofollow Uygulama

**Yoast SEO aktifse:**
```python
# Post meta güncelleme
meta_data = {
    "meta": {
        "_yoast_wpseo_meta-robots-noindex": "1",    # noindex
        "_yoast_wpseo_meta-robots-nofollow": "1"     # nofollow
    }
}

requests.post(
    f"{site_url}/wp-json/wp/v2/posts/{post_id}",
    headers=headers,
    data=json.dumps(meta_data)
)
```

**Rank Math aktifse:**
```python
meta_data = {
    "meta": {
        "rank_math_robots": ["noindex", "nofollow"]
    }
}

requests.post(
    f"{site_url}/wp-json/wp/v2/posts/{post_id}",
    headers=headers,
    data=json.dumps(meta_data)
)
```

**Hiçbir SEO eklentisi yoksa:**
Kullanıcıya bilgi ver:
```
Sitenizde Yoast SEO veya Rank Math eklentisi tespit edilemedi. 
noindex/nofollow ayarını manuel yapmanız gerekecek:

Seçenek 1: Yoast SEO veya Rank Math kurun ve yazının SEO ayarlarından noindex/nofollow işaretleyin.
Seçenek 2: Yazının HTML'ine şu meta etiketi ekleyin:
<meta name="robots" content="noindex, nofollow">
```

#### 9.3 Durum Doğrulama

noindex/nofollow ayarlandıktan sonra, yazının durumunu doğrula:

```python
# Yazıyı tekrar çek ve meta değerlerini kontrol et
verify = requests.get(
    f"{site_url}/wp-json/wp/v2/posts/{post_id}",
    headers=headers
)
post = verify.json()

# Durum kontrolü
assert post["status"] == "draft", "Yazı taslak durumunda olmalı"
```

---

### ADIM 10: Son Rapor ve Tamamlama

Tüm işlemler tamamlandıktan sonra kullanıcıya son raporu sun:

#### 10.1 Başarılı Tamamlama Raporu

```
✅ İşlem tamamlandı! İşte özet:

📄 İçerik:
   - Başlık: [H1 başlık]
   - Kelime sayısı: [X] kelime
   - Alt başlık sayısı: [Y] adet

🌐 WordPress:
   - Yazı durumu: Taslak (Draft)
   - Yazı ID: [post_id]
   - Düzenleme linki: {site_url}/wp-admin/post.php?post={post_id}&action=edit
   - Robots: noindex, nofollow ✓

📊 Ek çıktılar:
   - Excel konu önerileri: [Z] adet yeni konu önerisi

⚠️ Hatırlatma:
   - Yazıyı yayınlamadan önce son bir kez gözden geçirin
   - Görselleri manuel olarak ekleyin
   - Kategori ve etiketleri belirleyin
   - Hazır olduğunuzda noindex/nofollow ayarını kaldırın ve yayınlayın
   - Güvenliğiniz için uygulama şifresini WordPress panelinizden silin
```

#### 10.2 Başarısız Tamamlama Raporu

WordPress yükleme başarısız olduysa:

```
📄 İçerik dosyalarınız hazır:
   - Word dosyası: [dosya adı].docx ✅
   - Excel konu önerileri: [dosya adı].xlsx ✅

❌ WordPress yükleme başarısız oldu:
   - Hata: [hata açıklaması]
   - Çözüm önerisi: [çözüm]

İçeriği manuel olarak WordPress panelinizden ekleyebilirsiniz:
1. {site_url}/wp-admin adresine gidin
2. Yazılar → Yeni Yazı Ekle
3. Word dosyasındaki içeriği kopyala-yapıştır yapın
4. Taslak olarak kaydedin
5. SEO ayarlarından noindex/nofollow işaretleyin
```

---

## ÖNEMLİ NOTLAR

1. **Ağ bağlantısı yoksa**: Kullanıcıya ağ erişiminin kapalı olduğunu bildir ve analiz yapılamayacağını söyle. Ağ ayarlarını güncellemelerini öner. WordPress yükleme adımı da ağ erişimi gerektirir.

2. **Birden fazla anahtar kelime verilirse**: Her anahtar kelime için ayrı analiz yap ama tek bir içerik belgesi oluştur (eğer konular ilişkiliyse) veya ayrı belgeler oluştur (eğer konular farklıysa).

3. **İçerik tekrarından kaçın**: Aynı bilgiyi farklı alt başlıklarda tekrarlama. Her bölüm yeni değer katmalı.

4. **Doğal dil kullan**: SEO için yazıyorsun ama insan için yazıyorsun. Anahtar kelime doldurmacası (keyword stuffing) yapma.

5. **Güncel bilgi kullan**: web_search sonuçlarındaki en güncel bilgileri öncelikle kullan.

6. **Telif hakkına dikkat**: Rakip sitelerden doğrudan kopya yapma. Bilgiyi kendi cümlelerinle yeniden yaz.

7. **WordPress güvenliği**: Kullanıcının giriş bilgilerini ASLA logla, sakla veya başka amaçla kullanma. İşlem tamamlandıktan sonra bilgileri bellekte tutma.

8. **Her zaman taslak**: WordPress'e eklenen yazılar MUTLAKA "draft" (taslak) durumunda olmalı. Asla doğrudan yayınlama ("publish" durumuna alma).

9. **Onay zorunlu**: İçeriği WordPress'e yüklemeden ÖNCE mutlaka kullanıcıdan açık onay al. Onaysız yükleme yapma.

---

## HIZLI BAŞVURU — Araç Kullanım Sırası

```
 1. web_search    → SERP analizi (AI özeti, organik sonuçlar)
 2. web_fetch     → İlk 5 sonucun detaylı analizi
 3. web_search    → "Diğer Sorular" varyasyonları
 4. web_search    → İlgili aramalar / görseller semantik analizi
 5. docx skill    → Word dosyası oluşturma
 6. xlsx skill    → Excel konu tablosu oluşturma
 7. present_files → Dosyaları kullanıcıya sunma
 8. [ONAY BEKLE]  → Kullanıcı içeriği onaylayana kadar dur
 9. [BİLGİ AL]    → WordPress site adresi, kullanıcı adı, şifre
10. requests/API  → WordPress REST API ile yazıyı taslak olarak ekle
11. requests/API  → noindex/nofollow ayarını uygula
12. [SON RAPOR]   → Kullanıcıya tamamlama raporu sun
```

---

## ORTAM GEREKSİNİMLERİ

Bu skill'in tüm adımlarını çalıştırabilmesi için:

| Gereksinim | Adımlar | Not |
|------------|---------|-----|
| `web_search` tool | ADIM 1 | SERP analizi için |
| `web_fetch` tool | ADIM 1 | Rakip site analizi için |
| Ağ erişimi (egress) | ADIM 1, 8, 9 | Google aramaları ve WordPress API için |
| `docx` skill | ADIM 4 | Word dosyası üretimi için |
| `xlsx` skill | ADIM 5 | Excel dosyası üretimi için |
| `present_files` tool | ADIM 6 | Dosya sunumu için |
| `requests` (Python) | ADIM 8, 9 | WordPress API çağrıları için |

**Ağ erişimi kapalıysa:** ADIM 1-6 arası çalıştırılabilir (eğer web_search tool mevcutsa). ADIM 7-9 ağ erişimi olmadan çalışmaz — bu durumda kullanıcıya dosyaları ver ve manuel yükleme talimatlarını sun.
