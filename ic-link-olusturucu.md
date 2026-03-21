---
name: wp-internal-linking
description: "WordPress web sitelerinde SEO odaklı iç bağlantı (internal linking) stratejisi kurgulamak, uygulamak ve denetlemek için kapsamlı bir beceri. Bu beceriyi şu durumlarda kullan: kullanıcı 'iç link', 'iç bağlantı', 'internal link', 'internal linking', 'site içi bağlantı', 'pillar cluster', 'konu kümeleme', 'topic cluster', 'link equity', 'yetim sayfa', 'orphan page', 'anchor text stratejisi', 'bağlantı mimarisi', 'link yapısı', 'SEO bağlantı', 'silo yapısı', 'hub spoke' ifadelerinden herhangi birini kullandığında tetikle. WordPress sitesinde içerikler arası bağlantı kurulması, mevcut bağlantı yapısının analizi, kırık linklerin tespiti, konu kümelerinin oluşturulması, anchor text optimizasyonu veya iç bağlantı denetimi gibi konularda da tetikle. Kullanıcı sadece 'SEO çalışması yap' veya 'sitemdeki bağlantıları düzenle' dese bile bu beceriyi kullan."
---

# WordPress İç Bağlantı (Internal Linking) SEO Becerisi

## Genel Bakış

Bu beceri, WordPress web sitelerinde SEO amaçlı iç bağlantı stratejisinin planlanması, uygulanması ve sürdürülmesi için uçtan uca bir çerçeve sunar. Kullanıcının site bilgilerini alır, mevcut yapıyı analiz eder, konu kümeleri oluşturur, somut bağlantı talimatları üretir ve WordPress'e özgü teknik uygulama rehberi sağlar.

## İş Akışı

Aşağıdaki adımları **sırasıyla** takip et. Her adımda kullanıcıdan gerekli bilgileri topla, eksik bilgiyi varsayımla değil soruyla tamamla.

---

### ADIM 1: Site Bilgilerini Topla

Kullanıcıdan şu bilgileri iste (yoksa varsayılan değerleri belirt):

```
Gerekli Bilgiler:
- Site URL'si
- Sektör / Niş alanı
- Yaklaşık toplam sayfa/yazı sayısı
- Mevcut kategori yapısı
- Kullanılan SEO eklentisi (Yoast / Rank Math / diğer)
- İçerik envanteri dosyası (varsa — CSV, XLSX veya Screaming Frog/Ahrefs/Semrush çıktısı)
```

**Opsiyonel ama faydalı:**
- Google Search Console erişimi veya dışa aktarılmış iç bağlantı raporu
- En çok trafik alan 10 sayfa
- Sıralama hedeflenen anahtar kelimeler listesi
- Dönüşüm sayfaları (iletişim, satış, form vb.)

---

### ADIM 2: İçerik Envanteri Analizi

Kullanıcı bir içerik listesi sağladıysa, aşağıdaki tabloyu oluştur:

| # | URL | Başlık | Hedef AK | Kategori | Gelen İç Link | Giden İç Link | Durum |
|---|-----|--------|----------|----------|----------------|----------------|-------|

**Analiz çıktıları:**

1. **Yetim Sayfalar (Orphan Pages):**
   - 0 gelen iç bağlantıya sahip sayfaları listele
   - Her biri için en az 2 potansiyel kaynak sayfa öner

2. **Aşırı Bağlantılı Sayfalar:**
   - Orantısız fazla bağlantı alan sayfaları belirle (ortalamadan 3x fazla)
   - Gereksiz bağlantıların kaldırılmasını öner

3. **Derinlik Sorunları:**
   - Ana sayfadan 3+ tık uzaklıktaki sayfaları tespit et
   - Yapıyı sığlaştıracak bağlantı önerileri sun

4. **Kırık Bağlantılar:**
   - 404 hatalı hedef URL'leri listele
   - 301 yönlendirme veya bağlantı güncelleme öner

**NOT:** Kullanıcı envanter sağlamadıysa, Screaming Frog veya benzeri araçla nasıl çıkarılacağını kısaca açıkla ve manuel bilgi toplamaya geç.

---

### ADIM 3: Konu Kümeleme (Topic Clustering)

