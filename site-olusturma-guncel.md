---
name: wp-embeddable-html
description: >
  Generate WordPress-embeddable, fully isolated single-file HTML code from a reference design
  (ZIP containing HTML/CSS/JS/images). Use this skill whenever a user uploads a ZIP file of a
  website and wants a new page coded in the same design language — specifically for embedding
  inside a WordPress content area (HTML block). Also trigger when the user mentions 'WordPress
  embed', 'WordPress HTML block', 'isolated HTML for WordPress', 'WP içerik alanı', 'tek parça
  kod', or asks to replicate/adapt a site design for WordPress insertion. Trigger even if the
  user just says 'make this design WordPress-compatible' or 'embed this in WordPress'. This skill
  handles CSS scoping, JS isolation via IIFE, removal of global tags, and content sectioning —
  all critical for WordPress compatibility.
---

# WordPress-Embeddable Isolated HTML Generator

Referans bir web sitesi ZIP dosyasından, WordPress HTML bloğuna doğrudan yapıştırılmaya hazır,
tamamen izole, tek parça HTML çıktısı üret.

---

## İçindekiler

1. [Bu Skill Ne Zaman Tetiklenir](#bu-skill-ne-zaman-tetiklenir)
2. [Tasarım Felsefesi — İnsan Eli Değmiş Uzman İşi](#tasarım-felsefesi)
3. [Adım Adım İş Akışı](#adım-adım-iş-akışı)
4. [WordPress İzolasyon Kuralları (KRİTİK)](#wordpress-izolasyon-kuralları-kritik)
5. [Tasarım Sadakati Rehberi](#tasarım-sadakati-rehberi)
6. [İçerik Yerleştirme Protokolü](#içerik-yerleştirme-protokolü)
7. [Çıktı Yapısı Şablonu](#çıktı-yapısı-şablonu)
8. [İleri Teknikler](#ileri-teknikler)
9. [Kalite Kontrol Listesi](#kalite-kontrol-listesi)
10. [Sık Yapılan Hatalar ve Düzeltmeleri](#sık-yapılan-hatalar-ve-düzeltmeleri)
11. [Son Çıktı Protokolü](#son-çıktı-protokolü)

---

## Bu Skill Ne Zaman Tetiklenir

- Kullanıcı bir web sitesi içeren ZIP dosyası yükler (index.html + CSS/JS/görseller)
- Aynı görsel dilde yeni bir sayfa kodlanması istenir
- Çıktı WordPress içerik alanına gömülecektir (HTML bloğu / Özel HTML widget'ı)
- Kullanıcı WordPress gömme, içerik alanı ekleme veya tema izolasyonundan bahseder
- Anahtar kelimeler: "WordPress embed", "WP HTML bloğu", "tek parça kod", "içerik alanı", "izole HTML"

**ÖNEMLİ:** Bu skill, yüklenen referans dosyayı WordPress'e dönüştürmek DEĞİL — referansın
tasarım dilini kullanarak YENİ bir içerik sayfası kodlamaktır.

---

## Tasarım Felsefesi — İnsan Eli Değmiş Uzman İşi {#tasarım-felsefesi}

Bu skill'in ürettiği çıktı, bir yapay zekanın değil, deneyimli bir frontend uzmanının elinden
çıkmış gibi görünmelidir. Aşağıdaki ilkeler HER çıktıda geçerlidir:

### Yapay Zeka Estetiğinden Kaçınma Kuralları

```
YASAK — Tipik AI çıktısı belirtileri:
  ✗ Her yerde aynı mor-mavi gradient
  ✗ Simetrik, robotik, tekdüze grid yapıları
  ✗ Abartılı gölgeler ve parlama efektleri
  ✗ İçerikle alakasız dekoratif öğeler
  ✗ Her bölümde aynı kart tasarımının tekrarı
  ✗ Anlamsız hover efektleri (sadece renk değişimi)
  ✗ Her şeyin yuvarlak köşeli kutular içinde olması
  ✗ Inter, Roboto, Arial gibi jenerik fontlar (referansta yoksa)
  ✗ Gereksiz animasyonlar ve geçiş efektleri
```

### Uzman Tasarımcı Kalitesi Kuralları

```
ZORUNLU — Profesyonel uzman dokunuşu:
  ✓ Referans tasarıma birebir sadakat
  ✓ Kasıtlı ve anlamlı beyaz alan (white space) kullanımı
  ✓ Tutarlı ama monoton olmayan görsel ritim
  ✓ İçeriğe uygun, bağlamsal tipografi seçimleri
  ✓ Asimetrik düzenlerden korkmamak (referans gerektiriyorsa)
  ✓ Detaylara özen: satır yüksekliği, harf aralığı, ince kenarlıklar
  ✓ Hover efektlerinde incelik: ölçek, gölge derinliği, renk tonu kayması
  ✓ Doğal görünen geçişler (ease-out, cubic-bezier — linear YASAK)
  ✓ Mikro-detaylar: ince ayırıcı çizgiler, accent renkli küçük vurgular
  ✓ İçerik hiyerarşisinde net basamaklar (her heading seviyesi ayırt edilebilir)
```

### Tasarım Kararları Hiyerarşisi

Karar verirken bu sırayı izle:

1. **Referans tasarım ne yapıyorsa → onu yap** (birincil kaynak)
2. **Referansta yoksa → sektör standartlarına bak** (aynı sektördeki premium siteler)
3. **Sektör standardı da belirsizse → minimal ve temiz tut** (az çok'tan iyidir)

**ASLA kendi başına süsleme ekleme.** Referansta olmayan dekoratif öğe, gradient, gölge veya
efekt eklenmez. Eksik bırakmak, fazla eklemekten her zaman daha iyidir.

---

## Adım Adım İş Akışı

### Faz 1: ZIP'i Çıkar ve Analiz Et

```bash
# Çalışma alanı oluştur
mkdir -p /home/claude/wp-work
cp /mnt/user-data/uploads/*.zip /home/claude/wp-work/
cd /home/claude/wp-work

# Çıkar
unzip -o *.zip -d extracted/

# Dosya yapısını listele
find extracted/ -type f | head -80
```

Her dosya türünü incele:

| Dosya Türü | Ne Çıkarılacak |
|-----------|----------------|
| `index.html` (ve diğer .html) | DOM yapısı, bölüm düzeni, sınıf adlandırma kalıpları, bileşen desenleri, semantik hiyerarşi |
| `.css` dosyaları | Renk paleti, font aileleri, boşluk sistemi, grid/flexbox desenleri, animasyonlar, hover durumları, gölgeler, border-radius, responsive kırılma noktaları |
| `.js` dosyaları | Etkileşimli davranışlar (slider, akordeon, tab, scroll efektleri, sayaçlar, modal, lazy loading) |
| Görseller (`.png`, `.jpg`, `.svg`, `.webp`) | Hero banner'lar, ikonlar, arka plan desenleri, dekoratif öğeler — boyut ve kullanım bağlamını not et |
| Font dosyaları (`.woff`, `.woff2`, `.ttf`) | Google Fonts'ta olmayan özel fontlar — base64 gömme veya harici URL gerekecek |

**HER CSS ve JS dosyasını BAŞTAN SONA oku.** Göz gezdirme YASAK. Tasarım sadakati her
görsel detayı anlamaya bağlıdır.

### Faz 2: Tasarım Token Haritası Oluştur

Kod yazmadan ÖNCE bu token'ları açıkça belgele. Bu zorunludur:

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
  Metin Soluk:              #______
  Arka Plan:                #ffffff  (ZORUNLU — daima beyaz)
  Yüzey/Kart Arka Planı:   #______
  Kenarlık Rengi:           #______

TİPOGRAFİ:
  Başlık Fontu:     '________', ________
  Gövde Fontu:      '________', ________
  UI/Accent Fontu:  '________', ________ (farklıysa)
  H1:  __px  |  Ağırlık: __  |  Satır Yüksekliği: __
  H2:  __px  |  Ağırlık: __  |  Satır Yüksekliği: __
  H3:  __px  |  Ağırlık: __  |  Satır Yüksekliği: __
  H4:  __px  |  Ağırlık: __  |  Satır Yüksekliği: __
  Gövde: __px | Ağırlık: __  |  Satır Yüksekliği: __
  Küçük Metin: __px | Ağırlık: __ | Satır Yüksekliği: __
  Harf Aralığı:     __px veya __em (varsa)

BOŞLUKLAR:
  Bölüm Padding (Masaüstü):   __px üst / __px alt
  Bölüm Padding (Tablet):     __px üst / __px alt
  Bölüm Padding (Mobil):      __px üst / __px alt
  İçerik Boşluğu (grid/flex): __px
  Kart İç Padding:            __px
  Öğe Alt Margin:             __px

DÜZEN:
  Grid Sistemi:        __ sütun  |  Boşluk: __px
  Konteyner Padding:   __px (masaüstü) / __px (mobil)
  Genişlik Stratejisi: Referanstaki max-width değerini aynen kullan
                       (referansta yoksa → width: 100% tam genişlik)

DEKORATİF:
  Border Radius:    __px (kartlar) / __px (butonlar) / __px (görseller)
  Box Shadow:       ______________________________
  Hover Shadow:     ______________________________
  Ayırıcı Stili:    ______________________________
  Vurgu Çizgisi:    ______________________________

GEÇİŞ EFEKTLERİ:
  Transition:       ______________________________
  Hover Efektleri:  ______________________________

RESPONSIVE KIRILMA NOKTALARI:
  Masaüstü:         > ____px
  Tablet:           ____px — ____px
  Mobil:            < ____px
  Küçük Mobil:      < ____px
═══════════════════════════════════════════════
```

### Faz 3: İzole HTML'i Üret

Aşağıdaki **WordPress İzolasyon Kuralları**'na BİREBİR uy. Her kural zorunludur.

Çıktıyı tek bir `.html` dosyası olarak yaz. Karmaşık tasarımlarda (>400 satır) iteratif oluştur:

1. **İlk geçiş:** Semantik bölümlerle HTML iskeleti
2. **İkinci geçiş:** Tüm token'lar uygulanmış eksiksiz CSS
3. **Üçüncü geçiş:** Responsive kırılma noktaları
4. **Dördüncü geçiş:** JavaScript etkileşimleri (gerekiyorsa)
5. **Son geçiş:** Kalite kontrol listesine göre gözden geçirme

---

## WordPress İzolasyon Kuralları (KRİTİK)

Bu kurallar **pazarlıksızdır**. Herhangi birinin ihlali WordPress sitesini BOZAR.

### Kural 1: Kök Etiketler — MUTLAK YASAK

```
YASAK — Bunları ASLA çıktıya yazma:
  <!DOCTYPE html>
  <html>
  <head>
  <body>
  <meta>
  <title>
  <link rel="stylesheet">  (bunun yerine <style> içinde @import kullan)
```

Çıktı DOĞRUDAN sarmalayıcı div ile başlar:
```html
<div id="ozel-tasarim-alani-XXXX">
```

`XXXX` yerine **benzersiz rastgele 4 haneli sayı** kullan (örn: `ozel-tasarim-alani-7429`).
Aynı WordPress sayfasında birden fazla gömme olursa ID çakışmasını önler.

### Kural 2: CSS Kapsamlandırma — HER TEK KURAL

TÜM CSS seçicileri `#ozel-tasarim-alani-XXXX` ile başlaMALIDIR. Sıfır istisna.

```css
/* ═══ YANLIŞ — WordPress temasına sızar ═══ */
h1 { font-size: 36px; }
.card { padding: 20px; }
* { box-sizing: border-box; }
a { color: blue; }
img { max-width: 100%; }
p { margin-bottom: 1em; }
ul { list-style: disc; }

/* ═══ DOĞRU — Sadece kendi alanımızı hedefler ═══ */
#ozel-tasarim-alani-XXXX h1 { font-size: 36px; }
#ozel-tasarim-alani-XXXX .ozel-card { padding: 20px; }
#ozel-tasarim-alani-XXXX *,
#ozel-tasarim-alani-XXXX *::before,
#ozel-tasarim-alani-XXXX *::after { box-sizing: border-box; }
#ozel-tasarim-alani-XXXX a { color: blue; }
#ozel-tasarim-alani-XXXX img { max-width: 100%; height: auto; display: block; }
#ozel-tasarim-alani-XXXX p { margin-bottom: 1em; }
#ozel-tasarim-alani-XXXX ul { list-style: disc; }
```

**Ek CSS Kapsamlandırma Gereksinimleri:**

```css
/* CSS Özel Değişkenler — :root DEĞİL, sarmalayıcıya tanımla */
#ozel-tasarim-alani-XXXX {
  --ozel-primary: #2563eb;
  --ozel-secondary: #1e40af;
  --ozel-accent: #f59e0b;
  /* Tema çakışmasını önlemek için değişken adlarına 'ozel-' önek ekle */
}

/* @keyframes — animasyon adlarına önek ekle */
@keyframes ozelFadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes ozelSlideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

/* Pseudo-element'ler — yine kapsam gerektirir */
#ozel-tasarim-alani-XXXX .ozel-divider::after { content: ''; ... }

/* Agresif temalara karşı özgüllük artırma */
#ozel-tasarim-alani-XXXX h2.ozel-section-title { ... }
/* Tema hâlâ eziyorsa: */
div#ozel-tasarim-alani-XXXX h2.ozel-section-title { ... }
```

**Google Fonts:**
```css
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;600&display=swap');

  /* Font SADECE kendi kapsamımız içinde uygulanır */
  #ozel-tasarim-alani-XXXX {
    font-family: 'Open Sans', sans-serif;
  }
  #ozel-tasarim-alani-XXXX h1,
  #ozel-tasarim-alani-XXXX h2,
  #ozel-tasarim-alani-XXXX h3 {
    font-family: 'Montserrat', sans-serif;
  }
</style>
```

### Kural 3: İkon Sistemi — Google Material Symbols

İkonlar için **Google Material Symbols** kullan. Inline SVG veya font icon kütüphanesi
yerine bu yöntem tercih edilir:

```css
/* <style> etiketinin en başında, @import ile yükle */
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

/* İkon stilini kapsamlı tanımla */
#ozel-tasarim-alani-XXXX .material-symbols-outlined {
  font-family: 'Material Symbols Outlined';
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-feature-settings: 'liga';
  /* İkon özelleştirme değişkenleri */
  font-variation-settings:
    'FILL' 0,
    'wght' 400,
    'GRAD' 0,
    'opsz' 24;
  vertical-align: middle;
  color: inherit;
}

/* Dolu (filled) ikon varyantı */
#ozel-tasarim-alani-XXXX .material-symbols-outlined.ozel-icon-filled {
  font-variation-settings:
    'FILL' 1,
    'wght' 400,
    'GRAD' 0,
    'opsz' 24;
}

/* Farklı boyutlar */
#ozel-tasarim-alani-XXXX .ozel-icon-sm { font-size: 18px; }
#ozel-tasarim-alani-XXXX .ozel-icon-md { font-size: 24px; }
#ozel-tasarim-alani-XXXX .ozel-icon-lg { font-size: 36px; }
#ozel-tasarim-alani-XXXX .ozel-icon-xl { font-size: 48px; }
```

**HTML'de kullanım:**
```html
<!-- Temel kullanım -->
<span class="material-symbols-outlined">check_circle</span>

<!-- Dolu varyant -->
<span class="material-symbols-outlined ozel-icon-filled">favorite</span>

<!-- Büyük boyut -->
<span class="material-symbols-outlined ozel-icon-lg">rocket_launch</span>

<!-- Buton içinde -->
<button class="ozel-btn">
  <span class="material-symbols-outlined">arrow_forward</span>
  Devam Et
</button>
```

**İkon seçimi kuralları:**
- Referans tasarımda kullanılan ikonlara EN YAKIN Material Symbols karşılığını bul
- İkon adlarını https://fonts.google.com/icons adresinden doğrula
- Referansta ikon yoksa ekstra ikon EKLEME (Tasarım Felsefesi kuralı)
- Tutarlılık: Tüm sayfada aynı ikon stilini kullan (outlined VEYA filled, karıştırma)

### Kural 4: JS İzolasyonu — IIFE Sarmalama (Zorunlu)

TÜM JavaScript IIFE içine sarılmalıdır:

```html
<script>
(function() {
  'use strict';

  // ── Yapılandırma ──
  var ROOT_ID = 'ozel-tasarim-alani-XXXX';
  var root = document.getElementById(ROOT_ID);
  if (!root) return;  // Güvenlik: konteyner bulunamazsa çık

  // ── DOM Sorguları — HER ZAMAN root'a kapsamla ──
  // DOĞRU:
  var butonlar = root.querySelectorAll('.ozel-btn');
  var heroAlani = root.querySelector('.ozel-hero');

  // YANLIŞ — ASLA yapma:
  // var butonlar = document.querySelectorAll('.ozel-btn');  // Sayfadaki TÜM .ozel-btn'leri seçer!
  // var el = document.getElementById('benim-id');           // Kapsamımızdan kaçar!

  // ── Olay Dinleyiciler ──
  butonlar.forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      // tıklama işlemi
    });
  });

})();
</script>
```

**JS Kesin Kuralları:**
- **Global kapsamda `var`, `let`, `const` YASAK** — her şey IIFE içinde
- **İç öğeler için `document.querySelector` YASAK** — `root.querySelector` kullan
- **`window.onload = ...` YASAK** — gerekirse `addEventListener` kullan
- **Global `window.$` veya jQuery YASAK** — gerekiyorsa IIFE içinde `jQuery.noConflict()` kullan
- **Global referanslı `setTimeout`/`setInterval` YASAK** — referansları IIFE içinde yakala
- **HTML'de inline olay yöneticileri YASAK** (örn: `onclick="..."`). JS'den bağla.

### Kural 5: Üst Bilgi / Alt Bilgi Yok

Çıktıda şunlar OLMAMALIDIR:
- ❌ Navigasyon çubukları / başlık menüleri
- ❌ Üst barlar (duyuru çubukları, dil seçiciler)
- ❌ Alt bilgi bölümleri (site haritası, telif hakkı, iletişim satırları)
- ❌ "Başa dön" yüzen butonları
- ❌ Sabit/yapışkan konum öğeleri (`position: fixed` konteynerin dışına kaçar!)
- ❌ Çerez onay banner'ları
- ❌ Sohbet widget'ları veya yüzen butonlar

Sadece **içerik bölümleri** üretilir.

### Kural 6: Konteyner Tanımlaması

```css
#ozel-tasarim-alani-XXXX {
  width: 100%;
  margin: 0 auto;
  padding: 0;
  background-color: #ffffff;           /* ZORUNLU — daima beyaz */
  box-sizing: border-box;
  overflow: hidden;                    /* Yatay taşma kaçağını önle */
  position: relative;                  /* Mutlak konumlu çocukları kapsasın */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

**Genişlik stratejisi:**
- Sabit `max-width` KULLANMA — referans tasarımın genişlik davranışını aynen taklit et
- Referansta belirli bir `max-width` varsa (örn: 1200px, 1440px) → onu kullan
- Referansta tam genişlik (full-width) bölümler varsa → `width: 100%` ile yap
- İçerik konteynerini referanstaki gibi ayarla (genellikle bölüm içinde bir `.ozel-container`)
- Amaç: WordPress'in kendi konteyner genişliğine doğal şekilde uyum sağlamak

```css
/* İç konteyner — referanstaki genişliği kullan */
#ozel-tasarim-alani-XXXX .ozel-container {
  max-width: ____px;    /* Referanstan oku, yoksa kaldır */
  width: 100%;
  margin: 0 auto;
  padding: 0 ____px;    /* Referanstan oku */
}
```

### Kural 7: Görsel İşleme Stratejisi

WordPress'e yapıştırılacağı için görseller özel işlem gerektirir:

| Senaryo | Strateji |
|---------|----------|
| Küçük ikonlar/logolar < 30KB | Base64 inline: `src="data:image/svg+xml;base64,..."` |
| Dekoratif desenler | CSS gradient'leri, inline SVG veya CSS desenleri |
| Hero/banner görselleri | Placeholder + talimat yorumu |
| İçerik görselleri | Placeholder + talimat yorumu |

**Lazy loading ZORUNLUDUR — tüm görsellere ekle:**
```html
<img
  src="https://placehold.co/800x400/HEXRENK/YAZRENK?text=Gorsel+Aciklamasi"
  alt="Açıklayıcı alt metin"
  class="ozel-hero-img"
  loading="lazy"
  decoding="async"
>
<!-- WP-MEDYA-TALIMATI: Bu görseli WordPress Medya Kütüphanesi'ne yükleyip
     src değerini güncelleyin. Önerilen boyut: 800x400px -->
```

**`loading="lazy"` kuralları:**
- Sayfadaki TÜM `<img>` etiketlerine `loading="lazy"` ve `decoding="async"` ekle
- İlk ekranda (above the fold) görünen tek bir hero görseli varsa → o görselde `loading="eager"` kullan
- `<iframe>` öğelerine de `loading="lazy"` ekle

### Kural 8: Responsive Tasarım (Kapsamlı)

Üç zorunlu kırılma noktası, tümü kapsamlı:

```css
/* ── Tablet ── */
@media (max-width: 1024px) {
  #ozel-tasarim-alani-XXXX .ozel-grid-3 {
    grid-template-columns: 1fr 1fr;
  }
  #ozel-tasarim-alani-XXXX .ozel-section {
    padding: 60px 24px;
  }
}

/* ── Mobil ── */
@media (max-width: 768px) {
  #ozel-tasarim-alani-XXXX .ozel-grid-3,
  #ozel-tasarim-alani-XXXX .ozel-grid-2 {
    grid-template-columns: 1fr;
  }
  #ozel-tasarim-alani-XXXX .ozel-section {
    padding: 40px 16px;
  }
  #ozel-tasarim-alani-XXXX h1 { font-size: 28px; }
  #ozel-tasarim-alani-XXXX h2 { font-size: 24px; }
}

/* ── Küçük Mobil ── */
@media (max-width: 480px) {
  #ozel-tasarim-alani-XXXX .ozel-section {
    padding: 32px 12px;
  }
  #ozel-tasarim-alani-XXXX h1 { font-size: 24px; }
  #ozel-tasarim-alani-XXXX h2 { font-size: 20px; }
}
```

### Kural 9: Animasyon Politikası — Statik Öncelikli

```
VARSAYILAN DAVRANIŞ: Sayfa statik olarak yüklenir.
Scroll tetiklemeli animasyonlar (fade-in, slide-up vb.) EKLENMEZ.
```

İzin verilen etkileşimler:
- ✅ Hover geçişleri (butonlar, kartlar, linkler) — `transition` ile
- ✅ Focus durumları (form öğeleri, linkler) — erişilebilirlik için
- ✅ Aktif tab/akordeon panellerinin açılıp kapanması
- ✅ Slider/carousel geçişleri (referansta varsa)

Yasaklananlar:
- ❌ Scroll tetiklemeli fade-in / slide-up / zoom-in
- ❌ IntersectionObserver ile görünürlük animasyonları
- ❌ Sayfa yüklenirken staggered reveal (sıralı belirme)
- ❌ Paralax efektleri
- ❌ Sayaç animasyonları (sayılar sabit gösterilir)

**İSTİSNA:** Kullanıcı açıkça "animasyon ekle" veya "scroll efekti olsun" derse → ekle.
Aksi halde sayfa tamamen statik yüklenir.

---

## Tasarım Sadakati Rehberi

Üretilen kod, referans tasarımla **görsel olarak ayırt edilemez** olmalıdır:

### Renk ve Palet
- Referans CSS'ten BİREBİR hex değerlerini çıkar
- Her kullanımı eşle: arka planlar, metinler, kenarlıklar, butonlar, hover durumları, gölgeler
- Yaklaşık değer KULLANMA — tam değerleri kullan
- **Arka plan rengi her zaman #ffffff** — referansta farklı olsa bile sarmalayıcı beyaz kalır

### Tipografi
- HER metin seviyesi için font ailesi, ağırlık, boyut, satır yüksekliği, harf aralığını eşle
- Referans Google Fonts'ta olmayan bir font kullanıyorsa → yorumda belirt
- Text transform (uppercase, capitalize) kullanıldığı yerlerde koru
- **Font seçimi referansa bağlıdır** — kendi tercihini EKLEME

### Boşluk ve Ritim
- Bölüm padding'ini tam olarak eşle
- Öğe margin ve boşluklarını eşle
- Başlıklar, paragraflar ve bileşenler arası dikey ritmi koru
- Kart/bileşen iç padding'ini eşle

### Bileşen Desenleri
- Kart tasarımlarını birebir kopyala (gölgeler, kenarlıklar, radius, hover durumları)
- Buton stillerini kopyala (padding, radius, arka plan, hover geçişi)
- Liste/grid düzenlerini kopyala (sütunlar, boşluklar, hizalama)
- Ayırıcıları, vurgu çizgilerini, dekoratif öğeleri kopyala

### Görsel Efektler
- Box-shadow değerlerini birebir eşle
- Transition/geçiş zamanlama ve yumuşatmasını eşle (ease-out, cubic-bezier tercih)
- Gradient tanımlarını eşle
- Overlay/opaklık efektlerini eşle
- Hover durumlarını ve etkileşimli geri bildirimleri eşle

---

## İçerik Yerleştirme Protokolü

Kullanıcı içeriği numaralı bölümler halinde sunar. Her bölüm için:

1. **Referans tasarımın düzeninden uygun görsel bölüme eşle**
2. **Referansın başlık hiyerarşisini uygula** (bölüm başlıkları için h2, alt bölümler için h3)
3. **Referansın bileşen desenlerini kullan** (kartlar, grid'ler, listeler, özellik blokları)
4. **Referansın dekoratif öğelerini koru** (vurgu çizgileri, ikonlar, ayırıcılar)

### Bölüm Eşleme Stratejisi

```
Kullanıcı İçeriği       →  Görsel İşlem
─────────────────────────────────────────────
1. Bölüm (Ana/Hero)     →  Tam genişlikte öne çıkan bölüm, büyük başlık
2. Bölüm (Özellikler)   →  Kart grid'i veya özellik listesi düzeni
3. Bölüm (Detaylar)     →  İki sütun veya dönüşümlü görsel-metin düzeni
4. Bölüm (CTA/Kapanış)  →  Vurgu kutusu veya harekete geçirici bölüm
```

Eşlemeyi referans tasarımın gerçek bölüm desenlerine göre uyarla. Referansta
referanslar, istatistikler veya galeri için özel stil varsa → içerik uyuyorsa o desenleri kullan.

---

## Çıktı Yapısı Şablonu

```html
<!-- WordPress Gömülebilir Bileşen — Tamamen İzole -->
<div id="ozel-tasarim-alani-XXXX">

<style>
  /* ══════════════════════════════════════════
     Google Fonts ve Material Symbols Yükleme
     ══════════════════════════════════════════ */
  @import url('https://fonts.googleapis.com/css2?family=...&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

  /* ══════════════════════════════════════════
     CSS Özel Değişkenler (kapsamlı)
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX {
    --ozel-primary: #______;
    --ozel-secondary: #______;
    --ozel-accent: #______;
    --ozel-text: #______;
    --ozel-text-light: #______;
    --ozel-bg: #ffffff;
    --ozel-surface: #______;
    --ozel-border: #______;
    --ozel-radius: __px;
    --ozel-shadow: 0 __px __px rgba(0,0,0,0.__);
    --ozel-transition: all 0.3s ease-out;
  }

  /* ══════════════════════════════════════════
     Temel Sıfırlama (kapsamlı)
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX {
    width: 100%;
    margin: 0 auto;
    padding: 0;
    background-color: #ffffff;
    box-sizing: border-box;
    font-family: '...', sans-serif;
    color: var(--ozel-text);
    line-height: 1.6;
    overflow: hidden;
    position: relative;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  #ozel-tasarim-alani-XXXX *,
  #ozel-tasarim-alani-XXXX *::before,
  #ozel-tasarim-alani-XXXX *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  #ozel-tasarim-alani-XXXX img {
    max-width: 100%;
    height: auto;
    display: block;
  }

  #ozel-tasarim-alani-XXXX a {
    text-decoration: none;
    color: inherit;
  }

  /* ══════════════════════════════════════════
     Material Symbols İkon Stilleri
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX .material-symbols-outlined {
    font-family: 'Material Symbols Outlined';
    font-weight: normal;
    font-style: normal;
    font-size: 24px;
    line-height: 1;
    letter-spacing: normal;
    text-transform: none;
    display: inline-block;
    white-space: nowrap;
    word-wrap: normal;
    direction: ltr;
    -webkit-font-smoothing: antialiased;
    font-feature-settings: 'liga';
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    vertical-align: middle;
    color: inherit;
  }
  #ozel-tasarim-alani-XXXX .ozel-icon-filled {
    font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  }
  #ozel-tasarim-alani-XXXX .ozel-icon-sm { font-size: 18px; }
  #ozel-tasarim-alani-XXXX .ozel-icon-lg { font-size: 36px; }
  #ozel-tasarim-alani-XXXX .ozel-icon-xl { font-size: 48px; }

  /* ══════════════════════════════════════════
     İç Konteyner
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX .ozel-container {
    width: 100%;
    margin: 0 auto;
    padding: 0 ____px;   /* Referanstan oku */
  }

  /* ══════════════════════════════════════════
     Tipografi (kapsamlı)
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX h1 { ... }
  #ozel-tasarim-alani-XXXX h2 { ... }
  #ozel-tasarim-alani-XXXX h3 { ... }
  #ozel-tasarim-alani-XXXX h4 { ... }
  #ozel-tasarim-alani-XXXX p  { ... }

  /* ══════════════════════════════════════════
     Bölüm Stilleri
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX .ozel-section { ... }
  #ozel-tasarim-alani-XXXX .ozel-section-1 { ... }
  #ozel-tasarim-alani-XXXX .ozel-section-2 { ... }
  #ozel-tasarim-alani-XXXX .ozel-section-3 { ... }

  /* ══════════════════════════════════════════
     Bileşen Stilleri
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX .ozel-card { ... }
  #ozel-tasarim-alani-XXXX .ozel-btn { ... }
  #ozel-tasarim-alani-XXXX .ozel-grid { ... }

  /* ══════════════════════════════════════════
     Hover Geçişleri (statik sayfa — sadece hover)
     ══════════════════════════════════════════ */
  #ozel-tasarim-alani-XXXX .ozel-card {
    transition: var(--ozel-transition);
  }
  #ozel-tasarim-alani-XXXX .ozel-card:hover {
    transform: translateY(-4px);
    box-shadow: ...;
  }
  #ozel-tasarim-alani-XXXX .ozel-btn {
    transition: var(--ozel-transition);
  }
  #ozel-tasarim-alani-XXXX .ozel-btn:hover { ... }

  /* ══════════════════════════════════════════
     Responsive — Tablet
     ══════════════════════════════════════════ */
  @media (max-width: 1024px) {
    #ozel-tasarim-alani-XXXX ... { ... }
  }

  /* ══════════════════════════════════════════
     Responsive — Mobil
     ══════════════════════════════════════════ */
  @media (max-width: 768px) {
    #ozel-tasarim-alani-XXXX ... { ... }
  }

  /* ══════════════════════════════════════════
     Responsive — Küçük Mobil
     ══════════════════════════════════════════ */
  @media (max-width: 480px) {
    #ozel-tasarim-alani-XXXX ... { ... }
  }
</style>

  <!-- ════════ Bölüm 1: [Bölüm Adı] ════════ -->
  <section class="ozel-section ozel-section-1">
    <div class="ozel-container">
      ...
    </div>
  </section>

  <!-- ════════ Bölüm 2: [Bölüm Adı] ════════ -->
  <section class="ozel-section ozel-section-2">
    <div class="ozel-container">
      ...
    </div>
  </section>

  <!-- ════════ Bölüm 3: [Bölüm Adı] ════════ -->
  <section class="ozel-section ozel-section-3">
    <div class="ozel-container">
      ...
    </div>
  </section>

<script>
(function() {
  'use strict';

  var ROOT_ID = 'ozel-tasarim-alani-XXXX';
  var root = document.getElementById(ROOT_ID);
  if (!root) return;

  // ── Ek Etkileşimler (gerekiyorsa) ──
  // Tab'lar, akordeonlar, slider'lar vb.
  // Tümü root'a kapsamlı...

})();
</script>

</div>
<!-- /WordPress Gömülebilir Bileşen -->
```

---

## İleri Teknikler

### CSS Sınıf Adlandırma Kuralı

WordPress tema sınıflarıyla çakışmayı önlemek için TÜM özel sınıflara `ozel-` öneki ekle:

```
✅ ozel-hero, ozel-card, ozel-grid, ozel-btn, ozel-section
❌ hero, card, grid, btn, section (yaygın adlar — ÇAKIŞIR)
```

### Karmaşık Etkileşimlerin İşlenmesi

**Tab'lar:**
```javascript
var tabButonlari = root.querySelectorAll('.ozel-tab-btn');
var tabPanelleri = root.querySelectorAll('.ozel-tab-panel');

tabButonlari.forEach(function(btn, i) {
  btn.addEventListener('click', function() {
    tabButonlari.forEach(function(b) { b.classList.remove('ozel-active'); });
    tabPanelleri.forEach(function(p) { p.classList.remove('ozel-active'); });
    btn.classList.add('ozel-active');
    tabPanelleri[i].classList.add('ozel-active');
  });
});
```

**Akordeon:**
```javascript
root.querySelectorAll('.ozel-accordion-header').forEach(function(baslik) {
  baslik.addEventListener('click', function() {
    var oge = this.parentElement;
    var acikMi = oge.classList.contains('ozel-open');

    // Diğerlerini kapat (opsiyonel)
    root.querySelectorAll('.ozel-accordion-item').forEach(function(el) {
      el.classList.remove('ozel-open');
    });

    if (!acikMi) oge.classList.add('ozel-open');
  });
});
```

### WordPress Tema Müdahalesinin Yönetimi

WordPress temasının agresif global stillerle ezmesi durumunda:

```css
/* Konteyner için nükleer sıfırlama */
#ozel-tasarim-alani-XXXX,
#ozel-tasarim-alani-XXXX * {
  all: unset;
  display: revert;
  box-sizing: border-box;
}

/* Ardından stilleri yüksek özgüllükle yeniden uygula */
div#ozel-tasarim-alani-XXXX { ... }
div#ozel-tasarim-alani-XXXX p { ... }
```

⚠️ Nükleer sıfırlamayı SADECE açıkça istendiğinde veya kullanıcı tema çakışması bildirdiğinde kullan.

### Harici Kütüphaneler (Dikkatli Kullan)

Referans tasarım bir kütüphane kullanıyorsa (Swiper, AOS vb.):

```html
<script>
(function() {
  'use strict';
  var ROOT_ID = 'ozel-tasarim-alani-XXXX';
  var root = document.getElementById(ROOT_ID);
  if (!root) return;

  // Kütüphane zaten yüklü mü kontrol et (WordPress'te olabilir)
  if (typeof Swiper === 'undefined') {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js';
    script.onload = sliderBaslat;
    document.head.appendChild(script);

    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css';
    document.head.appendChild(link);
  } else {
    sliderBaslat();
  }

  function sliderBaslat() {
    new Swiper(root.querySelector('.ozel-swiper'), {
      slidesPerView: 1,
      spaceBetween: 30,
      pagination: { el: root.querySelector('.ozel-swiper-pagination') },
      navigation: {
        nextEl: root.querySelector('.ozel-swiper-next'),
        prevEl: root.querySelector('.ozel-swiper-prev')
      }
    });
  }
})();
</script>
```

---

## Kalite Kontrol Listesi (Çıktıdan Önce HER Maddeyi Doğrula)

### İzolasyon Kontrolleri (KRİTİK — herhangi bir başarısızlık = bozuk WordPress)

- [ ] `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, `<meta>`, `<title>` etiketleri YOK
- [ ] Çıktı `<div id="ozel-tasarim-alani-XXXX">` ile başlıyor
- [ ] Sarmalayıcı ID'de benzersiz sayısal sonek var
- [ ] HER CSS kuralı `#ozel-tasarim-alani-XXXX` ile önekli
- [ ] Çıplak öğe seçicileri YOK (`h1 {}`, `p {}`, `a {}`, `img {}`, `div {}`)
- [ ] `:root` CSS değişken tanımı YOK (sarmalayıcı ID kullanılıyor)
- [ ] Tüm `@keyframes` adları `ozel` önekli
- [ ] Tüm CSS özel değişkenleri `--ozel-` önekli
- [ ] Tüm CSS sınıf adları `ozel-` önekli
- [ ] JS `(function() { ... })();` IIFE içinde sarılı
- [ ] JS iç öğeler için `root.querySelector` kullanıyor, `document.querySelector` DEĞİL
- [ ] Global JS değişken veya fonksiyon YOK
- [ ] Inline olay yöneticileri YOK (onclick, onmouseover vb.)
- [ ] `position: fixed` hiçbir yerde YOK
- [ ] Header/nav/footer öğeleri YOK

### Konteyner Kontrolleri

- [ ] `width: 100%`
- [ ] `margin: 0 auto`
- [ ] `background-color: #ffffff` (ZORUNLU beyaz)
- [ ] `box-sizing: border-box`
- [ ] `overflow: hidden` (veya minimum `overflow-x: hidden`)
- [ ] Sabit `max-width: 1280px` KULLANILMAMIŞ (referansa göre belirleniyor)

### Tasarım Kalitesi Kontrolleri (Yapay Zeka DEĞİL Uzman İşi)

- [ ] Renk paleti referansla birebir eşleşiyor
- [ ] Fontlar referansla eşleşiyor (gerekirse Google Fonts import var)
- [ ] Font boyutları, ağırlıkları, satır yükseklikleri seviye bazında eşleşiyor
- [ ] Boşluk/padding referans ritmiyle eşleşiyor
- [ ] Kart/bileşen stilleri kopyalanmış (gölgeler, kenarlıklar, radius)
- [ ] Buton stilleri kopyalanmış (padding, renkler, hover durumları)
- [ ] Hover/geçiş efektleri mevcut (ease-out veya cubic-bezier kullanılıyor)
- [ ] Görsel hiyerarşi korunmuş
- [ ] Referansta OLMAYAN süsleme EKLENMEMİŞ
- [ ] Jenerik AI estetiği YOK (mor gradient, Inter font, simetrik robotik düzen)
- [ ] Google Material Symbols ikonları doğru kullanılmış

### Lazy Loading Kontrolleri

- [ ] TÜM `<img>` etiketlerinde `loading="lazy"` var
- [ ] TÜM `<img>` etiketlerinde `decoding="async"` var
- [ ] İlk ekran hero görseli varsa `loading="eager"` kullanılmış
- [ ] `<iframe>` öğelerinde de `loading="lazy"` var

### Responsive Kontrolleri

- [ ] 1024px, 768px ve 480px kırılma noktaları var (minimum)
- [ ] Tüm kırılma kuralları sarmalayıcı ID ile kapsamlı
- [ ] Grid/flex düzenleri mobilde düzgün daraltılıyor
- [ ] Font boyutları mobilde uygun şekilde küçülüyor
- [ ] Görseller responsive (`max-width: 100%; height: auto;`)
- [ ] Mobilde yatay kaydırma YOK

### Animasyon Politikası Kontrolleri

- [ ] Scroll tetiklemeli animasyon YOK (fade-in, slide-up vb.)
- [ ] IntersectionObserver animasyonu YOK
- [ ] Paralax efekti YOK
- [ ] Sayaç animasyonu YOK (sayılar sabit gösteriliyor)
- [ ] SADECE hover geçişleri ve etkileşim geri bildirimleri var

### İçerik ve Dil Kontrolleri

- [ ] Tüm kullanıcı bölüm içerikleri doğru sırada yerleştirilmiş
- [ ] Bölüm içerikleri uygun görsel konteynerlere sarılmış
- [ ] Header/footer içeriği dahil EDİLMEMİŞ
- [ ] Görsellerde placeholder + yükleme talimatı yorumları var
- [ ] Tüm görsellerde alt metin var
- [ ] HTML yorumları Türkçe
- [ ] Placeholder metinleri Türkçe
- [ ] Talimat yorumları Türkçe

---

## Sık Yapılan Hatalar ve Düzeltmeleri

| # | Hata | Düzeltme |
|---|------|----------|
| 1 | `:root { --color: ... }` | `#ozel-tasarim-alani-XXXX { --ozel-color: ... }` kullan |
| 2 | `position: fixed` herhangi bir öğede | `position: sticky` veya `relative` parent içinde `absolute` kullan |
| 3 | Çıplak `.card { }` seçici | Her zaman `#ozel-tasarim-alani-XXXX .ozel-card { }` |
| 4 | `document.getElementById('hero')` | `root.querySelector('.ozel-hero')` |
| 5 | Global `$` veya `jQuery` kullanımı | IIFE içinde sar, varlık kontrol et: `if (typeof jQuery !== 'undefined')` |
| 6 | `@keyframes fadeIn` | `@keyframes ozelFadeIn` |
| 7 | `<script src="harici.js">` | IIFE içinde dinamik yükle ve varlık kontrol et |
| 8 | `onclick="birSeyYap()"` | IIFE içinde `addEventListener` ile bağla |
| 9 | Responsive kapsamlamayı unutmak | Her `@media` kuralı `#ozel-tasarim-alani-XXXX` öneki içermeli |
| 10 | Yaygın sınıf adları (`.container`, `.row`, `.btn`) | Önekle: `.ozel-container`, `.ozel-row`, `.ozel-btn` |
| 11 | `<link rel="stylesheet" href="...">` | `<style>` içinde `@import url(...)` kullan |
| 12 | Bölümlerde ID'ler (`id="hero"`) | Önekle: `id="ozel-hero"` veya tercihen sınıf kullan |
| 13 | `z-index: 9999` | z-index değerlerini konteyner içinde makul tut (1-100) |
| 14 | `100vh` yükseklikler | `min-height` değerlerini px/rem ile kullan — `100vh` WP'de sorun çıkarabilir |
| 15 | `max-width: 1280px` sabit değer | Referanstaki genişliği kullan veya `width: 100%` ile WP konteynerine uyum sağla |
| 16 | Scroll animasyonları eklemek | Statik tut — kullanıcı açıkça istemedikçe animasyon EKLEME |
| 17 | `loading="lazy"` eksik görseller | TÜM görsellere `loading="lazy" decoding="async"` ekle |
| 18 | İngilizce yorum ve placeholder'lar | Tüm yorumlar, placeholder'lar ve talimatlar Türkçe olmalı |

---

## Son Çıktı Protokolü

1. Eksiksiz kodu `/mnt/user-data/outputs/wordpress-embed.html` dosyasına yaz
2. `present_files` ile kullanıcıyla paylaş
3. Açıklayıcı metin EKLEME — kullanıcı kopyala-yapıştır'a hazır kod istiyor
4. Tasarım karmaşıksa (>500 satır) → `/home/claude/wp-work/` içinde iteratif oluştur, son halini outputs'a kopyala
5. Dosya adı kullanıcı belirtirse özelleştirilebilir, yoksa varsayılan `wordpress-embed.html`

**UNUTMA:** Kullanıcı bu kodu WordPress HTML bloğuna birebir yapıştıracak.
Görsel URL'leri dışında SIFIR değişiklikle ilk yapıştırmada mükemmel çalışMALIDIR.

**DİL KURALI:** HTML yorumları, placeholder metinleri, görsel alt metinleri, talimat
yorumları ve tüm kullanıcıya görünür metin — hepsi Türkçe olacak.
