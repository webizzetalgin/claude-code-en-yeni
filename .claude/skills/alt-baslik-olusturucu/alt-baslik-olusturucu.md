---
name: seo-search-intent
description: "Anahtar kelime bazlı arama niyeti (search intent) analizi yaparak SEO uyumlu içerik başlık kurgusu oluşturur. Bu skill'i şu durumlarda tetikle: kullanıcı bir anahtar kelime verip alt başlık, H2/H3 başlık, içerik kurgusu, makale iskeleti, blog yapısı, SEO başlık önerisi, arama niyeti analizi, search intent, içerik planı, content outline, başlık hiyerarşisi, silo yapısı veya semantik başlık varyasyonu istediğinde. 'Şu anahtar kelime için başlıklar oluştur', 'bu konu için içerik planla', 'SEO uyumlu başlıklar yaz', 'arama niyetine göre kurgu yap' gibi ifadelerde de tetiklenmeli. Türkçe veya İngilizce anahtar kelimelerle çalışır."
---

# SEO Arama Niyeti Analizi ve İçerik Başlık Kurgusu

Verilen anahtar kelimeyi temel alarak, arama niyetini (search intent) analiz edip kapsamlı, SEO uyumlu, kullanıcı odaklı içerik başlık hiyerarşisi oluşturan skill.

---

## Roller ve Perspektif

Bu skill çalıştırıldığında Claude şu üç rolü aynı anda üstlenir:

1. **SEO Uzmanı** — Anahtar kelime optimizasyonu, SERP analizi, arama hacmi mantığı
2. **İçerik Stratejisti** — Konu derinliği, bilgi mimarisi, editorial akış
3. **UX Araştırmacısı** — Kullanıcı yolculuğu, arama niyeti sınıflandırması, soru kalıpları

---

## Tetikleme Koşulları

Aşağıdakilerden herhangi biri geçerliyse bu skill tetiklenir:

- Kullanıcı bir anahtar kelime verip "başlık oluştur", "alt başlık yaz", "içerik kurgusu yap" derse
- "SEO uyumlu", "arama niyeti", "search intent", "H2/H3", "content outline" ifadeleri geçerse
- "Bu anahtar kelime için makale planla", "blog iskeleti çıkar" gibi talepler gelirse
- Kullanıcı sadece bir anahtar kelime yazıp başlık beklerse (önceki bağlamda bu görev tanımlanmışsa)

---

## Kesin Kurallar (Her Çalıştırmada Uyulması Zorunlu)

### Kural 1: Başlangıç Şartı
Her alt başlık, **istisnasız** doğrudan verilen anahtar kelime ile başlamalıdır.

```
✅ DOĞRU (anahtar kelime: "Web Tasarım")
   H2: Web Tasarım Nedir ve Neden Önemlidir?
   H2: Web Tasarım Fiyatları Ne Kadar?
   H3: Web Tasarım Sürecinde Dikkat Edilmesi Gerekenler

❌ YANLIŞ
   H2: Modern Bir Web Tasarım Nasıl Yapılır?        → "Modern Bir" ile başlıyor
   H2: Profesyonel Web Tasarım Hizmetleri            → "Profesyonel" ile başlıyor
   H2: En İyi Web Tasarım Trendleri                  → "En İyi" ile başlıyor
   H2: Neden Web Tasarım Yaptırmalısınız?             → "Neden" ile başlıyor
```

**Bu kural mutlaktır.** Başlığın ilk kelimesi/kelime grubu tam olarak verilen anahtar kelime olmalıdır. Anahtar kelimenin önüne hiçbir sıfat, zarf, bağlaç veya başka bir sözcük eklenmez.

### Kural 2: Anlamsal Varyasyon ve Soru Kalıpları
Başlıkların devamında aşağıdaki soru ve ifade kalıplarından yararlan:

