---
name: wp-elementor-json
description: >
  Referans bir web sitesi URL'sinden tasarım dilini analiz edip, Elementor Template Library
  içe aktarıcısıyla doğrudan yüklenebilecek JSON formatında sayfa çıktısı üret. Kullanıcı
  URL'yi paylaşır, web_fetch ile çekilir, tasarımı analiz edilir ve Elementor'ın native
  Flexbox Container yapısıyla iç içe konteynerler, katmanlı düzenler ve estetik tasarımlar
  üretilir. Üretilen tüm şablonlar %100 RESPONSIVE'dır — desktop, tablet ve mobile için
  tam destek sağlar (tüm container padding, gap, typography, width değerleri 3 breakpoint
  için ayrı ayrı tanımlanır). HTML widget'ları için @media query'li responsive CSS
  otomatik üretilir. Çıktı, WordPress yönetim panelinde Şablonlar > Kayıtlı Şablonlar
  > İçe Aktar menüsünden JSON dosyası olarak doğrudan yüklenir ve sayfaya eklenir.
  Anahtar kelimeler: "Elementor JSON", "Elementor şablon", "Elementor içe aktar",
  "Template Library import", "Flexbox Container", "iç içe konteyner", "responsive tasarım",
  "mobile uyumlu", "tablet mobile font", "bu siteye benzer", "bu URL gibi yap",
  "Elementor template", "JSON şablon", "Elementor tasarım".
---

# Elementor JSON Şablon Üretici — URL Referanslı, Flexbox Container Tabanlı

Referans bir web sitesinin URL'sinden tasarım dilini analiz edip, Elementor Template
Library'ye doğrudan içe aktarılabilecek JSON formatında, iç içe Flexbox Container
yapılarıyla estetik sayfa şablonları üret.

**Bu skill YALNIZCA Elementor tasarımları için kullanılır.**
**Gutenberg blok editörü formatı ÜRETMEZ.**
**Üretilen her şablon %100 RESPONSIVE olmak ZORUNDADIR — desktop, tablet ve mobile için
tam destek sağlanmalıdır. Responsive alanları eksik bir şablon KABUL EDİLMEZ.**

---

## İçindekiler