İçerikleri tematik kümelere ayır. Her küme için aşağıdaki yapıyı oluştur:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KÜME: [KONU ADI]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 Pillar Sayfa: [URL] — [Başlık]
   Hedef AK: [anahtar kelime]
   Durum: Mevcut / Oluşturulacak

   ├── Cluster 1: [URL] — [Başlık]
   │   Hedef AK: [anahtar kelime]
   │
   ├── Cluster 2: [URL] — [Başlık]
   │   Hedef AK: [anahtar kelime]
   │
   ├── Cluster 3: [URL] — [Başlık]
   │   Hedef AK: [anahtar kelime]
   │
   ├── [EKSİK] Önerilen: [Başlık Önerisi]
   │   Hedef AK: [anahtar kelime]
   │
   └── [EKSİK] Önerilen: [Başlık Önerisi]
       Hedef AK: [anahtar kelime]

Küme İçi Bağlantı Yönü:
  Pillar ←→ Tüm Cluster'lar (çift yönlü)
  Cluster 1 → Cluster 2 (bağlamsal ilişki varsa)
  Cluster 2 → Cluster 3 (bağlamsal ilişki varsa)

Çapraz Küme Bağlantıları:
  Cluster 2 → [Diğer Küme] Cluster X (ilişki açıklaması)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Kümeleme kuralları:**
- Bir içerik birden fazla kümeye ait olabilir; ancak yalnızca bir kümenin cluster'ı olarak birincil atanır
- Pillar sayfa yoksa, mevcut en geniş kapsamlı içeriği pillar olarak öner veya yeni pillar içerik yaratılmasını tavsiye et
- Her küme en az 3, ideal olarak 5-8 cluster içeriğe sahip olmalıdır
- Eksik içerik boşluklarını belirle ve öner

---

### ADIM 4: İç Bağlantı Talimat Listesi

Her bağlantı için aşağıdaki formatta somut talimat oluştur:

```
┌─────────────────────────────────────────┐
│ BAĞLANTI #[NUMARA]          [ÖNCELİK]  │
├─────────────────────────────────────────┤
│ Kaynak:  [kaynak sayfa URL'si]          │
│ Hedef:   [hedef sayfa URL'si]           │
│ Tür:     [Contextual/Navigational]      │
│                                         │
│ Anchor Text (birincil):                 │
│   "[önerilen anchor text]"              │
│                                         │
│ Anchor Text (alternatif):               │
│   "[alternatif varyasyon 1]"            │
│   "[alternatif varyasyon 2]"            │
│                                         │
│ Yerleşim Talimatı:                      │
│   [Bağlantının ekleneceği bölüm/        │
│    paragraf açıklaması ve bağlamı]      │
│                                         │
│ Örnek Cümle:                            │
│   "[Bağlantının kullanıldığı örnek      │
│    cümle — anchor text bold]"           │
└─────────────────────────────────────────┘
```

**Anchor Text Kuralları (Zorunlu):**

| Kural | Açıklama |
|-------|----------|
| Çeşitlilik | Aynı hedefe farklı anchor text varyasyonları kullan |
| Doğallık | "Buraya tıklayın", "devamı" gibi genel ifadelerden kaçın |
| Uzunluk | 3-7 kelime arası |
| Exact Match Sınırı | Toplam bağlantıların en fazla %30'u exact match olsun |
| Bağlam Uyumu | Anchor text çevreleyen metinle uyumlu olmalı |
| Tekrar Yasağı | Aynı sayfada aynı hedefe 1'den fazla bağlantı verme |

**Anchor Text Dağılım Hedefi:**
- Kısmi eşleşme (partial match): %40-50
- Doğal ifadeler: %20-30
- Tam eşleşme (exact match): %15-25
- Markalı (branded): %5-10

---

### ADIM 5: Sayfa Türüne Göre Bağlantı Dağılımı

Her sayfa türü için optimum bağlantı sayısını hesapla:

| Sayfa Türü | Kelime Aralığı | Toplam İç Link | Contextual | Nav/Footer |
|------------|----------------|----------------|------------|------------|
| Blog (kısa) | 500-1.000 | 3-7 | 2-5 | 1-2 |
| Blog (orta) | 1.000-2.000 | 5-15 | 4-12 | 1-3 |
| Blog (uzun) | 2.000-3.000 | 10-20 | 8-16 | 2-4 |
| Pillar | 3.000-5.000+ | 15-30 | 12-25 | 3-5 |
| Kategori | Değişken | 10-25 | — | 10-25 |
| Ürün/Hizmet | 500-1.500 | 5-10 | 3-7 | 2-3 |
| Ana Sayfa | Değişken | 10-20 | 5-10 | 5-10 |