**Bilgi Amaçlı (Informational)**
- Nedir?, Ne Demek?, Ne İşe Yarar?
- Nasıl Çalışır?, Nasıl Yapılır?, Nasıl Uygulanır?
- Tarihçesi, Gelişimi, Evrimi
- Türleri, Çeşitleri, Yöntemleri
- Avantajları ve Dezavantajları
- Örnekleri, Kullanım Alanları

**Ticari Amaçlı (Commercial Investigation)**
- Fiyatları Ne Kadar?, Maliyeti Nedir?
- En İyi ... Hangisi?, Karşılaştırması
- ... mı ... mı? (Kıyaslama)
- Yorumları, Değerlendirmesi
- Alternatifleri Nelerdir?

**İşlemsel (Transactional)**
- Nasıl Satın Alınır?, Nereden Alınır?
- İndirim, Kampanya, Fırsat
- Sipariş, Başvuru, Kayıt

**Navigasyonel (Navigational)**
- Resmi Sitesi, İletişim
- Giriş, Panel, Uygulama

### Kural 3: Minimum 10 Başlık
Kesinlikle en az 10 adet farklı, özgün ve doyurucu alt başlık üretilmelidir. Tercihen 12-18 arası başlık idealdir.

### Kural 4: Konsept Bütünlüğü
Tüm başlıklar anahtar kelimenin ana konseptine ve kullanıcının olası arama yolculuğuna hizmet etmelidir. Konu dışı, genel geçer veya dolgu niteliğinde başlıklardan kaçın.

### Kural 5: Mantıksal Akış ve Hiyerarşi
Başlıklar, bir içeriğin doğal okuma akışına uygun sıralanmalıdır:

```
AKIŞ SIRASI:
1. Tanım / Temel Kavram      → "X Nedir?"
2. Önem / Neden Gerekli       → "X Neden Önemlidir?"
3. Türler / Çeşitler          → "X Türleri Nelerdir?"
4. Nasıl Yapılır / Süreç      → "X Nasıl Yapılır?"
5. Dikkat Edilecekler          → "X Yaparken Dikkat Edilmesi Gerekenler"
6. Avantaj / Dezavantaj        → "X Avantajları ve Dezavantajları"
7. Fiyat / Maliyet            → "X Fiyatları Ne Kadar?"
8. Karşılaştırma              → "X vs Y: Hangisi Daha İyi?"
9. Örnekler / Uygulamalar     → "X Örnekleri ve Başarılı Uygulamalar"
10. Sık Sorulan Sorular       → "X Hakkında Sık Sorulan Sorular"
```

---

## Adım Adım İş Akışı

### Adım 1: Anahtar Kelimeyi Al ve Ayrıştır

Kullanıcının verdiği anahtar kelimeyi tanımla:
- Anahtar kelimenin kelime sayısını belirle (tek kelime mi, long-tail mı?)
- Anahtar kelimenin dilini belirle (Türkçe / İngilizce / diğer)
- Anahtar kelimenin sektör/niche alanını tespit et

### Adım 2: Arama Niyetini Sınıflandır

Anahtar kelimeyi 4 temel niyet kategorisinde değerlendir:

| Niyet Türü | Açıklama | Sinyal Kelimeleri |
|------------|----------|-------------------|
| **Informational** | Bilgi edinme | nedir, nasıl, neden, ne zaman |
| **Commercial** | Araştırma/kıyaslama | en iyi, karşılaştırma, fiyat, yorum |
| **Transactional** | Satın alma/aksiyon | satın al, sipariş, indir, kayıt |
| **Navigational** | Belirli siteye yönelim | giriş, resmi site, iletişim |

Çoğu anahtar kelime birden fazla niyete hizmet edebilir. Baskın niyeti belirle ama diğerlerini de kapsayacak başlıklar üret.

### Adım 3: Başlık Seti Oluşturma

Aşağıdaki şablonu kullanarak başlıkları üret. Her başlık mutlaka anahtar kelime ile başlamalı:

