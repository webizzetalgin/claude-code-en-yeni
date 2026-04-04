---
name: wp-embeddable-json
description: >
  Referans bir web sitesi URL'sinden tasarım dilini analiz edip, WordPress Gutenberg blok 
  editörüne uyumlu JSON formatında sayfa çıktısı üret. URL'yi web_fetch ile çekerek tasarımı 
  analiz eder. Çıktı, WordPress REST API veya Starter Templates JSON import formatında olur — 
  iç içe konteynerler, grup blokları ve gelişmiş düzen yapılarıyla estetik, katmanlı tasarımlar 
  üretir. Anahtar kelimeler: "WordPress JSON", "WP JSON import", "Starter Templates", "Spectra 
  blok", "iç içe konteyner", "WordPress sayfa tasarımı", "referans URL", "tasarım kopyala", 
  "JSON çıktı", "blok editörü", "Gutenberg JSON", "sayfa şablonu", "bu siteye benzer", 
  "bu URL gibi yap".
---

# WordPress JSON Sayfa Üretici — URL Referanslı, İç İçe Konteyner Destekli

Referans bir web sitesinin URL'sinden tasarım dilini analiz edip, WordPress blok editörüne
(Gutenberg) doğrudan import edilebilecek JSON formatında, iç içe konteyner yapılarıyla
estetik sayfa çıktısı üret.

---

## İçindekiler