**Genel kural:** Her 200-300 kelimede 1 contextual iç bağlantı.

---

### ADIM 6: Otorite Yönlendirme (Link Equity Sculpting)

Bağlantıları stratejik olarak önceliklendir:

**Tier 1 — En Fazla İç Bağlantı Alacak Sayfalar:**
- Dönüşüm sayfaları (satış, iletişim, teklif formu)
- Para kazandıran sayfalar (ürün, hizmet)
- Sıralama yükseltilmek istenen hedef sayfalar
- Organik trafiği yüksek ancak sıralaması düşürülebilecek sayfalar

**Tier 2 — Orta Düzey İç Bağlantı:**
- Blog yazıları ve bilgi içerikleri
- Pillar sayfalar (zaten küme merkezinde oldukları için doğal olarak bağlantı alırlar)
- Hakkımızda, referanslar gibi güven sayfaları

**Tier 3 — Minimum İç Bağlantı veya Nofollow:**
- Giriş/kayıt sayfaları → nofollow öner
- Site içi arama sonuç sayfaları → nofollow öner
- Arşiv/etiket sayfaları (çok fazla varsa) → noindex + nofollow değerlendir
- Yasal sayfalar (KVKK, gizlilik, çerez) → doğal bağlantı yeterli

---

### ADIM 7: WordPress Teknik Uygulama

#### 7.1 Manuel Bağlantı Ekleme (Gutenberg Editörü)

Her bağlantı talimatı için:
1. WordPress Admin → İlgili Yazı/Sayfa → Düzenle
2. Bağlantı eklenecek metni seçin
3. Araç çubuğundan "Bağlantı" simgesine tıklayın (veya Ctrl+K)
4. Hedef sayfa URL'sini yapıştırın veya arayın
5. "Yeni sekmede aç" → Kapalı (iç bağlantılarda yeni sekme açmayın)
6. Kaydedin/Güncelleyin

#### 7.2 Toplu Ekleme İçin PHP Fonksiyonu

Kullanıcı çok sayıda bağlantı eklemek istiyorsa, aşağıdaki PHP yaklaşımını öner:

```php
/**
 * Otomatik iç bağlantı ekleme fonksiyonu
 * functions.php veya özel eklenti dosyasına eklenecek
 */
function wp_auto_internal_links($content) {
    if (!is_singular('post')) return $content;

    // Bağlantı haritası: anahtar kelime => hedef URL
    $link_map = array(
        'teknik SEO'        => '/teknik-seo-rehberi/',
        'anahtar kelime araştırması' => '/anahtar-kelime-arastirmasi/',
        'site hızı'         => '/site-hizi-optimizasyonu/',
        // Daha fazla ekle...
    );

    foreach ($link_map as $keyword => $url) {
        // Zaten bağlantı içinde olan kelimeleri atla
        $pattern = '/(?<!<a[^>]*>)(' . preg_quote($keyword, '/') . ')(?![^<]*<\/a>)/iu';
        $replacement = '<a href="' . esc_url($url) . '">$1</a>';
        // Sayfa başına aynı hedef için sadece 1 bağlantı
        $content = preg_replace($pattern, $replacement, $content, 1);
    }

    return $content;
}
add_filter('the_content', 'wp_auto_internal_links');
```

**UYARI:** Bu fonksiyonu dikkatli kullanın. Otomatik bağlantılar doğallığı bozabilir. Manuel ekleme her zaman tercih edilmelidir.

#### 7.3 Eklenti Ayarları

**Link Whisper (Ücretli — En Kapsamlı):**
- Ayarlar → Link Whisper → Auto-Linking → kapalı tut (manuel öneri modunda kullan)
- Yazı düzenlerken sağ panelde önerilen bağlantıları incele ve onayla
- Raporlar → Orphan sayfaları düzenli kontrol et

**Internal Link Juicer (Ücretsiz Alternatif):**
- Ayarlar → ILJ → her yazıya hedef anahtar kelimeler tanımla
- Otomatik bağlantı limitini sayfa başına 3-5 olarak ayarla
- Özel post type'ları dahil et/hariç tut

**Yoast SEO İç Bağlantı Önerileri:**
- Yazı editöründe sağ panelde Yoast → İç Bağlantı Önerileri bölümünü kontrol et
- Cornerstone content işaretlemesi yap (pillar sayfalara)