```
## [Anahtar Kelime] + [Tanım Kalıbı]
## [Anahtar Kelime] + [Süreç/Nasıl Kalıbı]
## [Anahtar Kelime] + [Türler/Çeşitler Kalıbı]
## [Anahtar Kelime] + [Avantaj/Fayda Kalıbı]
## [Anahtar Kelime] + [Dikkat/Uyarı Kalıbı]
## [Anahtar Kelime] + [Fiyat/Maliyet Kalıbı]
## [Anahtar Kelime] + [Karşılaştırma Kalıbı]
## [Anahtar Kelime] + [Hata/Sorun Kalıbı]
## [Anahtar Kelime] + [Örnek/Uygulama Kalıbı]
## [Anahtar Kelime] + [Trend/Gelecek Kalıbı]
### [Anahtar Kelime] + [Detay/Alt Konu H3'ler]
```

### Adım 4: Kalite Kontrolü

Üretilen her başlığı şu kontrol listesinden geçir:

- [ ] Başlık anahtar kelime ile mi başlıyor? (Kural 1)
- [ ] Soru kalıbı veya anlamsal varyasyon içeriyor mu? (Kural 2)
- [ ] Toplam başlık sayısı 10'dan fazla mı? (Kural 3)
- [ ] Ana konuyla doğrudan alakalı mı? (Kural 4)
- [ ] Mantıksal sıra bozulmuyor mu? (Kural 5)
- [ ] Başlık yeterince spesifik ve doyurucu mu? (genel geçer değil)
- [ ] Diğer başlıklarla çakışma veya tekrar var mı?

---

## Çıktı Formatı

Çıktıyı aşağıdaki formatta sun. Çıktının başında kısa bir arama niyeti analizi yap, ardından başlıkları listele:

```
## 🔍 Arama Niyeti Analizi

**Anahtar Kelime:** [kullanıcının verdiği kelime]
**Baskın Niyet:** [Informational / Commercial / Transactional / Navigational]
**Destekleyici Niyetler:** [varsa diğer niyetler]
**Hedef Kitle Profili:** [bu kelimeyi arayan kişinin muhtemel profili]

---

## 📋 Önerilen İçerik Başlık Hiyerarşisi

### H2 Başlıklar (Ana Bölümler)

1. **H2:** [Anahtar Kelime] Nedir? [Kısa açıklama]
2. **H2:** [Anahtar Kelime] Nasıl ...?
3. **H2:** [Anahtar Kelime] Türleri ...
...

### H3 Başlıklar (Alt Bölümler)

- **H3 (2. başlığın altı):** [Anahtar Kelime] ...
- **H3 (3. başlığın altı):** [Anahtar Kelime] ...
...

---

## 💡 İçerik Stratejisi Notları

- [Bu içeriğin nasıl zenginleştirilebileceğine dair 2-3 kısa öneri]
- [Dahili bağlantı (internal link) önerileri]
- [Featured snippet / öne çıkan sonuç hedefleme ipuçları]
```

---

## Sektöre Göre Uyarlama İpuçları

Anahtar kelime farklı sektörlerden gelebilir. Sektöre göre başlık kalıplarını uyarla:

### Sağlık / Medikal
- "X Belirtileri Nelerdir?", "X Tedavisi Nasıl Yapılır?", "X Ameliyatı Riskleri"
- E-A-T (Uzmanlık-Otorite-Güvenilirlik) sinyalleri önemli, başlıklara güven veren ifadeler ekle

### Teknoloji / Yazılım
- "X Kurulumu Nasıl Yapılır?", "X Sistem Gereksinimleri", "X vs Y Karşılaştırması"
- Versiyon numaraları, güncel yıl (2024, 2025) eklemek CTR artırır

### E-Ticaret / Ürün
- "X Fiyatları", "X Yorumları", "X Nereden Satın Alınır?", "X İndirim ve Kampanyaları"
- Transactional niyetli başlıklara ağırlık ver

### Hizmet Sektörü
- "X Hizmeti Nedir?", "X Nasıl Yaptırılır?", "X Firması Seçerken Dikkat Edilecekler"
- Yerel SEO sinyalleri: şehir/bölge bazlı varyasyonlar eklenebilir

