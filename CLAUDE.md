# CLAUDE.md — Bu Proje İçin Kalıcı Kurallar

---

## ⚡ OTOMATİK ÖĞRENME SİSTEMİ — NASIL ÇALIŞIR

> Bu sistem **pasif değil aktiftir.** Kullanıcının hatırlatmasına gerek yok; Claude her tetikleyici anında kendisi kaydeder.

---

### ADIM 1 — Her Sohbet Başında (ZORUNLU, ilk 30 saniye)

```
1. memory/MEMORY.md → oku, tüm linkleri içselleştir
2. İlgili memory dosyalarını oku (proje/feedback türleri öncelikli)
3. LEARN.md → son 3 entry'yi oku (önceki çözümleri hatırla, tekrar arama)
```

---

### ADIM 2 — Sohbet İçi Anlık Kayıt (ZORUNLU — erteleme yok)

**Bu tetikleyicilerden biri oluştuğu anda tool çağrısını bırak, önce kaydet:**

| # | Tetikleyici | Nereye | Ne Kaydet |
|---|-------------|--------|-----------|
| T1 | Bash/Python hata verdi → farklı yöntem çalıştı | `LEARN.md` | Hata + çözüm ikisi birlikte |
| T2 | Yeni kütüphane/API/yöntem ilk kez başarıyla çalıştı | `LEARN.md` + `project_*.md` | Minimum çalışan kod snippet |
| T3 | Kullanıcı "hayır / öyle değil / şöyle yap" dedi | `feedback_*.md` | Kural + Why + How to apply |
| T4 | Kullanıcı "evet / tam bu / mükemmel / onaylıyorum" dedi | `feedback_*.md` | Onaylanan yaklaşımı da kaydet |
| T5 | Kullanıcı proje hakkında yeni bilgi verdi | `project_*.md` | Yazı sayısı, Post ID, site ayarı |
| T6 | Script başarıyla tamamlandı (0 hata) | `LEARN.md` | Sonuç özeti + dosya/ID listesi |
| T7 | Yeni bir skill/iş akışı ilk kez tamamlandı | `LEARN.md` + yeni `project_*.md` | Akış adımları + çıktılar |
| T8 | Yeni site/proje bilgisi geldi (URL, şifre, API) | yeni `project_*.md` | Tüm bağlantı bilgileri |
| T9 | Kullanıcı yeni tercih/kural belirtti | `feedback_*.md` | Kural net biçimde yaz |

**Kayıt sırası:** Tetikleyici oluşur → dosya güncellenir → asıl işe devam edilir.
**"Sohbet sonunda kaydederim" = YASAK** — context tükenirse kayıp olur.

---

### Tetikleyici Örnekleri (Somut Senaryolar)

**T1 örneği:** WebFetch 403 verdi → curl ile çalıştı → hemen LEARN.md'ye ekle, sonra işe devam et.

**T3 örneği:** Kullanıcı "JSON istemiştim" dedi → feedback_elementor_json.md güncelle/oluştur, sonra JSON üret.

**T6 örneği:** `wp_yukle.py` 13/13 başarılı yazdı → LEARN.md + project_neidir.md güncelle, sonra kullanıcıya bildir.

**T7 örneği:** İlk kez Elementor JSON üretildi ve onaylandı → LEARN.md + project_site_olusturma.md akışı kaydet.

**Eğer bir sohbette hiç kayıt yapmadım → sohbet sonu kontrol listesinde mutlaka tamamla.**

---

### ADIM 3 — Sohbet Sonu Zorunlu Kontrol Listesi

Her sohbet sonunda sırayla uygula (kullanıcı "tamam" veya "teşekkürler" dediğinde):

```
☐ 1. LEARN.md → ## [YYYY-MM-DD] SOHBET ÖZETİ — [konu] ekle
       - Yapılanlar listesi (madde madde)
       - Yeni öğrenilen (varsa, spesifik)
       - Site/dosya durumu değiştiyse (yazı sayısı, son post ID, üretilen dosyalar)

☐ 2. İlgili project_*.md → sayılar/durum değiştiyse güncelle

☐ 3. MEMORY.md → yeni memory dosyası oluşturduysan pointer ekle
       (200 satır sınırı var — kısa tut)

☐ 4. CLAUDE.md → "Site Bilgileri" bölümü eskidiyse güncelle
```

---

### Kayıt Formatları

**LEARN.md entry:**
```markdown
## [YYYY-MM-DD] Kısa Başlık

**Bağlam:** Ne yapılıyordu?
**Başarısız yöntem (varsa):** X → hata
**Çalışan yöntem:**
```python
# minimum çalışan kod
```
**Not:** Dikkat edilecek ayrıntı
```

**Memory dosyası:**
```markdown
---
name: Kısa isim
description: Bir cümle — gelecekte relevance tespiti için spesifik yaz
type: feedback | project | user | reference
---

Kural veya bilgi.

**Why:** Neden bu kural var?
**How to apply:** Ne zaman, hangi durumda uygulanır?
```

---

## WordPress Entegrasyon Kuralları

