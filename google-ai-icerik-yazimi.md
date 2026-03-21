---
name: seo-content-generator
description: "Google Türkiye SERP analizi yaparak SEO uyumlu Türkçe içerik üretir. Kullanıcı bir veya birden fazla anahtar kelime verdiğinde bu skill tetiklenir. Tetikleyiciler: 'anahtar kelime', 'SEO içerik yaz', 'içerik üret', 'makale yaz', 'blog yazısı oluştur', 'Google analizi yap', 'SERP analizi', 'AI özeti analiz et', 'içerik oluştur', herhangi bir Türkçe anahtar kelime verilmesi. Çıktı olarak Word (.docx) formatında SEO içerik + Excel (.xlsx) formatında konu önerileri tablosu üretir. Bu skill her anahtar kelime bazlı içerik talebi için kullanılmalıdır — kullanıcı açıkça 'SEO' demese bile, bir konu hakkında içerik/makale/yazı istiyorsa bu skill tetiklenmelidir."
---

# SEO İçerik Üretici — Google Türkiye SERP Analizi ile

## Genel Bakış

Bu skill, kullanıcının verdiği anahtar kelime(ler) için Google Türkiye arama sonuçlarını derinlemesine analiz eder ve bu analizlere dayalı olarak SEO uyumlu, kapsamlı Türkçe içerik üretir. Çıktı olarak iki dosya verir:
1. **Word (.docx)** — Ana içerik dosyası
2. **Excel (.xlsx)** — Konuyla ilgisi olmayan ama yazılabilecek yeni konu önerileri

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

---

### ADIM 3: İçerik Yazımı

#### 3.1 Yazım Kuralları
- Üslup: SEO odaklı, teknik, bilgilendirici
- İlk paragraf: Anahtar kelimeyi ilk 100 kelime içinde doğal şekilde geçir
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

### ADIM 6: Sonuçları Kullanıcıya Sunma

Her iki dosyayı `/mnt/user-data/outputs/` dizinine kopyala ve `present_files` tool ile kullanıcıya sun.

Sunumda kısa bir özet ver:
- Hedeflenen kelime sayısı ve neden
- Kaç alt başlık kullanıldığı
- Hangi semantik kelimelerin içeriğe eklendiği
- Excel'de kaç potansiyel yeni konu önerisi olduğu

---

## ÖNEMLİ NOTLAR

1. **Ağ bağlantısı yoksa**: Kullanıcıya ağ erişiminin kapalı olduğunu bildir ve analiz yapılamayacağını söyle. Ağ ayarlarını güncellemelerini öner.

2. **Birden fazla anahtar kelime verilirse**: Her anahtar kelime için ayrı analiz yap ama tek bir içerik belgesi oluştur (eğer konular ilişkiliyse) veya ayrı belgeler oluştur (eğer konular farklıysa).

3. **İçerik tekrarından kaçın**: Aynı bilgiyi farklı alt başlıklarda tekrarlama. Her bölüm yeni değer katmalı.

4. **Doğal dil kullan**: SEO için yazıyorsun ama insan için yazıyorsun. Anahtar kelime doldurmacası (keyword stuffing) yapma.

5. **Güncel bilgi kullan**: web_search sonuçlarındaki en güncel bilgileri öncelikle kullan.

6. **Telif hakkına dikkat**: Rakip sitelerden doğrudan kopya yapma. Bilgiyi kendi cümlelerinle yeniden yaz.

---

## HIZLI BAŞVURU — Araç Kullanım Sırası

```
1. web_search  → SERP analizi (AI özeti, organik sonuçlar)
2. web_fetch   → İlk 5 sonucun detaylı analizi
3. web_search  → "Diğer Sorular" varyasyonları
4. web_search  → İlgili aramalar / görseller semantik analizi
5. docx skill  → Word dosyası oluşturma
6. xlsx skill  → Excel konu tablosu oluşturma
7. present_files → Dosyaları kullanıcıya sunma
```