**Rank Math İç Bağlantı Önerileri:**
- Rank Math → Genel Ayarlar → Bağlantılar → İç bağlantı önerilerini aç
- Focus keyword tanımla (her yazıda)
- Pillar sayfaları "Pillar Content" olarak işaretle

#### 7.4 Breadcrumb Yapılandırması

```php
// Yoast SEO Breadcrumb (functions.php'ye ekle)
if (function_exists('yoast_breadcrumb')) {
    yoast_breadcrumb('<p id="breadcrumbs">', '</p>');
}

// Rank Math Breadcrumb
if (function_exists('rank_math_the_breadcrumbs')) {
    rank_math_the_breadcrumbs();
}
```

WordPress Admin → Yoast SEO → Arama Görünümü → Breadcrumbs → Etkinleştir
- Ayırıcı: `›` veya `>`
- Ana sayfa metni: "Ana Sayfa"
- Prefix'leri boş bırak

Schema markup otomatik olarak eklenir (Yoast/Rank Math).

#### 7.5 İlgili Yazılar Modülü

**Manuel Yaklaşım (Gutenberg):**
- Yazı sonuna "Grup" bloğu ekle
- Başlık: "İlgili Yazılar" veya "Bunları da Okuyun"
- Liste bloğu ile aynı kümedeki 3-5 yazıya bağlantı ver

**Eklenti Yaklaşımı (YARPP — Yet Another Related Posts Plugin):**
- Ayarlar → YARPP → Eşleşme: Kategori ağırlığı yüksek, etiket ağırlığı orta
- Gösterim: 3-4 ilgili yazı
- Şablon: Liste veya ızgara

---

### ADIM 8: Uygulama Takvimi

Kullanıcının site büyüklüğüne göre aşağıdaki takvimi özelleştir:

```
HAFTA 1: ANALİZ VE PLANLAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ İçerik envanteri çıkar (Screaming Frog veya manuel)
□ Yetim sayfaları tespit et
□ Kırık bağlantıları düzelt (301 yönlendirme)
□ Konu kümelerini oluştur
□ Pillar sayfaları belirle (mevcut veya oluşturulacak)

HAFTA 2-3: TEMEL BAĞLANTI KURGUSU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Pillar → Cluster bağlantıları ekle
□ Cluster → Pillar geri bağlantıları ekle
□ Cluster ↔ Cluster yatay bağlantıları ekle
□ Yetim sayfalara en az 2 gelen bağlantı sağla
□ Yeni eksik içerikleri yayınla ve bağla

HAFTA 4: TEKNİK OPTİMİZASYON
━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Breadcrumb yapılandır ve schema doğrula
□ İlgili yazılar modülünü kur
□ Nofollow ayarlarını yap (login, arama, sepet vb.)
□ Otorite yönlendirme: Tier 1 sayfalara ek bağlantı
□ Derinlik sorunlarını gider (3+ tık → 2-3 tık)

AYLIK SÜRDÜRME
━━━━━━━━━━━━━
□ Her yeni içerik için 3+ eski içerikten bağlantı ekle
□ Her yeni içerikte 2-3 mevcut içeriğe bağlantı ver
□ Kırık bağlantı taraması yap
□ Yetim sayfa kontrolü yap
□ GSC iç bağlantı raporunu incele
□ Sıralama ve trafik değişimlerini takip et
```

---

### ADIM 9: Denetim Kontrol Listesi

Aylık veya üç aylık periyotlarla çalıştırılacak kontrol listesi:

```
İÇ BAĞLANTI DENETİM KONTROL LİSTESİ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YAPISAL KONTROLLER
□ Tüm sayfalar en az 1 iç bağlantı alıyor mu?
□ Önemli sayfalar ≤3 tıkta ulaşılabilir mi?
□ Yönlendirme zincirleri (redirect chain) var mı?
□ Kırık iç bağlantı (404) var mı?
□ Nofollow gereksiz yere kullanılmış mı?

KÜMELEME KONTROLLERI
□ Her pillar sayfa tüm cluster içeriklere bağlı mı?
□ Her cluster içerik pillar sayfaya geri bağlı mı?
□ Yeni içerikler uygun kümeye atanmış mı?
□ Eksik cluster içerikler belirlenmiş mi?

ANCHOR TEXT KONTROLLERI
□ Anchor text'ler çeşitli ve tanımlayıcı mı?
□ Exact match oranı %30'un altında mı?
□ "Buraya tıklayın" gibi genel ifadeler kullanılmamış mı?
□ Aynı sayfada aynı hedefe çift bağlantı yok mu?

TEKNİK KONTROLLER
□ Breadcrumb yapısı doğru çalışıyor mu?
□ Schema markup (BreadcrumbList) geçerli mi?
□ İlgili yazılar modülü doğru içerik öneriyor mu?
□ Sitemap ile iç bağlantı yapısı tutarlı mı?
□ JavaScript ile oluşturulan bağlantılar HTML'de var mı?

PERFORMANS KONTROLLERI
□ Organik trafik trendi olumlu mu?
□ Oturum süresi artmış mı?
□ Sayfa/oturum oranı yükselmiş mi?
□ Bounce rate düşmüş mü?
□ Crawl istatistikleri sağlıklı mı?
```