### Eğitim / Kurs
- "X Eğitimi Nasıl Alınır?", "X Sertifikası Ne İşe Yarar?", "X Öğrenmek İçin En İyi Kaynaklar"
- Kariyer odaklı başlıklar ekle

### Finans / Yatırım
- "X Nedir Nasıl Yatırım Yapılır?", "X Riskleri Nelerdir?", "X Vergilendirmesi"
- Güncellik çok önemli, yıl belirt

---

## Sık Yapılan Hatalar ve Kaçınılması Gerekenler

1. **Başlığın başına ek kelime koymak**
   - ❌ "En İyi Web Tasarım Firmaları" → Kural 1 ihlali
   - ✅ "Web Tasarım Firmaları: En İyiler Hangileri?"

2. **Genel geçer, boş başlıklar**
   - ❌ "Web Tasarım Hakkında Bilmeniz Gerekenler" → çok belirsiz
   - ✅ "Web Tasarım Sürecinde Dikkat Edilmesi Gereken 7 Kritik Nokta"

3. **Başlıklar arası tekrar**
   - ❌ "Web Tasarım Nasıl Yapılır?" ve "Web Tasarım Yapmak İçin Adımlar" → aynı niyet
   - ✅ Birini sürece, diğerini araçlara veya yöntemlere odakla

4. **Arama niyetiyle uyumsuz başlık**
   - Bilgi amaçlı aranan bir kelime için sadece fiyat/satış başlıkları koymak
   - Tüm niyet türlerini dengeli kapsa

5. **Hiyerarşi bozukluğu**
   - H3 başlıkları bağımsız H2'ler gibi kullanmak
   - H3'ler mutlaka bir H2'nin altında ve ona bağlı olmalı

6. **Fazla benzer kalıp tekrarı**
   - Her başlığı "Nedir?" ile bitirmek monotonluk yaratır
   - Soru kalıplarını çeşitlendir: Nedir, Nasıl, Neden, Hangileri, Ne Zaman, Dikkat Edilecekler...

---

## Dil Desteği

- **Türkçe anahtar kelimeler:** Soru ekleri (-mı, -mi), bağlaçlar (ve, veya, ile) ve Türk arama davranışına uygun kalıplar kullan
- **İngilizce anahtar kelimeler:** "What is", "How to", "Best", "vs", "Cost of", "Guide to" gibi kalıplar kullan
- **Karışık dil:** Türkçe içerikte İngilizce terim kullanılıyorsa (örn. "SEO", "CRM"), anahtar kelimeyi olduğu gibi koru

---

## Bonus: Featured Snippet Hedefleme

Bazı başlıkları Google Featured Snippet (sıfır pozisyon) hedefleyecek şekilde formüle et:

- **Tanım snippet:** "[Anahtar Kelime] Nedir?" → İlk paragrafta 40-60 kelimelik net tanım
- **Liste snippet:** "[Anahtar Kelime] Türleri" → Numaralı veya madde işaretli liste
- **Tablo snippet:** "[Anahtar Kelime] Karşılaştırması" → Tablo formatında veri
- **Adım snippet:** "[Anahtar Kelime] Nasıl Yapılır?" → Adım adım süreç

---

## Son Kontrol

Tüm çıktı hazırlandıktan sonra şu soruları sor:

1. Her başlık verilen anahtar kelime ile mi başlıyor?
2. En az 10 farklı başlık var mı?
3. Başlıklar arasında mantıksal bir okuma akışı var mı?
4. Farklı arama niyetleri (bilgi, ticari, işlemsel) temsil ediliyor mu?
5. Soru kalıpları yeterince çeşitli mi?
6. Konu dışına sapan başlık var mı?
7. Featured snippet hedefleyen en az 2-3 başlık var mı?

Tümüne "evet" cevabı verilebiliyorsa, çıktı hazırdır.