1.  [Bu Skill Ne Zaman Tetiklenir](#bu-skill-ne-zaman-tetiklenir)
2.  [Tasarım Felsefesi](#tasarım-felsefesi)
3.  [Adım Adım İş Akışı](#adım-adım-iş-akışı)
4.  [JSON Çıktı Formatı ve Blok Yapısı](#json-çıktı-formatı)
5.  [İç İçe Konteyner Tasarım Sistemi](#iç-içe-konteyner-sistemi)
6.  [WordPress Blok Türleri Referansı](#blok-türleri-referansı)
7.  [Tasarım Sadakati Rehberi](#tasarım-sadakati-rehberi)
8.  [İçerik Yerleştirme Protokolü](#içerik-yerleştirme-protokolü)
9.  [Çıktı Yapısı Şablonu](#çıktı-yapısı-şablonu)
10. [Kalite Kontrol Listesi](#kalite-kontrol-listesi)
11. [Sık Yapılan Hatalar ve Düzeltmeleri](#sık-yapılan-hatalar)
12. [Son Çıktı Protokolü](#son-çıktı-protokolü)

---

## Bu Skill Ne Zaman Tetiklenir

- Kullanıcı bir referans web sitesi URL'si paylaşır ve benzer tasarımda sayfa ister
- Çıktı WordPress blok editörüne JSON olarak import edilecektir
- Kullanıcı WordPress JSON import, Starter Templates, Spectra blok veya Gutenberg'den bahseder
- Kullanıcı iç içe konteyner, katmanlı düzen, gelişmiş blok yapısı ister
- Anahtar kelimeler: "WordPress JSON", "WP JSON", "bu siteye benzer", "bu URL gibi",
  "Gutenberg import", "blok editörü JSON", "Starter Templates JSON", "iç içe konteyner"

**ÖNEMLİ:** Bu skill referans URL'nin birebir kopyasını DEĞİL — o tasarımın dilini,
ritmini ve estetiğini kullanarak YENİ bir sayfa üretir.

---

## Tasarım Felsefesi {#tasarım-felsefesi}

Bu skill'in ürettiği çıktı, deneyimli bir frontend uzmanının WordPress'te oluşturduğu
profesyonel bir sayfa gibi görünmelidir.

### Yapay Zeka Estetiğinden Kaçınma Kuralları

```
YASAK — Tipik AI çıktısı belirtileri:
  ✗ Her yerde aynı mor-mavi gradient
  ✗ Simetrik, robotik, tekdüze grid yapıları
  ✗ Abartılı gölgeler ve parlama efektleri
  ✗ İçerikle alakasız dekoratif öğeler
  ✗ Her bölümde aynı kart tasarımının tekrarı
  ✗ Anlamsız hover efektleri
  ✗ Her şeyin yuvarlak köşeli kutular içinde olması
  ✗ Gereksiz animasyonlar
  ✗ Düz, tek katmanlı düzenler (sadece ardışık bloklar)
```

### Uzman Tasarımcı Kalitesi Kuralları

```
ZORUNLU — Profesyonel uzman dokunuşu:
  ✓ Referans tasarıma birebir sadakat
  ✓ İç içe konteynerlerle derinlik ve katman hissi
  ✓ Kasıtlı ve anlamlı beyaz alan (white space) kullanımı
  ✓ Tutarlı ama monoton olmayan görsel ritim
  ✓ İçeriğe uygun, bağlamsal tipografi seçimleri
  ✓ Detaylara özen: satır yüksekliği, harf aralığı, ince kenarlıklar
  ✓ Arka plan katmanları: dış konteyner bg + iç konteyner bg + kart bg
  ✓ Asimetrik düzenlerden korkmamak (referans gerektiriyorsa)
  ✓ Mikro-detaylar: ince ayırıcı çizgiler, accent renkli küçük vurgular
  ✓ İçerik hiyerarşisinde net basamaklar
```

### Tasarım Kararları Hiyerarşisi

1. **Referans tasarım ne yapıyorsa → onu yap** (birincil kaynak)
2. **Referansta yoksa → sektör standartlarına bak**
3. **Sektör standardı da belirsizse → minimal ve temiz tut**

**ASLA kendi başına süsleme ekleme.** Referansta olmayan dekoratif öğe eklenmez.

---

## Adım Adım İş Akışı

### Faz 1: URL'yi Çek ve Analiz Et

Kullanıcının paylaştığı URL'yi `web_fetch` ile çek:

```
1. web_fetch ile referans URL'nin HTML içeriğini al
2. CSS dosyalarının URL'lerini bul ve onları da web_fetch ile çek
3. Sayfanın genel yapısını, bölümlerini ve bileşenlerini analiz et
```

Her öğeyi incele:

| Analiz Hedefi | Ne Çıkarılacak |
|---------------|----------------|
| HTML yapısı | Bölüm düzeni, konteyner iç içeliği, sınıf adlandırma, semantik hiyerarşi |
| CSS | Renk paleti, font aileleri, boşluk sistemi, grid/flex desenleri, hover durumları, gölgeler, border-radius, responsive kırılma noktaları |
| Görsel katmanlar | Arka plan renkleri/gradientleri, overlay'ler, iç içe konteyner arka planları |
| Bileşen desenleri | Kartlar, butonlar, listeler, özellik blokları, CTA alanları |
| Derinlik yapısı | Kaç katman konteyner iç içe geçmiş, hangi seviyede hangi stil uygulanmış |

**Sayfayı BAŞTAN SONA analiz et.** Göz gezdirme YASAK.

### Faz 2: Tasarım Token Haritası Oluştur

JSON üretmeden ÖNCE bu token'ları belgele:

```
═══════════════════════════════════════════════
REFERANSTAN ÇIKARILAN TASARIM TOKEN'LARI
═══════════════════════════════════════════════

RENK PALETİ:
  Birincil (Primary):       #______
  İkincil (Secondary):      #______
  Vurgu (Accent):           #______
  Metin Birincil:           #______
  Metin İkincil:            #______
  Arka Plan Katman 1:       #______ (dış konteyner / sayfa arka planı)
  Arka Plan Katman 2:       #______ (iç konteyner / bölüm arka planı)
  Arka Plan Katman 3:       #______ (kart / yüzey arka planı)
  Kenarlık Rengi:           #______
  Gradient (varsa):         ______ → ______

TİPOGRAFİ:
  Başlık Fontu:     '________', ________
  Gövde Fontu:      '________', ________
  H1:  __px | Ağırlık: __ | Satır Yüksekliği: __
  H2:  __px | Ağırlık: __ | Satır Yüksekliği: __
  H3:  __px | Ağırlık: __ | Satır Yüksekliği: __
  Gövde: __px | Ağırlık: __ | Satır Yüksekliği: __

BOŞLUKLAR:
  Bölüm Padding (Masaüstü):   __px üst / __px alt
  Bölüm Padding (Mobil):      __px üst / __px alt
  İçerik Boşluğu (grid/flex): __px
  Kart İç Padding:            __px
  Konteyner İç İçe Padding:   __px (dış) → __px (iç)

KONTEYNER DERECELENMESİ:
  Seviye 1 (Dış):   Genişlik: ____ | Padding: __px | Arka Plan: #______
  Seviye 2 (Orta):  Genişlik: ____ | Padding: __px | Arka Plan: #______
  Seviye 3 (İç):    Genişlik: ____ | Padding: __px | Arka Plan: #______

DEKORATİF:
  Border Radius:    __px (kartlar) / __px (butonlar)
  Box Shadow:       ______________________________
  Ayırıcı Stili:    ______________________________
═══════════════════════════════════════════════
```

### Faz 3: JSON Yapısını Üret

Aşağıdaki format kurallarına uyarak WordPress blok editörü JSON'u oluştur.

---

## JSON Çıktı Formatı ve Blok Yapısı {#json-çıktı-formatı}

Çıktı, WordPress blok editörünün anlayacağı **blok serileştirme (block serialization)**
formatında JSON dosyasıdır.

### Temel JSON Yapısı

```json
{
  "title": "Sayfa Başlığı",
  "status": "draft",
  "content": {
    "raw": "<!-- WordPress blok içeriği buraya gelir -->"
  },
  "template": "",
  "meta": {
    "_starter_page_template": "blank"
  }
}
```

**`content.raw` alanı**, WordPress blok serileştirme formatında HTML string içerir.
Bu, blok yorumları (`<!-- wp:block-name -->`) ile sarılmış HTML'dir.

### Blok Serileştirme Formatı

WordPress her bloğu şu formatta saklar:

```html
<!-- wp:block-name {"attribute":"value"} -->
<div class="wp-block-name">İçerik</div>
<!-- /wp:block-name -->
```

İç içe bloklar:

```html
<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group">
  <!-- wp:heading {"level":2} -->
  <h2 class="wp-block-heading">Başlık</h2>
  <!-- /wp:heading -->

  <!-- wp:paragraph -->
  <p>Metin içeriği</p>
  <!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
```

### KRİTİK FORMAT KURALLARI

1. **`content.raw` değeri tek bir string olmalıdır** — JSON escape ile düzgün yazılmalı
2. **Her blok açma ve kapama yorumlarıyla sarılmalıdır**
3. **Blok özellikleri (attributes) JSON nesnesi olarak yorum içine yazılır**
4. **İç içe bloklar fiziksel olarak parent bloğun HTML'i içinde yer alır**
5. **Boş satırlar bloklar arasında `\n\n` ile ayrılır**

---

## İç İçe Konteyner Tasarım Sistemi {#iç-içe-konteyner-sistemi}

WordPress'in hazır Group, Cover, Columns bloklarını iç içe kullanarak
estetik, katmanlı tasarımlar üret. **Düz, tek katmanlı blok dizilimi YASAKTIR.**

### Katmanlı Mimari Prensibi

Her bölüm minimum 2, ideal 3 katman derinliğinde olmalıdır:

```
KATMAN 1 — Dış Sarmalayıcı (wp:group, full-width)
│  Arka plan rengi, gradient veya görsel
│  Tam genişlik (alignfull)
│
├── KATMAN 2 — İçerik Konteyneri (wp:group, constrained)
│   │  max-width ile sınırlı, ortalanmış
│   │  İç padding ile nefes alanı
│   │
│   ├── KATMAN 3a — İçerik Grubu (wp:columns veya wp:group)
│   │   │  Grid/flex düzeni
│   │   │
│   │   ├── wp:column → içerik blokları
│   │   └── wp:column → içerik blokları
│   │
│   └── KATMAN 3b — Kart Grubu (wp:group)
│       │  Arka plan, gölge, radius ile kart görünümü
│       │
│       └── İç içerik blokları
```

### Dış Sarmalayıcı Deseni (Katman 1)

```html
<!-- wp:group {"align":"full","style":{"color":{"background":"#f8f9fa"},"spacing":{"padding":{"top":"80px","bottom":"80px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#f8f9fa;padding-top:80px;padding-bottom:80px;padding-left:24px;padding-right:24px">

  <!-- İç konteyner ve içerikler buraya -->

</div>
<!-- /wp:group -->
```

### İçerik Konteyneri Deseni (Katman 2)

```html
<!-- wp:group {"style":{"spacing":{"padding":{"top":"40px","bottom":"40px","left":"40px","right":"40px"}},"border":{"radius":"16px"},"color":{"background":"#ffffff"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-background" style="background-color:#ffffff;padding-top:40px;padding-bottom:40px;padding-left:40px;padding-right:40px;border-radius:16px">

  <!-- Başlık, metin ve alt gruplar buraya -->

</div>
<!-- /wp:group -->
```

### Kart Deseni (Katman 3)

```html
<!-- wp:group {"style":{"spacing":{"padding":{"top":"32px","bottom":"32px","left":"32px","right":"32px"}},"border":{"radius":"12px"},"color":{"background":"#ffffff"},"shadow":"0 2px 12px rgba(0,0,0,0.08)"},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-background" style="background-color:#ffffff;padding-top:32px;padding-bottom:32px;padding-left:32px;padding-right:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08)">

  <!-- Kart içeriği -->

</div>
<!-- /wp:group -->
```

### Columns ile Yan Yana Düzen

```html
<!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"32px"}}}} -->
<div class="wp-block-columns">

  <!-- wp:column {"width":"60%"} -->
  <div class="wp-block-column" style="flex-basis:60%">
    <!-- Sol sütun içeriği -->
  </div>
  <!-- /wp:column -->

  <!-- wp:column {"width":"40%"} -->
  <div class="wp-block-column" style="flex-basis:40%">
    <!-- Sağ sütun içeriği -->
  </div>
  <!-- /wp:column -->

</div>
<!-- /wp:columns -->
```

### Cover Bloğu ile Zengin Arka Plan

```html
<!-- wp:cover {"overlayColor":"black","minHeight":500,"isDark":true,"align":"full","style":{"spacing":{"padding":{"top":"100px","bottom":"100px"}}}} -->
<div class="wp-block-cover alignfull is-dark" style="min-height:500px;padding-top:100px;padding-bottom:100px">
  <span aria-hidden="true" class="wp-block-cover__background has-background-dim"></span>
  <div class="wp-block-cover__inner-container">

    <!-- Cover içeriği — yine iç içe group ile sarılabilir -->

  </div>
</div>
<!-- /wp:cover -->
```

### İç İçe Derinlik Kuralları

```
ZORUNLU:
  ✓ Her bölümde minimum 2 katman konteyner (dış + iç)
  ✓ Kart içeren bölümlerde minimum 3 katman (dış + iç + kart)
  ✓ Farklı arka plan renkleriyle katmanlar arası kontrast
  ✓ Her katmanda uygun padding ile nefes alanı
  ✓ Border-radius ile yumuşak köşeler (referansa uygun)

YASAK:
  ✗ Düz, tek katmanlı ardışık blok dizilimi
  ✗ Tüm bölümlerde aynı arka plan rengi
  ✗ Padding'siz sıkışık konteynerler
  ✗ İç içe konteyner kullanmadan sadece columns ile düzen
  ✗ Her bölümde aynı katman yapısı (monotonluk)
```

---

## WordPress Blok Türleri Referansı {#blok-türleri-referansı}

### Yapısal Bloklar (Konteyner Oluşturanlar)

| Blok | Kullanım | Önemli Özellikler |
|------|----------|-------------------|
| `wp:group` | Genel konteyner, katman oluşturma | `layout.type`: `constrained`, `flex`, `grid`; arka plan, padding, radius, gölge |
| `wp:columns` | Yan yana sütunlar | `isStackedOnMobile`: true/false; sütun genişlikleri |
| `wp:column` | Tek sütun (columns içinde) | `width`: yüzde veya px; `verticalAlignment` |
| `wp:cover` | Arka plan görselli/renkli bölüm | `overlayColor`, `minHeight`, `dimRatio` |

### İçerik Blokları

| Blok | Kullanım | Önemli Özellikler |
|------|----------|-------------------|
| `wp:heading` | Başlıklar (h1-h6) | `level`, `textAlign`, `style.typography`, `style.color` |
| `wp:paragraph` | Paragraf metni | `align`, `style.typography.fontSize`, `style.color.text` |
| `wp:image` | Görsel | `url`, `alt`, `sizeSlug`, `align`, `width`, `height` |
| `wp:buttons` | Buton grubu | `layout.justifyContent` |
| `wp:button` | Tek buton | `backgroundColor`, `textColor`, `style.border.radius`, `url` |
| `wp:list` | Liste | `ordered`: true/false |
| `wp:separator` | Ayırıcı çizgi | `style`, `className` (is-style-wide, is-style-dots) |
| `wp:spacer` | Boşluk | `height` |
| `wp:html` | Özel HTML | Serbest HTML+CSS+JS — karmaşık özel bileşenler için |

### Gelişmiş Düzen Özellikleri

**Group Layout Tipleri:**
```json
{"layout": {"type": "constrained"}}
{"layout": {"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between"}}
{"layout": {"type": "grid", "columnCount": 3}}
```

**Spacing (Boşluk) Sistemi:**
```json
{
  "style": {
    "spacing": {
      "padding": {"top": "60px", "bottom": "60px", "left": "30px", "right": "30px"},
      "margin": {"top": "0", "bottom": "0"},
      "blockGap": "24px"
    }
  }
}
```

**Tipografi Sistemi:**
```json
{
  "style": {
    "typography": {
      "fontSize": "18px",
      "fontFamily": "\"Inter\", sans-serif",
      "fontWeight": "600",
      "lineHeight": "1.5",
      "letterSpacing": "0.02em",
      "textTransform": "uppercase"
    }
  }
}
```

**Renk ve Arka Plan:**
```json
{
  "style": {
    "color": {
      "background": "#f8f9fa",
      "text": "#1a1a2e",
      "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    }
  }
}
```

**Kenarlık ve Gölge:**
```json
{
  "style": {
    "border": {
      "radius": "16px",
      "width": "1px",
      "color": "#e2e8f0",
      "style": "solid"
    },
    "shadow": "0 4px 20px rgba(0,0,0,0.08)"
  }
}
```

---

## Tasarım Sadakati Rehberi

### Renk ve Palet
- Referans CSS'ten BİREBİR hex değerlerini çıkar
- Yaklaşık değer KULLANMA — tam değerleri kullan
- İç içe konteyner katmanlarında arka plan renk geçişlerini koru

### Tipografi
- HER metin seviyesi için font ailesi, ağırlık, boyut, satır yüksekliğini eşle
- Gerekli Google Fonts listesini kullanıcıya bildir

### Boşluk ve Ritim
- Bölüm padding'ini tam olarak eşle
- Konteyner katmanları arasındaki padding farkını koru
- blockGap değerlerini referansa göre ayarla

### Katman Derinliği
- Referanstaki konteyner iç içeliğini taklit et
- Arka plan renk geçişlerini (koyu → açık → beyaz) koru
- Gölge derinliklerini katmana göre ayarla

---

## İçerik Yerleştirme Protokolü

**KRİTİK — İÇERİK SADAKAT KURALI:**
Kullanıcının verdiği yazılar haricinde ekstradan herhangi bir yazı YAZMA ve alt başlık ATMA.
İçerik birebir kullanıcıdan gelir, senin görevin yalnızca bu içeriği referans tasarımın
görsel diline ve iç içe konteyner yapısına uygun şekilde yerleştirmektir.

### Bölüm Eşleme Stratejisi

```
Kullanıcı İçeriği       →  JSON Blok Yapısı
─────────────────────────────────────────────────────────────
1. Bölüm (Hero)         →  wp:cover veya wp:group(full) > wp:group(constrained)
2. Bölüm (Özellikler)   →  wp:group(full,bg) > wp:group(constrained) > wp:columns > wp:group(kart)
3. Bölüm (Detaylar)     →  wp:group(full) > wp:group(constrained) > wp:columns(60/40)
4. Bölüm (CTA/Kapanış)  →  wp:group(full,accent-bg) > wp:group(constrained,rounded) > içerik
```

---

## Özel HTML Bloğu ile Gelişmiş Bileşenler

WordPress'in hazır bloklarının yetersiz kaldığı durumlarda `wp:html` bloğu kullan:

```html
<!-- wp:html -->
<div style="...özel CSS...">
  <!-- Karmaşık bileşen: özel grid, animasyonlu kart, özel form düzeni vb. -->
</div>
<!-- /wp:html -->
```

**wp:html Kullanım Kuralları:**
- Sadece hazır blokların karşılayamadığı karmaşık tasarımlarda kullan
- İçindeki CSS inline olmalı
- JS gerekiyorsa IIFE içinde sar
- Mümkünse hazır blok kombinasyonlarını tercih et

---

## Kalite Kontrol Listesi

### Yapısal Kontroller (KRİTİK)

- [ ] JSON dosyası valid (geçerli) JSON formatında
- [ ] `content.raw` içindeki string düzgün escape edilmiş
- [ ] Her blok açma ve kapama yorumlarıyla sarılı
- [ ] İç içe bloklar doğru hiyerarşide
- [ ] Tüm blok attribute'ları valid JSON nesneleri

### İç İçe Konteyner Kontrolleri

- [ ] Her bölümde minimum 2 katman konteyner var
- [ ] Kart bölümlerinde minimum 3 katman var
- [ ] Katmanlar arası arka plan renk kontrastı var
- [ ] Her katmanda uygun padding tanımlanmış
- [ ] Düz, tek katmanlı blok dizilimi YOK
- [ ] Monoton (her bölüm aynı yapıda) düzen YOK

### Tasarım Kalitesi Kontrolleri

- [ ] Renk paleti referansla birebir eşleşiyor
- [ ] Font boyutları, ağırlıkları seviye bazında eşleşiyor
- [ ] Boşluk/padding referans ritmiyle eşleşiyor
- [ ] Gölge ve border-radius değerleri referansla eşleşiyor
- [ ] Referansta OLMAYAN süsleme EKLENMEMİŞ
- [ ] Jenerik AI estetiği YOK

### Responsive Kontroller

- [ ] `isStackedOnMobile: true` columns bloklarında tanımlı
- [ ] `alignfull` bölümler mobilde düzgün görünüyor

### İçerik Kontrolleri

- [ ] Tüm kullanıcı içerikleri doğru sırada yerleştirilmiş
- [ ] Ekstra metin EKLENMEMİŞ
- [ ] Header/footer dahil EDİLMEMİŞ
- [ ] Görsel placeholder'ları talimat yorumlarıyla işaretli

---

## Sık Yapılan Hatalar ve Düzeltmeleri {#sık-yapılan-hatalar}

| # | Hata | Düzeltme |
|---|------|----------|
| 1 | Geçersiz JSON (escape hatası) | Python `json.dumps()` ile oluştur, elle yazma |
| 2 | Düz blok dizilimi (iç içe konteyner yok) | Her bölümü min. 2 katman group ile sar |
| 3 | Tüm bölümlerde aynı arka plan | Dönüşümlü arka plan renkleri kullan |
| 4 | Blok kapama yorumu eksik | Her `<!-- wp:x -->` için `<!-- /wp:x -->` olmalı |
| 5 | Attribute'larda tek tırnak | JSON'da sadece çift tırnak kullan |
| 6 | `style` attribute'unda object yerine string | `"style":{"color":{"background":"#fff"}}` doğru format |
| 7 | Padding'siz konteynerler | Her katmanda padding tanımla |
| 8 | Monoton kart tasarımı | Bölümlere göre farklı kart varyasyonları kullan |
| 9 | Font bilgisi eksik | Kullanıcıya hangi Google Font'ların gerektiğini bildir |
| 10 | `alignfull` eksik dış gruplarda | Tam genişlik bölümler için `"align":"full"` ekle |
| 11 | Responsive düşünülmemiş | `isStackedOnMobile` ve mobil padding değerlerini ekle |

---

## Son Çıktı Protokolü {#son-çıktı-protokolü}

### JSON Üretim Süreci

1. **Referans URL'yi `web_fetch` ile çek** ve tasarımı analiz et
2. **Tasarım token haritasını oluştur** (renkler, fontlar, boşluklar, katmanlar)
3. **Blok yapısını planla** — her bölüm için iç içe konteyner mimarisini belirle
4. **`content.raw` string'ini oluştur** — blok serileştirme formatında
5. **JSON dosyasını Python ile üret** — escape hatası olmaması için `json.dumps()` kullan
6. **Dosyayı `/mnt/user-data/outputs/wordpress-page.json` olarak kaydet**
7. **`present_files` ile kullanıcıyla paylaş**

### Python ile JSON Üretim Kodu

```python
import json

# Blok içeriğini oluştur
content_raw = """<!-- wp:group {"align":"full",...} -->
<div class="wp-block-group alignfull ...">
  ...tüm blok içeriği...
</div>
<!-- /wp:group -->"""

# JSON yapısını oluştur
page_data = {
    "title": "Sayfa Başlığı",
    "status": "draft",
    "content": {
        "raw": content_raw
    },
    "template": "",
    "meta": {
        "_starter_page_template": "blank"
    }
}

# Dosyaya yaz
with open('/mnt/user-data/outputs/wordpress-page.json', 'w', encoding='utf-8') as f:
    json.dump(page_data, f, ensure_ascii=False, indent=2)
```

### Kullanıcıya İletilecek Bilgiler

JSON dosyasıyla birlikte kullanıcıya şunları bildir:
1. **Gerekli Google Fonts** — Tema ayarlarından yüklenmesi gereken fontlar
2. **Görsel alanları** — Hangi görsellerin WordPress Medya Kütüphanesi'nden eklenmesi gerektiği
3. **Import yöntemi**:
   - REST API ile: `POST /wp-json/wp/v2/pages` endpoint'ine gönderim
   - Starter Templates eklentisi ile: JSON import
   - Manuel: `content.raw` değerini blok editörüne yapıştırma (Kod Editörü modunda)

### Dosya Adlandırma

- Varsayılan: `wordpress-page.json`
- Kullanıcı belirtirse özelleştirilebilir

**UNUTMA:** JSON geçerli olmalı, blok yapısı düzgün iç içe geçmeli, ve her bölüm
katmanlı konteyner mimarisiyle estetik derinlik taşımalıdır.

**DİL KURALI:** Sayfa içerikleri, başlıklar, açıklamalar ve tüm kullanıcıya
görünür metin — hepsi kullanıcının dilinde olacak.
