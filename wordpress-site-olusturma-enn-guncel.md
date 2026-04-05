---
name: wp-elementor-json
description: >
  Referans bir web sitesi URL'sinden tasarım dilini analiz edip, Elementor Template Library
  içe aktarıcısıyla doğrudan yüklenebilecek JSON formatında sayfa çıktısı üret. Kullanıcı
  URL'yi paylaşır, web_fetch ile çekilir, tasarımı analiz edilir ve Elementor'ın native
  Flexbox Container yapısıyla iç içe konteynerler, katmanlı düzenler ve estetik tasarımlar
  üretilir. Çıktı, WordPress yönetim panelinde Şablonlar > Kayıtlı Şablonlar > İçe Aktar
  menüsünden JSON dosyası olarak doğrudan yüklenir ve sayfaya eklenir. Anahtar kelimeler:
  "Elementor JSON", "Elementor şablon", "Elementor içe aktar", "Template Library import",
  "Flexbox Container", "iç içe konteyner", "bu siteye benzer", "bu URL gibi yap",
  "Elementor template", "JSON şablon", "Elementor tasarım".
---

# Elementor JSON Şablon Üretici — URL Referanslı, Flexbox Container Tabanlı

Referans bir web sitesinin URL'sinden tasarım dilini analiz edip, Elementor Template
Library'ye doğrudan içe aktarılabilecek JSON formatında, iç içe Flexbox Container
yapılarıyla estetik sayfa şablonları üret.

**Bu skill YALNIZCA Elementor tasarımları için kullanılır.**
**Gutenberg blok editörü formatı ÜRETMEZ.**

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

### HTML Widget (Özel Bileşenler)

```json
{
  "id": "htm00001",
  "elType": "widget",
  "widgetType": "html",
  "isInner": false,
  "settings": {
    "html": "<div style='padding:20px;background:#f0f0f0;border-radius:8px;'><p>Özel HTML içeriği</p></div>"
  },
  "elements": []
}
```

---

## Responsive Tasarım Kuralları {#responsive}

Elementor otomatik olarak 3 breakpoint kullanır: **Desktop**, **Tablet**, **Mobile**.

### Responsive Değer Formatı

Herhangi bir ayar için responsive değer ekle:

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

### Sütun Genişlikleri (Row Container İçinde)

```json
// Desktop: 3 sütun
"width": {"unit": "%", "size": 33.33},
// Tablet: 2 sütun
"width_tablet": {"unit": "%", "size": 50},
// Mobile: 1 sütun
"width_mobile": {"unit": "%", "size": 100}
```

### Flex Direction Responsive

```json
// Desktop: yatay
"flex_direction": "row",
// Mobile: dikey
"flex_direction_mobile": "column"
```

### Tipografi Responsive

```json
"typography_font_size": {"unit": "px", "size": 48},
"typography_font_size_tablet": {"unit": "px", "size": 36},
"typography_font_size_mobile": {"unit": "px", "size": 28}
```

### Responsive Zorunluluklar

```
ZORUNLU:
  ✓ Tüm bölüm padding'lerinde tablet + mobile versiyonları tanımla
  ✓ Row container'larda mobile'da flex_direction_mobile: "column" ekle
  ✓ Sütun widget'larında mobile'da width_mobile: 100% yap
  ✓ Büyük başlıklarda tablet + mobile font_size tanımla
  ✓ Gap değerlerinde mobile için küçük değerler tanımla
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

### Tam Sayfa Örnek Yapısı

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
        "padding": {"unit": "px", "top": "100", "right": "24", "bottom": "100", "left": "24", "isLinked": false},
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
            "flex_direction": "column",
            "flex_align_items": "center",
            "flex_gap": {"column": "24", "row": "24", "unit": "px", "isLinked": true}
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
                "typography_line_height": {"unit": "em", "size": 1.15}
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
                "text_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": false}
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

### Responsive Kontroller

- [ ] Bölüm padding'lerinde `_tablet` ve `_mobile` versiyonları var
- [ ] Row container'larda mobile için `flex_direction_mobile: "column"` var
- [ ] Sütunlarda `width_mobile: 100%` tanımlanmış
- [ ] Büyük font'larda mobile boyutları tanımlanmış

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

### Python ile JSON Üretim Kodu

```python
import json
import uuid

def gen_id():
    """Elementor uyumlu 8 karakterlik benzersiz id üret"""
    return uuid.uuid4().hex[:8]

# Widget oluşturucu
def make_heading(title, level="h2", color="#1a1a2e", font_size=32):
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": "heading",
        "isInner": False,
        "settings": {
            "title": title,
            "header_size": level,
            "align": "center",
            "title_color": color,
            "typography_typography": "custom",
            "typography_font_size": {"unit": "px", "size": font_size},
            "typography_font_weight": "700",
            "typography_line_height": {"unit": "em", "size": 1.2}
        },
        "elements": []
    }

def make_text(html_content, color="#4a5568"):
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": "text-editor",
        "isInner": False,
        "settings": {
            "editor": html_content,
            "text_color": color,
            "typography_typography": "custom",
            "typography_font_size": {"unit": "px", "size": 17},
            "typography_line_height": {"unit": "em", "size": 1.7}
        },
        "elements": []
    }

# Container oluşturucu
def make_outer_container(bg_color="#f8f9fa", children=None):
    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": False,
        "settings": {
            "content_width": "full",
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"unit": "px", "top": "80", "right": "24", "bottom": "80", "left": "24", "isLinked": False},
            "padding_mobile": {"unit": "px", "top": "48", "right": "16", "bottom": "48", "left": "16", "isLinked": False},
            "background_background": "classic",
            "background_color": bg_color
        },
        "elements": children or []
    }

def make_boxed_container(max_width=1200, bg_color=None, children=None):
    settings = {
        "content_width": "boxed",
        "width": {"unit": "px", "size": max_width},
        "flex_direction": "column",
        "flex_gap": {"column": "32", "row": "32", "unit": "px", "isLinked": True}
    }
    if bg_color:
        settings["background_background"] = "classic"
        settings["background_color"] = bg_color
        settings["padding"] = {"unit": "px", "top": "40", "right": "40", "bottom": "40", "left": "40", "isLinked": True}
        settings["border_radius"] = {"unit": "px", "top": "16", "right": "16", "bottom": "16", "left": "16", "isLinked": True}
    
    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": True,
        "settings": settings,
        "elements": children or []
    }

# Sayfa yapısını kur
hero_section = make_outer_container(
    bg_color="#1a1a2e",
    children=[
        make_boxed_container(
            max_width=900,
            children=[
                make_heading("Ana Başlık", level="h1", color="#ffffff", font_size=56),
                make_text("<p style='text-align:center;'>Açıklama metni</p>", color="#cbd5e0")
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