---

## Çıktı Formatları

Bu beceriyi kullanan Claude, sonuçları şu formatlarda sunabilir:

1. **Markdown raporu** — Sohbet içinde detaylı analiz ve talimatlar
2. **XLSX dosyası** — İçerik envanteri, bağlantı haritası ve takip tablosu
3. **DOCX raporu** — Profesyonel iç bağlantı strateji dokümanı
4. **Kontrol listesi** — Basılabilir denetim formu

Kullanıcının tercihine göre uygun formatı seç. Varsayılan olarak Markdown + XLSX kombinasyonunu öner.

---

## Kritik Kurallar (Her Zaman Uygula)

1. **Kullanıcı öncelikli:** Her bağlantı kullanıcıya değer katmalıdır. SEO için değil, okuyucu için bağlantı öner.
2. **Doğallık:** Bağlantılar içeriğin doğal akışında olmalıdır. Zorla bağlantı ekleme.
3. **Tekil hedef:** Aynı sayfada aynı hedefe birden fazla bağlantı verme.
4. **İlk paragraf kuralı:** İlk 100-200 kelimede en az bir iç bağlantı olmalıdır.
5. **Çeşitlilik:** Aynı anchor text'i tekrarlama; varyasyon kullan.
6. **Geri bağlantı:** Her yeni içerik için en az 3 eski içerikten bağlantı ekle.
7. **İleri bağlantı:** Her yeni içerik en az 2-3 mevcut içeriğe bağlantı vermeli.
8. **301 kuralı:** Kırık bağlantıları silme; 301 yönlendirme ile düzelt.
9. **Yeni sekme yasağı:** İç bağlantılar aynı sekmede açılmalıdır (target="_blank" kullanma).
10. **Nofollow dikkatli:** İç bağlantılarda nofollow yalnızca login, arama, sepet gibi değersiz hedefler için kullan.

---

## Araç Önerileri

| Araç | Kullanım | Maliyet |
|------|----------|---------|
| Screaming Frog | Site taraması, yetim sayfa, kırık link tespiti | Ücretsiz (500 URL) / Ücretli |
| Ahrefs Site Audit | İç bağlantı analizi, otorite haritası | Ücretli |
| Semrush Site Audit | İç bağlantı sorunları, derinlik analizi | Ücretli |
| Google Search Console | İç bağlantı raporu, tarama istatistikleri | Ücretsiz |
| Sitebulb | Görsel site haritası, bağlantı ağacı | Ücretli |
| Link Whisper | WordPress iç bağlantı önerileri | Ücretli |
| Internal Link Juicer | WordPress otomatik iç bağlantı | Ücretsiz / Ücretli |

---

## Sık Yapılan Hatalar

Bu hataları tespit ettiğinde kullanıcıyı uyar:

1. **Tüm bağlantıları footer/sidebar'a yığmak** — Contextual bağlantılar çok daha değerlidir
2. **Aynı anchor text'i her yerde kullanmak** — Spam sinyali verir
3. **Yeni içerik yayınlayıp bağlantı kurmamak** — Yetim sayfa oluşturur
4. **İç bağlantılarda nofollow kullanmak** — Otorite akışını keser
5. **Target="_blank" kullanmak** — İç bağlantılarda gereksiz, UX bozar
6. **Aşırı bağlantı vermek** — Paragraf başına 1-2 bağlantıyı aşma
7. **İlgisiz sayfalara bağlantı vermek** — Tematik sinyal bozulur
8. **Yönlendirme zinciri bırakmak** — A→B→C yerine A→C olmalı
9. **Sadece yeni→eski bağlantı kurmak** — Eski→yeni de kritik; çift yönlü düşün
10. **Bağlantıyı bir kez kurup unutmak** — İç bağlantı sürekli bakım gerektirir