1.  [Bu Skill Ne Zaman Tetiklenir](#bu-skill-ne-zaman-tetiklenir)
2.  [Elementor Uyumluluk Gereksinimleri](#elementor-uyumluluk)
3.  [Tasarım Felsefesi](#tasarım-felsefesi)
4.  [Adım Adım İş Akışı](#adım-adım-iş-akışı)
5.  [Elementor JSON Yapı Formatı](#json-yapı-formatı)
6.  [Flexbox Container Tasarım Sistemi](#container-sistemi)
7.  [Elementor Widget Türleri Referansı](#widget-referansı)
8.  [Widget Settings Detaylı Referans](#widget-settings-referansı)
9.  [Tasarım Sadakati Rehberi](#tasarım-sadakati)
10. [İçerik Yerleştirme Protokolü](#içerik-yerleştirme)
11. [Responsive Tasarım Kuralları](#responsive)
12. [Çıktı Yapısı Şablonu](#çıktı-şablonu)
13. [Kalite Kontrol Listesi](#kalite-kontrolü)
14. [Sık Yapılan Hatalar ve Düzeltmeleri](#sık-hatalar)
15. [Son Çıktı Protokolü](#son-çıktı)

---

## Bu Skill Ne Zaman Tetiklenir

- Kullanıcı bir referans web sitesi URL'si paylaşır ve benzer tasarımda Elementor sayfası ister
- Çıktı Elementor Template Library'ye JSON olarak içe aktarılacaktır
- Kullanıcı "Şablonlar > İçe Aktar" veya "Elementor template import" yönteminden bahseder
- Kullanıcı Flexbox Container, iç içe konteyner, Elementor widget'ları ister
- Anahtar kelimeler: "Elementor JSON", "Elementor şablon", "Elementor içe aktar",
  "Template Library", "Flexbox Container", "bu siteye benzer", "bu URL gibi",
  "Elementor template import", "JSON template"

**ÖNEMLİ:** Bu skill referans URL'nin birebir kopyasını DEĞİL — o tasarımın dilini,
ritmini ve estetiğini kullanarak YENİ bir Elementor sayfa şablonu üretir.

---

## Elementor Uyumluluk Gereksinimleri {#elementor-uyumluluk}

Bu skill'in ürettiği JSON dosyası, Elementor'ın **Template Library** içe aktarma
özelliğiyle doğrudan kullanılabilir olmalıdır.

### İçe Aktarma Yolu (Kullanıcı Tarafı)

```
WordPress Admin Panel
  → Şablonlar (Templates)
    → Kayıtlı Şablonlar (Saved Templates)
      → Şablonları İçe Aktar (Import Templates) butonu
        → JSON dosyasını seç
          → İçe Aktar butonuna bas
            → Şablon kitaplığına eklenir
              → Sayfa oluştururken "My Templates"ten eklenir
```

### Zorunlu Üst Seviye JSON Yapısı

Elementor her şablon JSON dosyasının şu temel yapıya sahip olmasını bekler:

```json
{
  "title": "Şablon Başlığı",
  "type": "page",
  "version": "0.4",
  "page_settings": [],
  "content": []
}
```

**Alan açıklamaları:**

| Alan | Tip | Açıklama |
|------|-----|----------|
| `title` | string | Şablon adı — Elementor şablon kütüphanesinde görünür |
| `type` | string | Şablon türü: `"page"`, `"section"`, `"header"`, `"footer"`, `"single"`, `"archive"`, `"popup"` |
| `version` | string | Elementor şablon formatı sürümü — her zaman `"0.4"` |
| `page_settings` | array veya object | Sayfa-seviyesi ayarlar (arka plan, layout vs.) — boşsa `[]` |
| `content` | array | Container ve widget elementlerinin listesi — tasarımın tamamı buradadır |

### Element (Container & Widget) Yapısı

Her element (container veya widget) şu yapıya sahiptir:

```json
{
  "id": "12345678",
  "elType": "container",
  "isInner": false,
  "settings": {},
  "elements": []
}
```

**Widget için ek alan:**
```json
{
  "id": "12345678",
  "elType": "widget",
  "widgetType": "heading",
  "isInner": false,
  "settings": {},
  "elements": []
}
```

**KRİTİK KURALLAR:**

1. **`id` alanı benzersiz olmalıdır** — Her element için 8 karakterlik hexadecimal string
2. **`elType` üç değerden biri olmalıdır:** `"container"`, `"widget"`, `"section"`, `"column"`
3. **`isInner` boolean'dır** — İç içe container'larda `true`, en dış container'da `false`
4. **`settings` object olmalıdır** (boş olsa bile) — KESİNLİKLE array (`[]`) DEĞİL
5. **`elements` array olmalıdır** — İç içe elementleri tutar
6. **Widget'larda `widgetType` zorunludur** — `"heading"`, `"text-editor"`, `"button"`, `"image"` vb.
7. **Container'lar widget'ları nest edebilir, widget'lar widget nest EDEMEZ** (nested widget'lar hariç)

### Modern Container Yapısı vs Eski Section/Column

Elementor'da iki farklı yapı mevcut:

**ESKİ YAPI (kullanma):** `section` → `column` → `widget`
**MODERN YAPI (KULLAN):** `container` → `container` veya `widget`

Bu skill **yalnızca modern Flexbox Container yapısını** kullanır çünkü:
- Daha az DOM node üretir (daha hızlı)
- Sonsuz iç içe nesting desteği
- Daha esnek ve modern layout kontrolleri
- Elementor 3.6+ ve sonrasının standart yapısı

---

## Tasarım Felsefesi {#tasarım-felsefesi}

Bu skill'in ürettiği çıktı, deneyimli bir Elementor uzmanının profesyonel müşteri
projesi için oluşturduğu bir sayfa gibi görünmelidir.

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
  ✗ Düz, tek katmanlı container dizilimleri
```

### Uzman Tasarımcı Kalitesi Kuralları

```
ZORUNLU — Profesyonel uzman dokunuşu:
  ✓ Referans tasarıma birebir sadakat
  ✓ İç içe container'larla derinlik ve katman hissi
  ✓ Kasıtlı ve anlamlı beyaz alan (white space) kullanımı
  ✓ Tutarlı ama monoton olmayan görsel ritim
  ✓ İçeriğe uygun, bağlamsal tipografi seçimleri
  ✓ Detaylara özen: satır yüksekliği, harf aralığı, ince kenarlıklar
  ✓ Arka plan katmanları: dış container bg + iç container bg + kart bg
  ✓ Asimetrik düzenlerden korkmamak (referans gerektiriyorsa)
  ✓ Mikro-detaylar: ince ayırıcı çizgiler, accent renkli küçük vurgular
  ✓ İçerik hiyerarşisinde net basamaklar
  ✓ Flexbox'un gücünden tam faydalanma (justify, align, gap)
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
4. Görselleri ve renk paletini tespit et
```

Her öğeyi incele:

| Analiz Hedefi | Ne Çıkarılacak |
|---------------|----------------|
| HTML yapısı | Bölüm düzeni, container iç içeliği, semantik hiyerarşi |
| CSS | Renk paleti, font aileleri, boşluk sistemi, grid/flex desenleri, hover durumları, gölgeler, border-radius, responsive kırılma noktaları |
| Görsel katmanlar | Arka plan renkleri/gradientleri, overlay'ler, iç içe container arka planları |
| Bileşen desenleri | Kartlar, butonlar, listeler, özellik blokları, CTA alanları |
| Derinlik yapısı | Kaç katman container iç içe geçmiş, hangi seviyede hangi stil uygulanmış |
| Flexbox ipuçları | Row/column direction, gap değerleri, justify/align kullanımları |

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
  Arka Plan Katman 1:       #______ (dış container / sayfa arka planı)
  Arka Plan Katman 2:       #______ (iç container / bölüm arka planı)
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
  İçerik Boşluğu (gap):       __px
  Kart İç Padding:            __px
  Container İç İçe Padding:   __px (dış) → __px (iç)

CONTAINER DERECELENMESİ:
  Seviye 1 (Dış):   Genişlik: Full Width | Padding: __px | Arka Plan: #______
  Seviye 2 (Orta):  Genişlik: Boxed __px | Padding: __px | Arka Plan: #______
  Seviye 3 (İç):    Genişlik: Boxed __px | Padding: __px | Arka Plan: #______

DEKORATİF:
  Border Radius:    __px (kartlar) / __px (butonlar)
  Box Shadow:       ______________________________
  Ayırıcı Stili:    ______________________________

FLEXBOX AYARLARI:
  Ana Direction:    row / column
  Justify Content:  flex-start / center / flex-end / space-between
  Align Items:      flex-start / center / flex-end / stretch
  Gap:              __px
═══════════════════════════════════════════════
```

### Faz 3: JSON Yapısını Üret

Aşağıdaki format kurallarına uyarak Elementor şablon JSON'u oluştur.

---

## Elementor JSON Yapı Formatı {#json-yapı-formatı}

### Temel Şablon İskeleti

```json
{
  "title": "Ana Sayfa Şablonu",
  "type": "page",
  "version": "0.4",
  "page_settings": [],
  "content": [
    {
      "id": "a1b2c3d4",
      "elType": "container",
      "isInner": false,
      "settings": {
        "content_width": "full",
        "padding": {
          "unit": "px",
          "top": "80",
          "right": "0",
          "bottom": "80",
          "left": "0",
          "isLinked": false
        },
        "background_background": "classic",
        "background_color": "#f8f9fa"
      },
      "elements": []
    }
  ]
}
```

### Container Settings Detaylı Referans

**Content Width (İçerik Genişliği):**
```json
"content_width": "full"      // Tam genişlik (default)
"content_width": "boxed"     // Sınırlı genişlik
```

**Width (Boxed için):**
```json
"width": {
  "unit": "px",
  "size": 1200
}
```

**Flex Direction (Yön):**
```json
"flex_direction": "row"              // Yatay sıralama
"flex_direction": "column"           // Dikey sıralama
"flex_direction": "row-reverse"      // Ters yatay
"flex_direction": "column-reverse"   // Ters dikey
```

**Flex Justify Content (Ana Eksen Hizalama):**
```json
"flex_justify_content": "flex-start"     // Başa yasla
"flex_justify_content": "center"         // Ortala
"flex_justify_content": "flex-end"       // Sona yasla
"flex_justify_content": "space-between"  // Aralarında boşluk
"flex_justify_content": "space-around"   // Etraflarında boşluk
"flex_justify_content": "space-evenly"   // Eşit boşluk
```

**Flex Align Items (Çapraz Eksen Hizalama):**
```json
"flex_align_items": "flex-start"
"flex_align_items": "center"
"flex_align_items": "flex-end"
"flex_align_items": "stretch"
```

**Flex Gap (Elementler Arası Boşluk):**
```json
"flex_gap": {
  "column": "20",
  "row": "20",
  "unit": "px",
  "isLinked": true
}
```

**Flex Wrap (Satır Kaydırma):**
```json
"flex_wrap": "wrap"      // Sarmalama açık
"flex_wrap": "nowrap"    // Sarmalama kapalı (default)
```

**Padding:**
```json
"padding": {
  "unit": "px",
  "top": "80",
  "right": "24",
  "bottom": "80",
  "left": "24",
  "isLinked": false
}
```

**Margin:**
```json
"margin": {
  "unit": "px",
  "top": "0",
  "right": "0",
  "bottom": "0",
  "left": "0",
  "isLinked": true
}
```

**Background (Klasik Renk):**
```json
"background_background": "classic",
"background_color": "#ffffff"
```

**Background (Gradient):**
```json
"background_background": "gradient",
"background_color": "#667eea",
"background_color_b": "#764ba2",
"background_gradient_type": "linear",
"background_gradient_angle": {
  "unit": "deg",
  "size": 135
}
```

**Background (Görsel):**
```json
"background_background": "classic",
"background_image": {
  "url": "https://example.com/image.jpg",
  "id": ""
},
"background_position": "center center",
"background_repeat": "no-repeat",
"background_size": "cover",
"background_overlay_background": "classic",
"background_overlay_color": "#000000",
"background_overlay_opacity": {
  "unit": "px",
  "size": 0.5
}
```

**Border Radius:**
```json
"border_radius": {
  "unit": "px",
  "top": "16",
  "right": "16",
  "bottom": "16",
  "left": "16",
  "isLinked": true
}
```

**Border:**
```json
"border_border": "solid",
"border_width": {
  "unit": "px",
  "top": "1",
  "right": "1",
  "bottom": "1",
  "left": "1",
  "isLinked": true
},
"border_color": "#e2e8f0"
```

**Box Shadow:**
```json
"box_shadow_box_shadow_type": "yes",
"box_shadow_box_shadow": {
  "horizontal": 0,
  "vertical": 4,
  "blur": 20,
  "spread": 0,
  "color": "rgba(0,0,0,0.08)"
}
```

**Min Height:**
```json
"min_height": {
  "unit": "px",
  "size": 500
}
```

---

## Flexbox Container Tasarım Sistemi {#container-sistemi}

Elementor'ın native Flexbox Container'larını iç içe kullanarak estetik, katmanlı
tasarımlar üret. **Düz, tek katmanlı container dizilimi YASAKTIR.**

### Katmanlı Mimari Prensibi

Her bölüm minimum 2, ideal 3 katman derinliğinde olmalıdır:

```
KATMAN 1 — Dış Container (Full Width Bölüm)
│  content_width: "full"
│  isInner: false
│  Arka plan rengi, gradient veya görsel
│  Üst-alt padding ile bölüm ritmi
│
├── KATMAN 2 — İçerik Container (Boxed)
│   │  content_width: "boxed", width: 1200px
│   │  isInner: true
│   │  İç padding ile nefes alanı
│   │  Farklı arka plan (opsiyonel)
│   │
│   ├── KATMAN 3a — İçerik Grubu Container
│   │   │  flex_direction: "row"
│   │   │  flex_gap: {...}
│   │   │  isInner: true
│   │   │
│   │   ├── Widget (heading)
│   │   └── Widget (text-editor)
│   │
│   └── KATMAN 3b — Kart Container'ları
│       │  Arka plan, gölge, radius ile kart görünümü
│       │  isInner: true
│       │
│       └── İç widget'lar
```

### Dış Container Deseni (Katman 1 — Full Width Bölüm)

```json
{
  "id": "out00001",
  "elType": "container",
  "isInner": false,
  "settings": {
    "content_width": "full",
    "flex_direction": "column",
    "flex_justify_content": "center",
    "flex_align_items": "center",
    "padding": {
      "unit": "px",
      "top": "80",
      "right": "24",
      "bottom": "80",
      "left": "24",
      "isLinked": false
    },
    "background_background": "classic",
    "background_color": "#f8f9fa"
  },
  "elements": []
}
```

### İçerik Container Deseni (Katman 2 — Boxed)

```json
{
  "id": "inn00001",
  "elType": "container",
  "isInner": true,
  "settings": {
    "content_width": "boxed",
    "width": {
      "unit": "px",
      "size": 1200
    },
    "flex_direction": "column",
    "flex_gap": {
      "column": "32",
      "row": "32",
      "unit": "px",
      "isLinked": true
    },
    "padding": {
      "unit": "px",
      "top": "40",
      "right": "40",
      "bottom": "40",
      "left": "40",
      "isLinked": true
    },
    "background_background": "classic",
    "background_color": "#ffffff",
    "border_radius": {
      "unit": "px",
      "top": "16",
      "right": "16",
      "bottom": "16",
      "left": "16",
      "isLinked": true
    }
  },
  "elements": []
}
```

### Yan Yana Container (Katman 3 — Row Layout)

```json
{
  "id": "row00001",
  "elType": "container",
  "isInner": true,
  "settings": {
    "content_width": "full",
    "flex_direction": "row",
    "flex_gap": {
      "column": "32",
      "row": "32",
      "unit": "px",
      "isLinked": true
    },
    "flex_wrap": "wrap"
  },
  "elements": []
}
```

### Kart Container Deseni

```json
{
  "id": "crd00001",
  "elType": "container",
  "isInner": true,
  "settings": {
    "content_width": "boxed",
    "width": {
      "unit": "%",
      "size": 33.33
    },
    "flex_direction": "column",
    "flex_gap": {
      "column": "16",
      "row": "16",
      "unit": "px",
      "isLinked": true
    },
    "padding": {
      "unit": "px",
      "top": "32",
      "right": "32",
      "bottom": "32",
      "left": "32",
      "isLinked": true
    },
    "background_background": "classic",
    "background_color": "#ffffff",
    "border_radius": {
      "unit": "px",
      "top": "12",
      "right": "12",
      "bottom": "12",
      "left": "12",
      "isLinked": true
    },
    "box_shadow_box_shadow_type": "yes",
    "box_shadow_box_shadow": {
      "horizontal": 0,
      "vertical": 2,
      "blur": 12,
      "spread": 0,
      "color": "rgba(0,0,0,0.08)"
    }
  },
  "elements": []
}
```

### İç İçe Derinlik Kuralları

```
ZORUNLU:
  ✓ Her bölümde minimum 2 katman container var
  ✓ Kart içeren bölümlerde minimum 3 katman var
  ✓ Katmanlar arası arka plan renk kontrastı var
  ✓ Her katmanda uygun padding ile nefes alanı
  ✓ Border-radius ile yumuşak köşeler (referansa uygun)
  ✓ Flexbox gap değerleri ile ritim
  ✓ En dış container'da isInner: false, içtekilerde isInner: true

YASAK:
  ✗ Düz, tek katmanlı container dizilimi
  ✗ Tüm bölümlerde aynı arka plan rengi
  ✗ Padding'siz sıkışık container'lar
  ✗ İç içe container kullanmadan sadece widget sıralaması
  ✗ Her bölümde aynı katman yapısı (monotonluk)
  ✗ Eski section/column yapısı (sadece modern container kullan)
```

---

## Elementor Widget Türleri Referansı {#widget-referansı}

### Temel (Free) Widget'lar — Bu Skill Sadece Bunları Kullanır

| widgetType | Kullanım | Önemli Ayarlar |
|------------|----------|----------------|
| `heading` | Başlıklar (h1-h6) | `title`, `header_size`, `align`, `title_color`, `typography_*` |
| `text-editor` | Rich text, paragraflar | `editor` (HTML içerir), `align`, `text_color`, `typography_*` |
| `image` | Görsel | `image.url`, `image.id`, `image_size`, `align`, `width` |
| `button` | Buton | `text`, `link.url`, `background_color`, `button_text_color`, `border_radius` |
| `divider` | Ayırıcı çizgi | `style`, `color`, `weight`, `width` |
| `spacer` | Dikey boşluk | `space` |
| `icon` | İkon | `selected_icon`, `primary_color`, `size` |
| `icon-box` | İkon + başlık + metin | `icon`, `title_text`, `description_text` |
| `icon-list` | İkonlu liste | `icon_list` (repeater) |
| `image-box` | Görsel + başlık + metin | `image`, `title_text`, `description_text` |
| `html` | Özel HTML | `html` |
| `google-maps` | Harita | `address` |

**NOT:** Pro widget'ları (form, posts, slides, nav-menu, theme-builder elemanları)
bu skill'de KULLANILMAZ — yalnızca Elementor Free'nin native widget'larıyla çalış.

---

## Widget Settings Detaylı Referans {#widget-settings-referansı}

### Heading Widget

```json
{
  "id": "hdr00001",
  "elType": "widget",
  "widgetType": "heading",
  "isInner": false,
  "settings": {
    "title": "Hoş Geldiniz",
    "header_size": "h2",
    "align": "center",
    "title_color": "#1a1a2e",
    "typography_typography": "custom",
    "typography_font_family": "Inter",
    "typography_font_size": {
      "unit": "px",
      "size": 48
    },
    "typography_font_weight": "700",
    "typography_line_height": {
      "unit": "em",
      "size": 1.2
    },
    "typography_letter_spacing": {
      "unit": "px",
      "size": -0.5
    }
  },
  "elements": []
}
```

### Text Editor Widget

```json
{
  "id": "txt00001",
  "elType": "widget",
  "widgetType": "text-editor",
  "isInner": false,
  "settings": {
    "editor": "<p>Buraya paragraf metni gelir. <strong>Kalın metin</strong> ve <em>italik metin</em> desteklenir.</p>",
    "align": "left",
    "text_color": "#4a5568",
    "typography_typography": "custom",
    "typography_font_family": "Inter",
    "typography_font_size": {
      "unit": "px",
      "size": 17
    },
    "typography_font_weight": "400",
    "typography_line_height": {
      "unit": "em",
      "size": 1.7
    }
  },
  "elements": []
}
```

### Button Widget

```json
{
  "id": "btn00001",
  "elType": "widget",
  "widgetType": "button",
  "isInner": false,
  "settings": {
    "text": "Daha Fazla Bilgi",
    "link": {
      "url": "#",
      "is_external": "",
      "nofollow": ""
    },
    "align": "center",
    "size": "md",
    "button_text_color": "#ffffff",
    "background_color": "#2563eb",
    "hover_color": "#ffffff",
    "button_background_hover_color": "#1d4ed8",
    "border_radius": {
      "unit": "px",
      "top": "8",
      "right": "8",
      "bottom": "8",
      "left": "8",
      "isLinked": true
    },
    "text_padding": {
      "unit": "px",
      "top": "14",
      "right": "28",
      "bottom": "14",
      "left": "28",
      "isLinked": false
    },
    "typography_typography": "custom",
    "typography_font_family": "Inter",
    "typography_font_size": {
      "unit": "px",
      "size": 16
    },
    "typography_font_weight": "600"
  },
  "elements": []
}
```

### Image Widget

```json
{
  "id": "img00001",
  "elType": "widget",
  "widgetType": "image",
  "isInner": false,
  "settings": {
    "image": {
      "url": "https://example.com/images/hero.jpg",
      "id": ""
    },
    "image_size": "large",
    "align": "center",
    "width": {
      "unit": "%",
      "size": 100
    },
    "border_radius": {
      "unit": "px",
      "top": "12",
      "right": "12",
      "bottom": "12",
      "left": "12",
      "isLinked": true
    }
  },
  "elements": []
}
```

### Divider Widget

```json
{
  "id": "div00001",
  "elType": "widget",
  "widgetType": "divider",
  "isInner": false,
  "settings": {
    "style": "solid",
    "weight": {
      "unit": "px",
      "size": 1
    },
    "color": "#e2e8f0",
    "width": {
      "unit": "%",
      "size": 100
    },
    "align": "center"
  },
  "elements": []
}
```

### Spacer Widget

```json
{
  "id": "spc00001",
  "elType": "widget",
  "widgetType": "spacer",
  "isInner": false,
  "settings": {
    "space": {
      "unit": "px",
      "size": 40
    }
  },
  "elements": []
}
```

### Icon Box Widget

```json
{
  "id": "ibx00001",
  "elType": "widget",
  "widgetType": "icon-box",
  "isInner": false,
  "settings": {
    "selected_icon": {
      "value": "fas fa-rocket",
      "library": "fa-solid"
    },
    "title_text": "Hızlı Teslimat",
    "description_text": "Siparişleriniz 24 saat içinde kapınızda.",
    "position": "top",
    "title_size": "h4",
    "primary_color": "#2563eb",
    "title_color": "#1a1a2e",
    "description_color": "#4a5568"
  },
  "elements": []
}
```

### Icon List Widget

```json
{
  "id": "ilt00001",
  "elType": "widget",
  "widgetType": "icon-list",
  "isInner": false,
  "settings": {
    "view": "default",
    "icon_list": [
      {
        "_id": "item1",
        "text": "İlk özellik",
        "selected_icon": {
          "value": "fas fa-check",
          "library": "fa-solid"
        }
      },
      {
        "_id": "item2",
        "text": "İkinci özellik",
        "selected_icon": {
          "value": "fas fa-check",
          "library": "fa-solid"
        }
      }
    ],
    "icon_color": "#2563eb",
    "text_color": "#1a1a2e",
    "space_between": {
      "unit": "px",
      "size": 16
    }
  },
  "elements": []
}
```

### HTML Widget (Özel Bileşenler) — KRİTİK RESPONSIVE KURALLARI

HTML widget'ı, Elementor'ın hazır widget'larının yetersiz kaldığı durumlarda kullanılır.
ANCAK HTML widget içindeki stiller Elementor'ın responsive kontrol sistemini KULLANAMAZ
(çünkü raw HTML'dir). Bu yüzden responsive davranış **CSS media query'leri** ile
sağlanmalıdır.

**ZORUNLU KURAL: Her HTML widget'ta `<style>` bloğu içinde media query'ler olmak ZORUNDA.**

#### HTML Widget Elementor Breakpoint'leri

Elementor'ın standart breakpoint'lerine uygun media query'ler kullan:

```
Desktop:           1025px ve üzeri (default, media query gerekmez)
Tablet Yatay:      768px - 1024px  → @media (max-width: 1024px)
Tablet Dikey:      768px - 880px   → @media (max-width: 880px)
Mobile Yatay:      480px - 767px   → @media (max-width: 767px)
Mobile:            767px altı      → @media (max-width: 767px)
Mobile Küçük:      360px altı      → @media (max-width: 360px)
```

**Standart iki breakpoint yeterlidir:** `max-width: 1024px` (tablet) ve `max-width: 767px` (mobile).

#### Doğru HTML Widget Yapısı (Responsive CSS İçeren)

```json
{
  "id": "htm00001",
  "elType": "widget",
  "widgetType": "html",
  "isInner": false,
  "settings": {
    "html": "<style>\n.wps-custom-card {\n  display: flex;\n  flex-direction: row;\n  gap: 32px;\n  padding: 48px;\n  background: #ffffff;\n  border-radius: 16px;\n  box-shadow: 0 4px 20px rgba(0,0,0,0.08);\n}\n.wps-custom-card__title {\n  font-size: 36px;\n  font-weight: 700;\n  line-height: 1.2;\n  color: #1a1a2e;\n  margin: 0 0 16px 0;\n}\n.wps-custom-card__text {\n  font-size: 17px;\n  line-height: 1.7;\n  color: #4a5568;\n  margin: 0;\n}\n.wps-custom-card__image {\n  width: 300px;\n  height: auto;\n  border-radius: 12px;\n  object-fit: cover;\n}\n\n/* TABLET */\n@media (max-width: 1024px) {\n  .wps-custom-card {\n    gap: 24px;\n    padding: 32px;\n  }\n  .wps-custom-card__title {\n    font-size: 28px;\n  }\n  .wps-custom-card__text {\n    font-size: 16px;\n  }\n  .wps-custom-card__image {\n    width: 240px;\n  }\n}\n\n/* MOBILE */\n@media (max-width: 767px) {\n  .wps-custom-card {\n    flex-direction: column;\n    gap: 20px;\n    padding: 24px;\n    border-radius: 12px;\n  }\n  .wps-custom-card__title {\n    font-size: 24px;\n  }\n  .wps-custom-card__text {\n    font-size: 15px;\n    line-height: 1.6;\n  }\n  .wps-custom-card__image {\n    width: 100%;\n    max-width: 100%;\n  }\n}\n</style>\n\n<div class=\"wps-custom-card\">\n  <img class=\"wps-custom-card__image\" src=\"https://example.com/image.jpg\" alt=\"Açıklama\">\n  <div class=\"wps-custom-card__content\">\n    <h3 class=\"wps-custom-card__title\">Kart Başlığı</h3>\n    <p class=\"wps-custom-card__text\">Kart metni buraya gelir.</p>\n  </div>\n</div>"
  },
  "elements": []
}
```

#### HTML Widget İçin Responsive Zorunlulukları

```
HER HTML WIDGET'ta ZORUNLU:
  ✓ Bir adet <style> bloğu widget'ın başında olmalı
  ✓ En az iki media query: @media (max-width: 1024px) ve @media (max-width: 767px)
  ✓ Tablet'ta font-size değerleri küçültülmüş olmalı (genellikle %70-80)
  ✓ Mobile'da font-size değerleri daha da küçültülmüş olmalı (genellikle %55-65)
  ✓ Row layout kullanan düzenler mobile'da flex-direction: column olmalı
  ✓ Mobile'da padding değerleri küçültülmüş olmalı
  ✓ Mobile'da gap değerleri küçültülmüş olmalı
  ✓ Sabit genişlik (px) olan öğeler mobile'da width: 100% olmalı
  ✓ Border-radius değerleri mobile'da biraz azaltılabilir (opsiyonel)

YASAK:
  ✗ <style> bloğu olmadan inline style'larla çok karmaşık HTML
  ✗ Media query olmayan raw HTML widget'ı
  ✗ Sabit px genişlikli container'lar (mobile'da taşma yapar)
  ✗ Viewport'tan büyük font değerleri (örn. 72px desktop + mobile karşılığı yok)
  ✗ Mobile'da flex-direction: row bırakmak (taşma/sıkışma nedeni)
```

#### Responsive Font Ölçekleme Tablosu (HTML Widget İçin Rehber)

Desktop → Tablet → Mobile dönüşüm oranları:

| Eleman Türü | Desktop | Tablet (~%75) | Mobile (~%60) |
|-------------|---------|---------------|---------------|
| H1 Büyük Başlık | 56-72px | 42-54px | 32-40px |
| H2 Orta Başlık | 40-48px | 30-36px | 24-28px |
| H3 Alt Başlık | 28-36px | 22-28px | 18-22px |
| H4 Küçük Başlık | 22-24px | 18-20px | 16-18px |
| Gövde Metni | 17-18px | 16px | 15-16px |
| Küçük Metin | 14-15px | 14px | 13-14px |
| Buton Metni | 16-17px | 15-16px | 14-15px |

#### Responsive Padding/Spacing Ölçekleme Tablosu

| Değer Türü | Desktop | Tablet | Mobile |
|------------|---------|--------|--------|
| Bölüm Dikey Padding | 80-120px | 60-80px | 40-60px |
| Bölüm Yatay Padding | 24-48px | 24px | 16px |
| Kart İç Padding | 40-48px | 28-32px | 20-24px |
| Gap (büyük) | 32-48px | 24-32px | 16-20px |
| Gap (orta) | 20-24px | 16-20px | 12-16px |
| Gap (küçük) | 12-16px | 10-14px | 8-12px |

#### Karmaşık HTML Widget Örnek: Feature Grid (3 Kart)

```json
{
  "id": "htm00002",
  "elType": "widget",
  "widgetType": "html",
  "isInner": false,
  "settings": {
    "html": "<style>\n.wps-feat-grid {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 32px;\n}\n.wps-feat-card {\n  padding: 40px 32px;\n  background: #ffffff;\n  border-radius: 16px;\n  border: 1px solid #e2e8f0;\n  transition: transform 0.3s ease, box-shadow 0.3s ease;\n}\n.wps-feat-card:hover {\n  transform: translateY(-4px);\n  box-shadow: 0 12px 32px rgba(0,0,0,0.08);\n}\n.wps-feat-card__icon {\n  width: 56px;\n  height: 56px;\n  background: #2563eb;\n  color: #ffffff;\n  border-radius: 12px;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  font-size: 24px;\n  margin-bottom: 24px;\n}\n.wps-feat-card__title {\n  font-size: 22px;\n  font-weight: 700;\n  color: #1a1a2e;\n  margin: 0 0 12px 0;\n  line-height: 1.3;\n}\n.wps-feat-card__desc {\n  font-size: 16px;\n  line-height: 1.6;\n  color: #4a5568;\n  margin: 0;\n}\n\n/* TABLET: 2 sütun */\n@media (max-width: 1024px) {\n  .wps-feat-grid {\n    grid-template-columns: repeat(2, 1fr);\n    gap: 24px;\n  }\n  .wps-feat-card {\n    padding: 32px 24px;\n  }\n  .wps-feat-card__icon {\n    width: 48px;\n    height: 48px;\n    font-size: 20px;\n    margin-bottom: 20px;\n  }\n  .wps-feat-card__title {\n    font-size: 20px;\n  }\n  .wps-feat-card__desc {\n    font-size: 15px;\n  }\n}\n\n/* MOBILE: tek sütun */\n@media (max-width: 767px) {\n  .wps-feat-grid {\n    grid-template-columns: 1fr;\n    gap: 16px;\n  }\n  .wps-feat-card {\n    padding: 24px 20px;\n    border-radius: 12px;\n  }\n  .wps-feat-card__icon {\n    width: 44px;\n    height: 44px;\n    font-size: 18px;\n    margin-bottom: 16px;\n  }\n  .wps-feat-card__title {\n    font-size: 18px;\n    margin-bottom: 8px;\n  }\n  .wps-feat-card__desc {\n    font-size: 14px;\n    line-height: 1.55;\n  }\n}\n</style>\n\n<div class=\"wps-feat-grid\">\n  <div class=\"wps-feat-card\">\n    <div class=\"wps-feat-card__icon\">⚡</div>\n    <h3 class=\"wps-feat-card__title\">Hızlı</h3>\n    <p class=\"wps-feat-card__desc\">Birinci özellik açıklaması.</p>\n  </div>\n  <div class=\"wps-feat-card\">\n    <div class=\"wps-feat-card__icon\">🔒</div>\n    <h3 class=\"wps-feat-card__title\">Güvenli</h3>\n    <p class=\"wps-feat-card__desc\">İkinci özellik açıklaması.</p>\n  </div>\n  <div class=\"wps-feat-card\">\n    <div class=\"wps-feat-card__icon\">✨</div>\n    <h3 class=\"wps-feat-card__title\">Modern</h3>\n    <p class=\"wps-feat-card__desc\">Üçüncü özellik açıklaması.</p>\n  </div>\n</div>"
  },
  "elements": []
}
```

#### HTML Widget CSS Sınıf İsimlendirme Kuralları

WordPress tema çakışmalarını önlemek için benzersiz prefix kullan:

```
ZORUNLU PREFIX: wps- (WordPress Site)
  ✓ wps-card, wps-grid, wps-hero, wps-feature
  ✓ BEM-benzeri: wps-card__title, wps-card__image, wps-card--featured
  ✗ .card, .grid, .container (çok genel, tema ile çakışır)
  ✗ .wrapper, .content, .item (çok genel)
```

#### HTML Widget'ta Viewport Meta Uyumluluğu

HTML widget içinde oluşturduğun stiller mobile'da taşma yapmaması için:

```css
/* Container'ların asla viewport'u aşmaması için ZORUNLU */
.wps-my-element {
  max-width: 100%;
  box-sizing: border-box;
  overflow-wrap: break-word;
}

/* Görsellerin otomatik ölçeklenmesi için ZORUNLU */
.wps-my-element img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

---

## Responsive Tasarım Kuralları {#responsive}

Elementor otomatik olarak 3 breakpoint kullanır: **Desktop** (1025px+), **Tablet**
(768-1024px), **Mobile** (767px ve altı).

**MUTLAK KURAL: Bu skill'in ürettiği her şablon TAMAMEN responsive olmak ZORUNDADIR.
Tek bir widget, container veya HTML bloğu bile responsive kontrollerden muaf değildir.**

### Responsive Değer Formatı (Elementor Native Widget'lar)

Herhangi bir ayar için responsive değer eklemek Elementor'ın native widget'larında
`_tablet` ve `_mobile` suffix'li alanlar eklenerek yapılır:

```json
"padding": {
  "unit": "px",
  "top": "80",
  "right": "24",
  "bottom": "80",
  "left": "24",
  "isLinked": false
},
"padding_tablet": {
  "unit": "px",
  "top": "60",
  "right": "24",
  "bottom": "60",
  "left": "24",
  "isLinked": false
},
"padding_mobile": {
  "unit": "px",
  "top": "40",
  "right": "16",
  "bottom": "40",
  "left": "16",
  "isLinked": false
}
```

### Her Widget Türü İçin Responsive Alanlar

#### Heading Widget — ZORUNLU Responsive Alanlar

```json
{
  "typography_font_size": {"unit": "px", "size": 48},
  "typography_font_size_tablet": {"unit": "px", "size": 36},
  "typography_font_size_mobile": {"unit": "px", "size": 28},
  
  "typography_line_height": {"unit": "em", "size": 1.2},
  "typography_line_height_tablet": {"unit": "em", "size": 1.25},
  "typography_line_height_mobile": {"unit": "em", "size": 1.3},
  
  "typography_letter_spacing": {"unit": "px", "size": -0.5},
  "typography_letter_spacing_mobile": {"unit": "px", "size": 0},
  
  "align": "left",
  "align_mobile": "center"
}
```

#### Text Editor Widget — ZORUNLU Responsive Alanlar

```json
{
  "typography_font_size": {"unit": "px", "size": 17},
  "typography_font_size_tablet": {"unit": "px", "size": 16},
  "typography_font_size_mobile": {"unit": "px", "size": 15},
  
  "typography_line_height": {"unit": "em", "size": 1.7},
  "typography_line_height_mobile": {"unit": "em", "size": 1.6}
}
```

#### Button Widget — ZORUNLU Responsive Alanlar

```json
{
  "typography_font_size": {"unit": "px", "size": 16},
  "typography_font_size_mobile": {"unit": "px", "size": 15},
  
  "text_padding": {"unit": "px", "top": "14", "right": "28", "bottom": "14", "left": "28", "isLinked": false},
  "text_padding_mobile": {"unit": "px", "top": "12", "right": "20", "bottom": "12", "left": "20", "isLinked": false},
  
  "align": "left",
  "align_mobile": "center"
}
```

#### Image Widget — ZORUNLU Responsive Alanlar

```json
{
  "width": {"unit": "%", "size": 60},
  "width_tablet": {"unit": "%", "size": 80},
  "width_mobile": {"unit": "%", "size": 100},
  
  "align": "left",
  "align_mobile": "center"
}
```

#### Icon Box Widget — ZORUNLU Responsive Alanlar

```json
{
  "title_typography_font_size": {"unit": "px", "size": 22},
  "title_typography_font_size_mobile": {"unit": "px", "size": 18},
  
  "description_typography_font_size": {"unit": "px", "size": 16},
  "description_typography_font_size_mobile": {"unit": "px", "size": 15},
  
  "icon_space": {"unit": "px", "size": 24},
  "icon_space_mobile": {"unit": "px", "size": 16},
  
  "position": "top",
  "position_mobile": "top"
}
```

#### Spacer Widget — ZORUNLU Responsive Alanlar

```json
{
  "space": {"unit": "px", "size": 80},
  "space_tablet": {"unit": "px", "size": 60},
  "space_mobile": {"unit": "px", "size": 40}
}
```

#### Divider Widget — ZORUNLU Responsive Alanlar

```json
{
  "width": {"unit": "%", "size": 100},
  "weight": {"unit": "px", "size": 1},
  "gap": {"unit": "px", "size": 40},
  "gap_mobile": {"unit": "px", "size": 24}
}
```

### Her Container İçin Responsive Alanlar — ZORUNLU

```json
{
  "padding": {"unit": "px", "top": "80", "right": "24", "bottom": "80", "left": "24", "isLinked": false},
  "padding_tablet": {"unit": "px", "top": "60", "right": "24", "bottom": "60", "left": "24", "isLinked": false},
  "padding_mobile": {"unit": "px", "top": "40", "right": "16", "bottom": "40", "left": "16", "isLinked": false},
  
  "flex_gap": {"column": "32", "row": "32", "unit": "px", "isLinked": true},
  "flex_gap_tablet": {"column": "24", "row": "24", "unit": "px", "isLinked": true},
  "flex_gap_mobile": {"column": "16", "row": "16", "unit": "px", "isLinked": true},
  
  "flex_direction": "row",
  "flex_direction_tablet": "row",
  "flex_direction_mobile": "column",
  
  "width": {"unit": "%", "size": 33.33},
  "width_tablet": {"unit": "%", "size": 50},
  "width_mobile": {"unit": "%", "size": 100}
}
```

### Responsive Font Ölçekleme Tablosu (Elementor Native Widget'lar)

Desktop → Tablet → Mobile dönüşüm oranları:

| Eleman Türü | Desktop | Tablet (~%75) | Mobile (~%60) |
|-------------|---------|---------------|---------------|
| H1 Büyük Başlık | 56-72px | 42-54px | 32-40px |
| H2 Orta Başlık | 40-48px | 30-36px | 24-28px |
| H3 Alt Başlık | 28-36px | 22-28px | 18-22px |
| H4 Küçük Başlık | 22-24px | 18-20px | 16-18px |
| Gövde Metni | 17-18px | 16px | 15-16px |
| Küçük Metin | 14-15px | 14px | 13-14px |
| Buton Metni | 16-17px | 15-16px | 14-15px |

### Responsive Padding/Spacing Ölçekleme Tablosu

| Değer Türü | Desktop | Tablet | Mobile |
|------------|---------|--------|--------|
| Bölüm Dikey Padding | 80-120px | 60-80px | 40-60px |
| Bölüm Yatay Padding | 24-48px | 24px | 16px |
| Container İç Padding | 40-48px | 28-32px | 20-24px |
| Flex Gap (büyük) | 32-48px | 24-32px | 16-20px |
| Flex Gap (orta) | 20-24px | 16-20px | 12-16px |
| Flex Gap (küçük) | 12-16px | 10-14px | 8-12px |
| Spacer Yüksekliği | 60-100px | 40-70px | 30-50px |

### Sütun Genişlikleri Dönüşüm Kuralları

Row layout'taki container'lar için mobile stacking:

```json
// 3 sütunlu düzen
"width": {"unit": "%", "size": 33.33}       // Desktop: 3 yan yana
"width_tablet": {"unit": "%", "size": 50}   // Tablet: 2 yan yana
"width_mobile": {"unit": "%", "size": 100}  // Mobile: alt alta

// 4 sütunlu düzen
"width": {"unit": "%", "size": 25}          // Desktop: 4 yan yana
"width_tablet": {"unit": "%", "size": 50}   // Tablet: 2x2 grid
"width_mobile": {"unit": "%", "size": 100}  // Mobile: alt alta

// 2 sütunlu düzen (60/40)
"width": {"unit": "%", "size": 60}          // Desktop: 60%
"width_mobile": {"unit": "%", "size": 100}  // Mobile: 100%
```

### Responsive Zorunluluklar — KAPSAMLI LİSTE

```
HER BÖLÜMDE ZORUNLU:
  ✓ Dış container padding: desktop + tablet + mobile tanımlı
  ✓ İç container padding: desktop + tablet + mobile tanımlı  
  ✓ Flex gap değerleri: desktop + tablet + mobile tanımlı
  ✓ Row container'lar mobile'da column'a dönmeli
  ✓ Sütun widget'ları mobile'da 100% olmalı
  ✓ Sütun widget'ları tablet'te ara değer almalı (50%, 66%, vs.)

HER METİN WIDGET'INDA ZORUNLU:
  ✓ Font size: desktop + tablet + mobile tanımlı
  ✓ H1 ve H2 için line_height mobile'da biraz artırılmalı
  ✓ Ortalamadan büyük (>48px) başlıklarda mobile font mutlaka tanımlı

HER GÖRSEL/BUTON WIDGET'INDA ZORUNLU:
  ✓ Image width: desktop + tablet + mobile tanımlı
  ✓ Button padding: mobile için daraltılmış
  ✓ Button font-size: mobile için tanımlı

HER HTML WIDGET'INDA ZORUNLU (EN KRİTİK):
  ✓ <style> bloğu içinde @media (max-width: 1024px) - TABLET
  ✓ <style> bloğu içinde @media (max-width: 767px) - MOBILE
  ✓ Tüm font-size değerleri 3 breakpoint için tanımlı
  ✓ Tüm padding değerleri 3 breakpoint için tanımlı
  ✓ Grid/flex yapılar mobile'da tek sütuna dönüşmeli
  ✓ Sabit px genişlikli öğeler mobile'da %100'e dönüşmeli
  ✓ Image'lar max-width: 100%; height: auto sahip olmalı

HER SPACER WIDGET'INDA ZORUNLU:
  ✓ space değeri: desktop + tablet + mobile tanımlı
  ✓ Mobile'da en az %40-50 küçültülmüş
```

### Responsive Test Checklist

Her şablon üretildikten sonra bu kontrolleri yap:

```
  [ ] Desktop'ta (1280px+) taşma, sıkışma yok
  [ ] Tablet'te (768-1024px) tüm öğeler okunabilir
  [ ] Mobile'da (320-767px) tek sütuna dönüşüm tamamlanmış
  [ ] Mobile'da yatay scroll YOK
  [ ] Mobile'da font'lar en az 14px
  [ ] Mobile'da butonlar tam genişlikte veya ortalanmış
  [ ] Mobile'da görseller container'ı aşmıyor
  [ ] HTML widget'larda her 3 breakpoint için stil var
```

---

## Tasarım Sadakati Rehberi {#tasarım-sadakati}

### Renk ve Palet
- Referans CSS'ten BİREBİR hex değerlerini çıkar
- Yaklaşık değer KULLANMA — tam değerleri kullan
- İç içe container katmanlarında arka plan renk geçişlerini koru

### Tipografi
- HER metin seviyesi için font ailesi, ağırlık, boyut, satır yüksekliğini eşle
- `typography_typography: "custom"` ile özel ayarları aktifleştir
- Gerekli Google Fonts listesini kullanıcıya bildir

### Boşluk ve Ritim
- Bölüm padding'ini tam olarak eşle
- Container katmanları arasındaki padding farkını koru
- `flex_gap` değerlerini referansa göre ayarla

### Katman Derinliği
- Referanstaki container iç içeliğini taklit et
- Arka plan renk geçişlerini (koyu → açık → beyaz) koru
- Gölge derinliklerini katmana göre ayarla

---

## İçerik Yerleştirme Protokolü {#içerik-yerleştirme}

**KRİTİK — İÇERİK SADAKAT KURALI:**
Kullanıcının verdiği yazılar haricinde ekstradan herhangi bir yazı YAZMA ve alt başlık ATMA.
İçerik birebir kullanıcıdan gelir, senin görevin yalnızca bu içeriği referans tasarımın
görsel diline ve iç içe container yapısına uygun şekilde yerleştirmektir.

### Bölüm Eşleme Stratejisi

```
Kullanıcı İçeriği       →  Elementor Container/Widget Yapısı
───────────────────────────────────────────────────────────────────
1. Bölüm (Hero)         →  container(full,bg) > container(boxed) > heading + text-editor + button
2. Bölüm (Özellikler)   →  container(full) > container(boxed) > container(row) > kart container'ları
3. Bölüm (Detaylar)     →  container(full) > container(boxed) > container(row,60/40) > widget'lar
4. Bölüm (CTA/Kapanış)  →  container(full,accent-bg) > container(boxed,rounded) > heading + button
```

---

## Çıktı Yapısı Şablonu {#çıktı-şablonu}

### Tam Sayfa Örnek Yapısı (Fully Responsive)

Aşağıdaki örnek, tüm widget ve container'larda desktop + tablet + mobile alanlarını
içerir — gerçek şablonlarda ZORUNLU minimum yapıdır:

```json
{
  "title": "Ana Sayfa - Hero + Özellikler + CTA",
  "type": "page",
  "version": "0.4",
  "page_settings": [],
  "content": [
    {
      "id": "hero0001",
      "elType": "container",
      "isInner": false,
      "settings": {
        "content_width": "full",
        "flex_direction": "column",
        "flex_justify_content": "center",
        "flex_align_items": "center",
        "min_height": {"unit": "vh", "size": 70},
        "min_height_tablet": {"unit": "vh", "size": 60},
        "min_height_mobile": {"unit": "vh", "size": 50},
        "padding": {"unit": "px", "top": "100", "right": "24", "bottom": "100", "left": "24", "isLinked": false},
        "padding_tablet": {"unit": "px", "top": "80", "right": "24", "bottom": "80", "left": "24", "isLinked": false},
        "padding_mobile": {"unit": "px", "top": "60", "right": "16", "bottom": "60", "left": "16", "isLinked": false},
        "background_background": "classic",
        "background_color": "#1a1a2e"
      },
      "elements": [
        {
          "id": "hero0002",
          "elType": "container",
          "isInner": true,
          "settings": {
            "content_width": "boxed",
            "width": {"unit": "px", "size": 900},
            "width_tablet": {"unit": "%", "size": 90},
            "width_mobile": {"unit": "%", "size": 100},
            "flex_direction": "column",
            "flex_align_items": "center",
            "flex_gap": {"column": "24", "row": "24", "unit": "px", "isLinked": true},
            "flex_gap_tablet": {"column": "20", "row": "20", "unit": "px", "isLinked": true},
            "flex_gap_mobile": {"column": "16", "row": "16", "unit": "px", "isLinked": true}
          },
          "elements": [
            {
              "id": "hero0003",
              "elType": "widget",
              "widgetType": "heading",
              "isInner": false,
              "settings": {
                "title": "Ana Başlık Buraya",
                "header_size": "h1",
                "align": "center",
                "title_color": "#ffffff",
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": {"unit": "px", "size": 56},
                "typography_font_size_tablet": {"unit": "px", "size": 42},
                "typography_font_size_mobile": {"unit": "px", "size": 32},
                "typography_font_weight": "700",
                "typography_line_height": {"unit": "em", "size": 1.15},
                "typography_line_height_mobile": {"unit": "em", "size": 1.25}
              },
              "elements": []
            },
            {
              "id": "hero0004",
              "elType": "widget",
              "widgetType": "text-editor",
              "isInner": false,
              "settings": {
                "editor": "<p style='text-align:center;'>Alt açıklama metni buraya gelir.</p>",
                "text_color": "#cbd5e0",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": 18},
                "typography_font_size_tablet": {"unit": "px", "size": 16},
                "typography_font_size_mobile": {"unit": "px", "size": 15},
                "typography_line_height": {"unit": "em", "size": 1.6}
              },
              "elements": []
            },
            {
              "id": "hero0005",
              "elType": "widget",
              "widgetType": "button",
              "isInner": false,
              "settings": {
                "text": "Başla",
                "link": {"url": "#", "is_external": "", "nofollow": ""},
                "align": "center",
                "background_color": "#2563eb",
                "button_text_color": "#ffffff",
                "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": true},
                "text_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": false},
                "text_padding_mobile": {"unit": "px", "top": "14", "right": "24", "bottom": "14", "left": "24", "isLinked": false},
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": 16},
                "typography_font_size_mobile": {"unit": "px", "size": 15},
                "typography_font_weight": "600"
              },
              "elements": []
            }
          ]
        }
      ]
    }
  ]
}
```

**NOT:** Örnekte dikkat edilmesi gereken responsive alanlar:

- Her container'da `padding` + `padding_tablet` + `padding_mobile`
- Her container'da `flex_gap` + `flex_gap_tablet` + `flex_gap_mobile`
- Genişlik değerleri: px'den %'ye geçiş (mobile'da daha esnek)
- Her heading'de `typography_font_size` + `_tablet` + `_mobile`
- H1 ve H2'de `typography_line_height_mobile` (mobile'da satırlar daha rahat)
- Button'da `text_padding_mobile` ve `typography_font_size_mobile`
- Min-height değerleri her breakpoint için ayrı

---

## Kalite Kontrol Listesi {#kalite-kontrolü}

### Elementor Uyumluluk Kontrolleri

- [ ] Üst seviye yapı doğru: `title`, `type: "page"`, `version: "0.4"`, `page_settings`, `content`
- [ ] JSON dosyası `json.dumps()` ile üretilmiş (escape hataları yok)
- [ ] JSON dosyası valid — `python -m json.tool` ile doğrulanmış
- [ ] Her element'te `id`, `elType`, `settings`, `elements` alanları mevcut
- [ ] `id` değerleri benzersiz (hiçbir id tekrarlanmıyor)
- [ ] Container'larda `elType: "container"` kullanılmış
- [ ] Widget'larda `elType: "widget"` ve `widgetType` kullanılmış
- [ ] `isInner` doğru set edilmiş (en dış `false`, iç içeler `true`)
- [ ] `settings` her zaman object `{}`, hiçbir yerde array `[]` DEĞİL (boş olsa bile)
- [ ] `elements` her zaman array `[]`
- [ ] Eski `section`/`column` yapısı KULLANILMAMIŞ — sadece `container`

### Yapısal Kontroller

- [ ] İç içe elementler doğru nest edilmiş
- [ ] Her container kendi içinde düzgün yapılanmış
- [ ] Widget'ların altında başka elementler YOK (nested widget'lar hariç)
- [ ] Container'lar hem container hem widget nest edebiliyor

### İç İçe Container Kontrolleri

- [ ] Her bölümde minimum 2 katman container var
- [ ] Kart bölümlerinde minimum 3 katman var
- [ ] Katmanlar arası arka plan renk kontrastı var
- [ ] Her katmanda uygun padding tanımlanmış
- [ ] Düz, tek katmanlı container dizilimi YOK
- [ ] Monoton (her bölüm aynı yapıda) düzen YOK

### Tasarım Kalitesi Kontrolleri

- [ ] Renk paleti referansla birebir eşleşiyor
- [ ] Font boyutları, ağırlıkları seviye bazında eşleşiyor
- [ ] Boşluk/padding referans ritmiyle eşleşiyor
- [ ] Gölge ve border-radius değerleri referansla eşleşiyor
- [ ] Referansta OLMAYAN süsleme EKLENMEMİŞ
- [ ] Jenerik AI estetiği YOK

### Responsive Kontroller (GENİŞLETİLMİŞ — HER ŞABLONDA ZORUNLU)

#### Container Responsive Kontrolleri
- [ ] Tüm dış container'larda `padding_tablet` ve `padding_mobile` tanımlı
- [ ] Tüm iç container'larda `padding_tablet` ve `padding_mobile` tanımlı
- [ ] Tüm container'larda `flex_gap_tablet` ve `flex_gap_mobile` tanımlı
- [ ] Row layout container'larda `flex_direction_mobile: "column"` set edilmiş
- [ ] Row layout container'larda gerekirse `flex_direction_tablet` set edilmiş
- [ ] Sütunlarda `width_tablet` ve `width_mobile` tanımlı
- [ ] 3 sütunlu düzen tablet'te 2'ye, mobile'da 1'e düşüyor
- [ ] 4 sütunlu düzen tablet'te 2'ye, mobile'da 1'e düşüyor

#### Widget Responsive Kontrolleri
- [ ] Tüm heading'lerde `typography_font_size_tablet` ve `typography_font_size_mobile` tanımlı
- [ ] Tüm text-editor'larda `typography_font_size_mobile` tanımlı
- [ ] H1 ve H2'de `typography_line_height_mobile` tanımlı
- [ ] Tüm image widget'larında `width_tablet` ve `width_mobile` tanımlı
- [ ] Tüm button'larda `text_padding_mobile` tanımlı
- [ ] Tüm spacer'larda `space_tablet` ve `space_mobile` tanımlı (desktop'un %50-70'i)
- [ ] Icon-box'larda `title_typography_font_size_mobile` tanımlı

#### HTML Widget Responsive Kontrolleri (EN KRİTİK)
- [ ] Her HTML widget'ın başında `<style>` bloğu var
- [ ] Her style bloğunda `@media (max-width: 1024px)` TABLET kuralı var
- [ ] Her style bloğunda `@media (max-width: 767px)` MOBILE kuralı var
- [ ] Desktop'taki her font-size değerinin tablet + mobile karşılığı var
- [ ] Desktop'taki her padding değerinin tablet + mobile karşılığı var
- [ ] Grid yapılar mobile'da `grid-template-columns: 1fr`'e dönüşüyor
- [ ] Flex row yapılar mobile'da `flex-direction: column`'a dönüşüyor
- [ ] Sabit px genişlikli öğeler mobile'da `width: 100%` veya `max-width: 100%`
- [ ] Tüm `img` elementlerinde `max-width: 100%; height: auto`
- [ ] CSS sınıflarında `wps-` prefix'i kullanılmış (tema çakışması önleme)
- [ ] Mobile breakpoint'inde gap/margin değerleri azaltılmış

#### Genel Responsive Kontrolleri
- [ ] Mobile'da hiçbir yerde yatay scroll oluşmuyor
- [ ] Mobile'da en küçük font 14px'ten küçük değil
- [ ] Mobile'da butonlar yeterince tıklanabilir boyutta (min 44x44px hedef)
- [ ] Görseller mobile'da viewport'u aşmıyor
- [ ] Mobile'da padding değerleri 16px'ten küçük değil (yan kenarlarda)

### İçerik Kontrolleri

- [ ] Tüm kullanıcı içerikleri doğru sırada yerleştirilmiş
- [ ] Ekstra metin EKLENMEMİŞ
- [ ] Header/footer dahil EDİLMEMİŞ (sayfa içeriği olarak)
- [ ] Görsel URL'leri placeholder veya referans kullanıcı talimatlı

---

## Sık Yapılan Hatalar ve Düzeltmeleri {#sık-hatalar}

| # | Hata | Düzeltme |
|---|------|----------|
| 1 | Geçersiz JSON (escape hatası) | Python `json.dumps()` ile oluştur, elle yazma |
| 2 | `version` alanı yanlış | Her zaman `"0.4"` olmalı (string, float DEĞİL) |
| 3 | `type` alanı eksik/yanlış | `"page"`, `"section"`, `"header"`, `"footer"` gibi geçerli değerlerden biri |
| 4 | `settings` array olarak yazılmış | Boş olsa bile `{}` kullan, `[]` DEĞİL |
| 5 | `elements` object olarak yazılmış | Her zaman `[]` array olmalı |
| 6 | `id` değeri tekrarlanıyor | Her element için benzersiz 8 karakterlik id üret |
| 7 | Widget'ta `widgetType` eksik | Her widget elementinde zorunlu |
| 8 | Eski `section`/`column` yapısı kullanılmış | Sadece modern `container` kullan |
| 9 | `isInner` değeri yanlış | En dış `false`, iç içedekiler `true` |
| 10 | Düz container dizilimi (iç içe yok) | Her bölümü min. 2 katman container ile sar |
| 11 | Tüm bölümlerde aynı arka plan | Dönüşümlü arka plan renkleri kullan |
| 12 | Padding formatı yanlış | `{unit, top, right, bottom, left, isLinked}` formatında olmalı |
| 13 | Tipografi özel ayar aktif değil | `typography_typography: "custom"` ekle |
| 14 | Responsive değerler eksik | `_tablet` ve `_mobile` versiyonlarını ekle |
| 15 | Font bilgisi eksik | Kullanıcıya hangi Google Font'ların gerektiğini bildir |
| 16 | Flex layout için eski yapı | `flex_direction`, `flex_justify_content`, `flex_align_items` kullan |
| 17 | Background formatı eksik | `background_background: "classic"` + `background_color` ikisi birlikte |
| 18 | `width` formatı yanlış | `{unit, size}` nesnesi olarak yazılmalı |
| 19 | Pro widget kullanılmış | Sadece Free widget'ları kullan |
| 20 | Monoton kart tasarımı | Bölümlere göre farklı kart varyasyonları kullan |
| 21 | HTML widget'ta media query yok | Her HTML widget'ta `<style>` bloğu ve 2 media query zorunlu |
| 22 | HTML widget'ta font-size sadece desktop | Tablet + mobile için `@media` query'lerinde font-size'ları tanımla |
| 23 | HTML widget'ta grid/flex mobile'da bozuluyor | Mobile media query'sinde `grid-template-columns: 1fr` veya `flex-direction: column` |
| 24 | Container'da responsive padding eksik | `padding_tablet` ve `padding_mobile` her container'da zorunlu |
| 25 | Row container mobile'da yatay kalıyor | `flex_direction_mobile: "column"` eklenmemiş |
| 26 | Sütun widget'ları mobile'da taşıyor | `width_mobile: 100%` tanımlanmamış |
| 27 | Büyük başlık mobile'da ekrana sığmıyor | `typography_font_size_mobile` eksik veya çok büyük |
| 28 | Spacer mobile'da çok büyük | `space_mobile` desktop değerinin %50-60'ı olmalı |
| 29 | Flex gap mobile'da sıkışık | `flex_gap_mobile` küçültülmeli (16px gibi) |
| 30 | HTML widget'ta görsel taşıyor | `img { max-width: 100%; height: auto; }` eklenmemiş |
| 31 | CSS class isimleri tema ile çakışıyor | `wps-` prefix kullan (`.wps-card`, `.wps-grid` gibi) |
| 32 | Mobile'da yatay scroll oluşuyor | Tüm sabit genişlikleri `max-width: 100%` ile sınırla |
| 33 | Icon-box başlıkları mobile'da büyük | `title_typography_font_size_mobile` tanımla |
| 34 | Image genişliği mobile'da orantısız | `width_mobile: 100%` veya uygun yüzde tanımla |

---

## Son Çıktı Protokolü {#son-çıktı}

### JSON Üretim Süreci

1. **Referans URL'yi `web_fetch` ile çek** ve tasarımı analiz et
2. **Tasarım token haritasını oluştur** (renkler, fontlar, boşluklar, katmanlar)
3. **Container yapısını planla** — her bölüm için iç içe container mimarisini belirle
4. **Element ağacını Python ile oluştur** — unique id'ler üret, settings'leri doldur
5. **JSON dosyasını Python ile üret** — escape hatası olmaması için `json.dumps()` kullan
6. **JSON'u doğrula** — `python -m json.tool` ile kontrol et
7. **Dosyayı `/mnt/user-data/outputs/elementor-template.json` olarak kaydet**
8. **`present_files` ile kullanıcıyla paylaş**

### Python ile JSON Üretim Kodu (Responsive Destekli)

```python
import json
import uuid

def gen_id():
    """Elementor uyumlu 8 karakterlik benzersiz id üret"""
    return uuid.uuid4().hex[:8]

def responsive_value(desktop, tablet=None, mobile=None, unit="px"):
    """Desktop/tablet/mobile değerleri otomatik üret.
    Verilmeyenler desktop'un %75 (tablet) ve %60 (mobile) olarak hesaplanır."""
    if tablet is None:
        tablet = round(desktop * 0.75)
    if mobile is None:
        mobile = round(desktop * 0.60)
    return {
        "desktop": {"unit": unit, "size": desktop},
        "tablet": {"unit": unit, "size": tablet},
        "mobile": {"unit": unit, "size": mobile}
    }

# ===== WIDGET OLUŞTURUCULAR (Responsive Dahil) =====

def make_heading(title, level="h2", color="#1a1a2e", font_size=32, align="center"):
    """Responsive heading widget — font_size otomatik tablet/mobile üretir"""
    rv = responsive_value(font_size)
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": "heading",
        "isInner": False,
        "settings": {
            "title": title,
            "header_size": level,
            "align": align,
            "title_color": color,
            "typography_typography": "custom",
            "typography_font_size": rv["desktop"],
            "typography_font_size_tablet": rv["tablet"],
            "typography_font_size_mobile": rv["mobile"],
            "typography_font_weight": "700",
            "typography_line_height": {"unit": "em", "size": 1.2},
            "typography_line_height_mobile": {"unit": "em", "size": 1.3}
        },
        "elements": []
    }

def make_text(html_content, color="#4a5568", font_size=17):
    """Responsive text-editor widget"""
    rv = responsive_value(font_size, tablet=max(font_size-1, 15), mobile=max(font_size-2, 14))
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": "text-editor",
        "isInner": False,
        "settings": {
            "editor": html_content,
            "text_color": color,
            "typography_typography": "custom",
            "typography_font_size": rv["desktop"],
            "typography_font_size_tablet": rv["tablet"],
            "typography_font_size_mobile": rv["mobile"],
            "typography_line_height": {"unit": "em", "size": 1.7},
            "typography_line_height_mobile": {"unit": "em", "size": 1.6}
        },
        "elements": []
    }

def make_button(text, url="#", bg_color="#2563eb", text_color="#ffffff"):
    """Responsive button widget"""
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": "button",
        "isInner": False,
        "settings": {
            "text": text,
            "link": {"url": url, "is_external": "", "nofollow": ""},
            "align": "center",
            "background_color": bg_color,
            "button_text_color": text_color,
            "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
            "text_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": False},
            "text_padding_mobile": {"unit": "px", "top": "14", "right": "24", "bottom": "14", "left": "24", "isLinked": False},
            "typography_typography": "custom",
            "typography_font_size": {"unit": "px", "size": 16},
            "typography_font_size_mobile": {"unit": "px", "size": 15},
            "typography_font_weight": "600"
        },
        "elements": []
    }

def make_spacer(height=60):
    """Responsive spacer widget"""
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": "spacer",
        "isInner": False,
        "settings": {
            "space": {"unit": "px", "size": height},
            "space_tablet": {"unit": "px", "size": round(height * 0.75)},
            "space_mobile": {"unit": "px", "size": round(height * 0.5)}
        },
        "elements": []
    }

def make_html(html_code):
    """HTML widget — html_code içinde responsive CSS media query'leri OLMALI"""
    # UYARI: html_code mutlaka <style> bloğu + media query'ler içermeli
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": "html",
        "isInner": False,
        "settings": {
            "html": html_code
        },
        "elements": []
    }

# ===== CONTAINER OLUŞTURUCULAR (Responsive Dahil) =====

def make_outer_container(bg_color="#f8f9fa", children=None, padding_top=80, padding_bottom=80):
    """Full-width dış container — tam responsive padding"""
    pt_tablet = round(padding_top * 0.75)
    pt_mobile = round(padding_top * 0.5)
    pb_tablet = round(padding_bottom * 0.75)
    pb_mobile = round(padding_bottom * 0.5)
    
    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": False,
        "settings": {
            "content_width": "full",
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"unit": "px", "top": str(padding_top), "right": "24", "bottom": str(padding_bottom), "left": "24", "isLinked": False},
            "padding_tablet": {"unit": "px", "top": str(pt_tablet), "right": "24", "bottom": str(pb_tablet), "left": "24", "isLinked": False},
            "padding_mobile": {"unit": "px", "top": str(pt_mobile), "right": "16", "bottom": str(pb_mobile), "left": "16", "isLinked": False},
            "background_background": "classic",
            "background_color": bg_color
        },
        "elements": children or []
    }

def make_boxed_container(max_width=1200, bg_color=None, children=None, gap=32):
    """Boxed (merkezde hizalı) container — tam responsive gap ve width"""
    settings = {
        "content_width": "boxed",
        "width": {"unit": "px", "size": max_width},
        "width_tablet": {"unit": "%", "size": 90},
        "width_mobile": {"unit": "%", "size": 100},
        "flex_direction": "column",
        "flex_gap": {"column": str(gap), "row": str(gap), "unit": "px", "isLinked": True},
        "flex_gap_tablet": {"column": str(round(gap*0.75)), "row": str(round(gap*0.75)), "unit": "px", "isLinked": True},
        "flex_gap_mobile": {"column": str(round(gap*0.5)), "row": str(round(gap*0.5)), "unit": "px", "isLinked": True}
    }
    if bg_color:
        settings["background_background"] = "classic"
        settings["background_color"] = bg_color
        settings["padding"] = {"unit": "px", "top": "40", "right": "40", "bottom": "40", "left": "40", "isLinked": True}
        settings["padding_tablet"] = {"unit": "px", "top": "32", "right": "32", "bottom": "32", "left": "32", "isLinked": True}
        settings["padding_mobile"] = {"unit": "px", "top": "24", "right": "24", "bottom": "24", "left": "24", "isLinked": True}
        settings["border_radius"] = {"unit": "px", "top": "16", "right": "16", "bottom": "16", "left": "16", "isLinked": True}
    
    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": True,
        "settings": settings,
        "elements": children or []
    }

def make_row_container(children=None, column_count=3, gap=32):
    """Row layout container — mobile'da otomatik column'a döner"""
    # column_count bazlı sütun genişlikleri
    widths = {2: 50, 3: 33.33, 4: 25}
    desktop_width = widths.get(column_count, 33.33)
    
    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": True,
        "settings": {
            "content_width": "full",
            "flex_direction": "row",
            "flex_direction_mobile": "column",  # MOBILE'DA DIKEY!
            "flex_wrap": "wrap",
            "flex_gap": {"column": str(gap), "row": str(gap), "unit": "px", "isLinked": True},
            "flex_gap_tablet": {"column": str(round(gap*0.75)), "row": str(round(gap*0.75)), "unit": "px", "isLinked": True},
            "flex_gap_mobile": {"column": str(round(gap*0.5)), "row": str(round(gap*0.5)), "unit": "px", "isLinked": True}
        },
        "elements": children or []
    }

def make_column_container(width_desktop=33.33, width_tablet=50, width_mobile=100, bg_color=None, children=None):
    """Row içindeki sütun — otomatik responsive width"""
    settings = {
        "content_width": "boxed",
        "width": {"unit": "%", "size": width_desktop},
        "width_tablet": {"unit": "%", "size": width_tablet},
        "width_mobile": {"unit": "%", "size": width_mobile},
        "flex_direction": "column",
        "flex_gap": {"column": "16", "row": "16", "unit": "px", "isLinked": True},
        "padding": {"unit": "px", "top": "32", "right": "32", "bottom": "32", "left": "32", "isLinked": True},
        "padding_mobile": {"unit": "px", "top": "24", "right": "20", "bottom": "24", "left": "20", "isLinked": True}
    }
    if bg_color:
        settings["background_background"] = "classic"
        settings["background_color"] = bg_color
        settings["border_radius"] = {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
    
    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": True,
        "settings": settings,
        "elements": children or []
    }

# ===== RESPONSIVE HTML WIDGET HELPER =====

def make_responsive_html(html_body, styles_desktop="", styles_tablet="", styles_mobile=""):
    """HTML widget'ı otomatik media query'li CSS ile sar"""
    full_html = f"""<style>
{styles_desktop}

@media (max-width: 1024px) {{
{styles_tablet}
}}

@media (max-width: 767px) {{
{styles_mobile}
}}
</style>

{html_body}"""
    
    return make_html(full_html)

# ===== SAYFA YAPISINI KUR =====

hero_section = make_outer_container(
    bg_color="#1a1a2e",
    padding_top=100,
    padding_bottom=100,
    children=[
        make_boxed_container(
            max_width=900,
            children=[
                make_heading("Ana Başlık", level="h1", color="#ffffff", font_size=56),
                make_text("<p style='text-align:center;'>Açıklama metni</p>", color="#cbd5e0"),
                make_button("Başla", url="#", bg_color="#2563eb")
            ]
        )
    ]
)

# Elementor JSON şablon formatı
template_data = {
    "title": "Sayfa Şablonu",
    "type": "page",
    "version": "0.4",
    "page_settings": [],
    "content": [hero_section]
}

# Dosyaya yaz
output_path = '/mnt/user-data/outputs/elementor-template.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(template_data, f, ensure_ascii=False, indent=2)

# Doğrulama
with open(output_path, 'r', encoding='utf-8') as f:
    validated = json.load(f)
    print("✓ JSON geçerli")
    print(f"✓ type: {validated['type']}")
    print(f"✓ version: {validated['version']}")
    print(f"✓ content element sayısı: {len(validated['content'])}")
```

### Kullanıcıya İletilecek Bilgiler

JSON dosyasıyla birlikte kullanıcıya şunları bildir:

1. **Gerekli Google Fonts** — WordPress tema ayarlarından veya Elementor Site Settings'ten yüklenmesi gereken fontlar
2. **Görsel alanları** — Hangi görsellerin WordPress Medya Kütüphanesi'nden manuel eklenmesi gerektiği (Elementor JSON'da görseller URL ile referanslanır, otomatik aktarılmaz)
3. **Elementor'a Aktarım Adımları:**

   ```
   1. WordPress yönetim paneline gir
   2. Sol menüden: Şablonlar (Templates) → Kayıtlı Şablonlar (Saved Templates)
   3. Üstteki "Şablonları İçe Aktar" (Import Templates) butonuna tıkla
   4. JSON dosyasını seç ve yükle
   5. "Şimdi İçe Aktar" (Import Now) butonuna bas
   6. Şablon listende yeni şablonun görünecek
   7. Yeni sayfa oluştur → Elementor ile düzenle
   8. Alt menüdeki klasör ikonuna tıkla (Template Library)
   9. "My Templates" sekmesine geç
   10. Şablonunun yanındaki "Insert" butonuna tıkla
   ```

4. **Önemli Uyarılar:**
   - Elementor eklentisinin yüklü ve aktif olması gerekli
   - Elementor versiyonu 3.6 veya üzeri olmalı (Flexbox Container desteği için)
   - Görseller manuel olarak WordPress Media'ya yüklenip Elementor'da güncellenmeli
   - Font Awesome ikonları için Elementor'da FA kütüphanesi aktif olmalı
   - Pro widget kullanılmadı; yalnızca Free versiyonla çalışır

### Dosya Adlandırma

- Varsayılan: `elementor-template.json`
- Kullanıcı belirtirse özelleştirilebilir (örn. `anasayfa-elementor.json`)

**UNUTMA:** JSON geçerli olmalı, element yapısı düzgün iç içe geçmeli, ve her bölüm
katmanlı container mimarisiyle estetik derinlik taşımalıdır. Sadece Elementor Free
widget'ları kullanılmalı — pro özellikler YASAK.

**DİL KURALI:** Sayfa içerikleri, başlıklar, açıklamalar ve tüm kullanıcıya
görünür metin — hepsi kullanıcının dilinde olacak. JSON alan adları (key'ler)
teknik olduğu için İngilizce kalır, ama değerler (title, text, vb.) kullanıcının
dilindedir.