### Kimlik Doğrulama (TÜM Türkçe WP siteleri için)
- REST API basic auth → **ÇALIŞMAZ** (403)
- **Çalışan:** `requests` + Cookie/Nonce
- Login `wp-submit`: **"Oturum aç"** — "Log In" ÇALIŞMAZ
- Login öncesi `GET /wp-login.php` (test cookie)
- `redirect_to` tam URL, `Referer` header gerekli

### İçerik Yükleme
- İçerikleri ayrı dosyaya yazma → Python scriptine göm (triple-quote)
- Post güncelleme: `POST` + `X-HTTP-Method-Override: PATCH`
- Kategori: `Uncategorized (ID:1)` — teyit edilmedikçe değiştirme
- Zamanlama: `"date": "YYYY-MM-DDTHH:MM:SS"`, `status: "future"` (TSİ = UTC+3, saat 16:00)
- Taslak: `status: "draft"` (her zaman önce taslak)

### Büyük İçerik Serileri (N > 5 makale)
- N makaleyi 4-5'erli batch script'lere böl
- Her batch ayrı `.py` dosyası: `generate_konu_1_4.py`, `generate_konu_5_9.py`
- Tek `wp_yukle.py` scripti tüm batch'lerin çıktısını yükler
- `docx_to_html()` fonksiyonuyla Gutenberg blok dönüşümü (detay: `LEARN.md`)

### SEO Ayarları
- Yoast noindex → REST API KAPALI → **XML-RPC** ile `wp.editPost` + `custom_fields`
- Başarı: XML-RPC response `<boolean>1</boolean>`

### İç Linkleme
- Yeni içerikler önce linksiz yükle → id/url al
- `GET /wp-json/wp/v2/posts?per_page=100` ile mevcut yazıları çek
- Keyword eşleşmesiyle related posts bul → güncelle
- 3+ kelime H1 → max 3 iç link | 1-2 kelime H1 → max 7 iç link

---

## Elementor / Site Oluşturma Kuralları

### HTML mi, JSON mu?
- Elementor kullanan site → **Elementor JSON** (import formatı, `[konu]-elementor.json`)
- HTML bloğu / Özel HTML widget → **HTML embed** (`wordpress-embed.html`)
- Eğer belirsizse → kullanıcıya sor

### KRİTİK — Gutenberg vs Elementor
- `wordpress-site-olusturma-en-guncel` skill tetiklense bile → hedef site Elementor kullanıyorsa çıktı **Elementor JSON** (`version: "0.4"`, `elType: section/column/widget`) olmalı
- Gutenberg `<!-- wp:... -->` blok formatı Elementor siteler için YANLIŞTIR
- **"Şablonlar > İçe Aktar"** ifadesi = Elementor JSON demektir

### Tasarım Kalitesi İçin
- Görsel çıktıyı göremediğimden kalite generic kalabilir
- En iyi çıktı için: (1) beğenilen Elementor export JSON, (2) referans screenshot, (3) spesifik eleştiri
- `custom_css` alanı olmadan hover/animasyon efektleri eksik kalır

### Elementor JSON — Kritik
- `custom_css` ile hover: `selector .elementor-column .elementor-widget-wrap { ... }`
- Sütun border/arka plan → `.elementor-widget-wrap`'a uygulanır
- `transform: translateY` → `.elementor-column`'a uygulanır
- İkon arkaplanı: `.elementor-icon-box-icon { display:flex; width:52px; height:52px; background:rgba(...); }`
- Eyebrow label: `<span style="display:inline-block;width:22px;height:2px;background:#RENK;vertical-align:middle;margin-right:10px;"></span>Metin`

### Bot Korumalı Site (403)
- WebFetch → 403 verirse → `curl -A "Mozilla/5.0..." -H "Accept-Language: tr-TR"` dene

---

## Site Bilgileri

### akdeniztravel.com
- URL: https://www.akdeniztravel.com | Admin: /wp-admin/
- SEO: Yoast SEO v27.1.1 | Builder: Elementor
- Kategoriler: İstanbul/Ankara/Antalya/... Gezi Rehberi, Seyahat Tavsiyeleri, Uncategorized (ID:1)
- **25 yazı mevcut (son kontrol: 2026-03-21)**
- Son eklenen: "Kortizon İğnesi Nedir?" — Post ID: 15851 (taslak, noindex)

### neidir.com
- URL: https://neidir.com | Admin: /wp-admin/
- **Son yükleme: 2026-03-28** — 13 uyku bozukluğu taslağı (Post ID: 9381–9393)
- Detaylar: `memory/project_neidir.md`

### aksoylarkurye.com
- URL: https://aksoylarkurye.com | Builder: **Elementor**
- İletişim: +90 532 207 96 09 | Sultangazi/İstanbul
- Tasarım referansı: Medicora (`#0D59F2` + `#0A1F33` + `#F0F5FF`)
- Üretilen: `aksoylar-kurye-medicora.json` (Elementor Şablonlar > İçe Aktar)
- Detaylar: `memory/project_aksoylarkurye.md`

---

## Genel Kurallar
- Windows Python encoding: `sys.stdout.reconfigure(encoding='utf-8')` — her scriptin başına
- Bash heredoc içinde Python string → dosyaya yaz, `python dosya.py` ile çalıştır
- Temp dosya oluşturma; scripte göm veya proje klasörüne kaydet
- `urllib` yerine `requests` kullan
