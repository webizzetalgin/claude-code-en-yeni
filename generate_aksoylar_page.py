import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

# ─────────────────────────────────────────────
# YARDIMCI FONKSİYONLAR
# ─────────────────────────────────────────────

def badge(text, dark=False):
    bg = "#FFFFFF1A" if dark else "#F0F5FF"
    color = "#FFFFFF" if dark else "#0D59F2"
    return f"""<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"11px","fontWeight":"600","letterSpacing":"1.5px","textTransform":"uppercase"}},"color":{{"text":"{color}","background":"{bg}"}},"spacing":{{"padding":{{"top":"6px","bottom":"6px","left":"12px","right":"12px"}}}}}}}} -->
<p class="has-text-color has-background" style="background-color:{bg};color:{color};font-size:11px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;padding-top:6px;padding-bottom:6px;padding-left:12px;padding-right:12px;display:inline-block">{text}</p>
<!-- /wp:paragraph -->"""

def h1(text, color="#FFFFFF", size="52px", weight="700", line_height="1.15"):
    return f"""<!-- wp:heading {{"level":1,"style":{{"typography":{{"fontSize":"{size}","fontWeight":"{weight}","lineHeight":"{line_height}"}},"color":{{"text":"{color}"}}}}}} -->
<h1 class="wp-block-heading has-text-color" style="color:{color};font-size:{size};font-weight:{weight};line-height:{line_height}">{text}</h1>
<!-- /wp:heading -->"""

def h2(text, color="#0A1F33", size="36px", weight="700", align="left"):
    align_attr = f'"textAlign":"{align}",' if align != "left" else ""
    align_style = f"text-align:{align};" if align != "left" else ""
    return f"""<!-- wp:heading {{"level":2,{align_attr}"style":{{"typography":{{"fontSize":"{size}","fontWeight":"{weight}","lineHeight":"1.25"}},"color":{{"text":"{color}"}}}}}} -->
<h2 class="wp-block-heading has-text-color" style="color:{color};font-size:{size};font-weight:{weight};line-height:1.25;{align_style}">{text}</h2>
<!-- /wp:heading -->"""

def h3(text, color="#0A1F33", size="20px", weight="600"):
    return f"""<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontSize":"{size}","fontWeight":"{weight}","lineHeight":"1.3"}},"color":{{"text":"{color}"}}}}}} -->
<h3 class="wp-block-heading has-text-color" style="color:{color};font-size:{size};font-weight:{weight};line-height:1.3">{text}</h3>
<!-- /wp:heading -->"""

def para(text, color="#5A6A7A", size="16px", line_height="1.7", align="left"):
    align_attr = f'"align":"{align}",' if align != "left" else ""
    align_style = f"text-align:{align};" if align != "left" else ""
    return f"""<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"{size}","lineHeight":"{line_height}"}},"color":{{"text":"{color}"}}}}}} -->
<p class="has-text-color" style="color:{color};font-size:{size};line-height:{line_height};{align_style}">{text}</p>
<!-- /wp:paragraph -->"""

def spacer(h="24px"):
    return f"""<!-- wp:spacer {{"height":"{h}"}} -->
<div style="height:{h}" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->"""

def button(text, url="#", bg="#0D59F2", color="#FFFFFF", radius="6px"):
    return f"""<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"left"}}}} -->
<div class="wp-block-buttons"><!-- wp:button {{"style":{{"border":{{"radius":"{radius}"}},"color":{{"background":"{bg}","text":"{color}"}},"spacing":{{"padding":{{"top":"14px","bottom":"14px","left":"28px","right":"28px"}}}}}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background wp-element-button" href="{url}" style="border-radius:{radius};color:{color};background-color:{bg};padding-top:14px;padding-bottom:14px;padding-left:28px;padding-right:28px">{text}</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->"""

def button_centered(text, url="#", bg="#0D59F2", color="#FFFFFF", radius="6px"):
    return f"""<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"center"}}}} -->
<div class="wp-block-buttons"><!-- wp:button {{"style":{{"border":{{"radius":"{radius}"}},"color":{{"background":"{bg}","text":"{color}"}},"spacing":{{"padding":{{"top":"14px","bottom":"14px","left":"32px","right":"32px"}}}}}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background wp-element-button" href="{url}" style="border-radius:{radius};color:{color};background-color:{bg};padding-top:14px;padding-bottom:14px;padding-left:32px;padding-right:32px">{text}</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->"""

def buttons_two(text1, url1, text2, url2, justify="center"):
    return f"""<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"{justify}"}}}} -->
<div class="wp-block-buttons"><!-- wp:button {{"style":{{"border":{{"radius":"6px"}},"color":{{"background":"#0D59F2","text":"#FFFFFF"}},"spacing":{{"padding":{{"top":"14px","bottom":"14px","left":"28px","right":"28px"}}}}}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background wp-element-button" href="{url1}" style="border-radius:6px;color:#FFFFFF;background-color:#0D59F2;padding-top:14px;padding-bottom:14px;padding-left:28px;padding-right:28px">{text1}</a></div>
<!-- /wp:button -->

<!-- wp:button {{"className":"is-style-outline","style":{{"border":{{"radius":"6px","width":"2px"}},"color":{{"text":"#FFFFFF"}},"spacing":{{"padding":{{"top":"14px","bottom":"14px","left":"28px","right":"28px"}}}}}}}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link has-text-color wp-element-button" href="{url2}" style="border-radius:6px;border-width:2px;color:#FFFFFF;padding-top:14px;padding-bottom:14px;padding-left:28px;padding-right:28px">{text2}</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->"""

def separator():
    return """<!-- wp:separator {"style":{"color":{"background":"#E2E8F0"}},"className":"is-style-wide"} -->
<hr class="wp-block-separator has-text-color has-background is-style-wide" style="background-color:#E2E8F0;color:#E2E8F0"/>
<!-- /wp:separator -->"""

# ─────────────────────────────────────────────
# BÖLÜM 1: HERO
# ─────────────────────────────────────────────
hero = """<!-- wp:cover {"overlayColor":"","customOverlayColor":"#0A1F33","dimRatio":85,"minHeight":600,"isDark":true,"align":"full","style":{"spacing":{"padding":{"top":"120px","bottom":"120px","left":"24px","right":"24px"}}}} -->
<div class="wp-block-cover alignfull is-dark" style="min-height:600px;padding-top:120px;padding-bottom:120px;padding-left:24px;padding-right:24px">
<span aria-hidden="true" class="wp-block-cover__background has-background-dim" style="background-color:#0A1F33;opacity:0.85"></span>
<!-- [GÖRSEL: Hero arka plan görseli — moto kurye veya şehir görseli ekleyin] -->
<div class="wp-block-cover__inner-container">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"720px"}} -->
<div class="wp-block-group">

""" + badge("AKSOYLAR KURYE — İSTANBUL", dark=True) + "\n\n" + spacer("16px") + "\n\n" + h1("Aksoylar Kurye İle Zamanında Teslimat Avantajı") + "\n\n" + spacer("20px") + "\n\n" + para("İstanbul moto kurye firması olarak acil iletilmesi gereken gönderilere ivedilikle karşılık veriyoruz. Şehrin her noktasına hızlı ve güvenilir teslimat hizmetindeyiz.", color="#CBD5E1", size="18px", line_height="1.7") + "\n\n" + spacer("32px") + "\n\n" + buttons_two("Kurye Çağır", "tel:+905322079609", "Hemen Bilgi Alın", "#iletisim", justify="left") + """

</div>
<!-- /wp:group -->

</div>
</div>
<!-- /wp:cover -->"""

# ─────────────────────────────────────────────
# BÖLÜM 2: İSTATİSTİK / INFO BOXES
# ─────────────────────────────────────────────
def info_box(number, title, desc, border_right=True):
    border = ' style="border-right:1px solid rgba(0,0,0,0.08)"' if border_right else ""
    return f"""<!-- wp:column -->
<div class="wp-block-column"{border}>

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"40px","bottom":"40px","left":"30px","right":"30px"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group" style="padding-top:40px;padding-bottom:40px;padding-left:30px;padding-right:30px">

<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontSize":"42px","fontWeight":"700","lineHeight":"1"}},"color":{{"text":"#0D59F2"}}}}}} -->
<h3 class="wp-block-heading has-text-color" style="color:#0D59F2;font-size:42px;font-weight:700;line-height:1">{number}</h3>
<!-- /wp:heading -->

{spacer("12px")}

<!-- wp:heading {{"level":4,"style":{{"typography":{{"fontSize":"17px","fontWeight":"600","lineHeight":"1.3"}},"color":{{"text":"#0A1F33"}}}}}} -->
<h4 class="wp-block-heading has-text-color" style="color:#0A1F33;font-size:17px;font-weight:600;line-height:1.3">{title}</h4>
<!-- /wp:heading -->

{spacer("8px")}

{para(desc, color="#5A6A7A", size="14px", line_height="1.6")}

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->"""

stats_section = """<!-- wp:group {"align":"full","style":{"color":{"background":"#F0F5FF"},"spacing":{"padding":{"top":"0px","bottom":"0px","left":"0px","right":"0px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#F0F5FF">

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"left":"0px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

""" + info_box("%99", "Hızlı Kurye Desteği", "Aksoylar Kurye, %99 hızlı kurye desteği sağlayarak iş süreçlerinin aksamadan ilerlemesine katkı sağladı.") + "\n\n" + info_box("✓", "Profesyonel Hizmet", "Profesyonel hizmet sunularak teslimatlar sorunsuz şekilde tamamlandı.") + "\n\n" + info_box("⚡", "Acil Durumların Çözülmesi", "Acil durumlar çözülerek herkes büyük sorunlardan kurtuldu.") + "\n\n" + info_box("✦", "İş Gücü Tasarrufu", "Aksoylar Kurye ile teslimatlar yapıldı ve firmalar iş gücü tasarrufuna sahip oldu.", border_right=False) + """

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# BÖLÜM 3: HİZMETLER
# ─────────────────────────────────────────────
def service_card(label, title, desc):
    return f"""<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {{"style":{{"color":{{"background":"#FFFFFF"}},"spacing":{{"padding":{{"top":"30px","bottom":"30px","left":"30px","right":"30px"}}}},"border":{{"radius":"8px","width":"1px","color":"#E2E8F0","style":"solid"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-background" style="background-color:#FFFFFF;padding-top:30px;padding-bottom:30px;padding-left:30px;padding-right:30px;border-radius:8px;border:1px solid #E2E8F0">

<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"11px","fontWeight":"600","letterSpacing":"1.2px","textTransform":"uppercase"}},"color":{{"text":"#0D59F2"}}}}}} -->
<p class="has-text-color" style="color:#0D59F2;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase">{label}</p>
<!-- /wp:paragraph -->

{spacer("8px")}

{h3(title, color="#0A1F33", size="22px", weight="700")}

{spacer("12px")}

{para(desc, color="#5A6A7A", size="15px", line_height="1.65")}

{spacer("20px")}

<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"14px","fontWeight":"600"}},"color":{{"text":"#0D59F2"}}}}}} -->
<p class="has-text-color" style="color:#0D59F2;font-size:14px;font-weight:600">→ İncele</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->"""

services_section = """<!-- wp:group {"align":"full","style":{"color":{"background":"#FFFFFF"},"spacing":{"padding":{"top":"80px","bottom":"80px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#FFFFFF;padding-top:80px;padding-bottom:80px;padding-left:24px;padding-right:24px">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"1100px"}} -->
<div class="wp-block-group">

""" + badge("HİZMETLERİMİZ") + "\n\n" + spacer("16px") + "\n\n" + h2("Aksoylar Kurye Hizmetlerimizle Tanışın") + "\n\n" + spacer("12px") + "\n\n" + para("Sunmuş olduğumuz hizmet seçeneklerimizle tanışın.") + "\n\n" + spacer("12px") + "\n\n" + button("Hizmetlerimiz Sayfasını Görüntüle", "/hizmetlerimiz", bg="#0A1F33") + "\n\n" + spacer("48px") + """

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"top":"24px","left":"24px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

""" + service_card("Gün içi teslimat", "Moto Kurye", "Moto kurye, evrakların, paketlerin, hediyelik ürünlerin ve benzeri eşyaların gün içinde teslimatının yapıldığı hizmettir.") + "\n\n" + service_card("Hızlı teslimat çözümü", "Acil Kurye", "Acil kurye, acil olan tüm teslimat işleri için en iyi çözüm olan hizmet seçeneğidir. Gönderiler en kısa sürede ulaştırılmaktadır.") + "\n\n" + service_card("Güvenilir taşıma", "Araçlı Kurye", "Araçlı kurye, büyük ebatlı ya da hassas gönderilerin taşınması için tercih edilen geniş zamanlı, ekonomik fiyatlı hizmettir.") + "\n\n" + service_card("Geniş hizmet kapsamı", "Şehirler Arası Kurye", "Şehirler arası kurye, acil ya da planlı olarak farklı şehirlere gerçekleştirilecek teslimatlar için kullanılan hizmettir.") + """

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# BÖLÜM 4: HAKKIMIZDA (2 sütun)
# ─────────────────────────────────────────────
about_section = """<!-- wp:group {"align":"full","style":{"color":{"background":"#F0F5FF"},"spacing":{"padding":{"top":"80px","bottom":"80px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#F0F5FF;padding-top:80px;padding-bottom:80px;padding-left:24px;padding-right:24px">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"1100px"}} -->
<div class="wp-block-group">

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"left":"60px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

<!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%">

""" + badge("HAKKIMIZDA") + "\n\n" + spacer("16px") + "\n\n" + h2("İstanbul Moto Kurye Olarak Hızlı Teslimatlarda Yanınızdayız!") + "\n\n" + spacer("20px") + "\n\n" + para("İstanbul motor kurye hizmetlerimiz sayesinde gönderileri hızlı ve güvenli bir şekilde varış noktasına ulaştırıyoruz. İstanbul'da gönderilerin araba ile teslimatın yapılması her zaman kolay olamayabiliyor. Bu nedenle hızlı kurye firması olarak bizler devreye giriyoruz.") + "\n\n" + spacer("16px") + "\n\n" + para("Gönderileri ivedi bir şekilde alıcı adresinden alıyor ve kısa süre içerisinde varış noktasına ulaştırıyoruz. İstanbul kurye olarak sunduğumuz bu çözümlerle, fabrikaların, işletmelerin ve bireylerin günlük iş akışını aksatmamalarını sağlıyoruz.") + "\n\n" + spacer("16px") + "\n\n" + para("İster acil bir evrak gönderiniz, isterseniz de önemli bir paket teslimatınız olsun, tüm gönderiler için her zaman yanınızda oluyoruz. Gönderilerin güvenliğini sağlamak adına ise her kuryeyi, uzman kadromuz ile birlikte eğitiyoruz.") + "\n\n" + spacer("32px") + "\n\n" + button("Hizmetlerimizi Keşfedin", "/hizmetlerimiz") + """

</div>
<!-- /wp:column -->

<!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%">

<!-- wp:group {"style":{"color":{"background":"#FFFFFF"},"spacing":{"padding":{"top":"40px","bottom":"40px","left":"40px","right":"40px"}},"border":{"radius":"12px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-background" style="background-color:#FFFFFF;padding-top:40px;padding-bottom:40px;padding-left:40px;padding-right:40px;border-radius:12px">

<!-- [GÖRSEL: Kurye veya teslimat görseli — 480x320px önerilir] -->

""" + h3("Neden Aksoylar Kurye?", color="#0A1F33", size="20px", weight="700") + "\n\n" + spacer("16px") + """

<!-- wp:list {"style":{"typography":{"fontSize":"15px"},"color":{"text":"#5A6A7A"},"spacing":{"blockGap":"12px"}}} -->
<ul class="has-text-color" style="color:#5A6A7A;font-size:15px">
<li>✓ İstanbul'un tüm bölgelerine teslimat</li>
<li>✓ %99 zamanında teslimat garantisi</li>
<li>✓ Uzman ve eğitimli kurye kadrosu</li>
<li>✓ 7/24 müşteri desteği</li>
<li>✓ Uygun ve şeffaf fiyat politikası</li>
</ul>
<!-- /wp:list -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# BÖLÜM 5: EKSTRA HİZMETLER (koyu arka plan)
# ─────────────────────────────────────────────
def extra_card(title, desc):
    return f"""<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {{"style":{{"color":{{"background":"rgba(255,255,255,0.06)"}},"spacing":{{"padding":{{"top":"28px","bottom":"28px","left":"28px","right":"28px"}}}},"border":{{"radius":"8px","width":"1px","color":"rgba(255,255,255,0.1)","style":"solid"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-background" style="background-color:rgba(255,255,255,0.06);padding-top:28px;padding-bottom:28px;padding-left:28px;padding-right:28px;border-radius:8px;border:1px solid rgba(255,255,255,0.1)">

{h3(title, color="#FFFFFF", size="17px", weight="600")}

{spacer("10px")}

{para(desc, color="#94A3B8", size="14px", line_height="1.6")}

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->"""

extra_section = """<!-- wp:group {"align":"full","style":{"color":{"background":"#0A1F33"},"spacing":{"padding":{"top":"80px","bottom":"80px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#0A1F33;padding-top:80px;padding-bottom:80px;padding-left:24px;padding-right:24px">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"1100px"}} -->
<div class="wp-block-group">

""" + badge("EKSTRA HİZMETLER", dark=True) + "\n\n" + spacer("16px") + "\n\n" + h2("Ekstra Hizmet Verdiğimiz Alanlar", color="#FFFFFF") + "\n\n" + spacer("12px") + "\n\n" + para("Vermiş olduğumuz hizmetlerin yanında ekstra olarak hizmet verdiğimiz alanlar şu şekildedir:", color="#94A3B8") + "\n\n" + spacer("48px") + """

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"top":"20px","left":"20px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

""" + extra_card("Vale & Şoför / Araç Muayene", "Vale, şoför ve araç muayene hizmetleri sunarak hayatınızı daha kolay hale getiriyoruz.") + "\n\n" + extra_card("Mağaza ve Market Alışverişi", "Kurye kadromuz ile mağaza ve market alışverişlerinizde istekleriniz için yardımcı oluyoruz.") + "\n\n" + extra_card("Ev Nakliyesi (Büyük Araç)", "Ev nakliyesi gibi durumlarda büyük araç ile nakliye sorunlarına uygun fiyatlarla çözüm getiriyoruz.") + """

</div>
<!-- /wp:columns -->

""" + spacer("20px") + """

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"top":"20px","left":"20px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

""" + extra_card("Toplu Dağıtım Günlük Kurye", "Toplu dağıtım kuryelerimizle tüm ürünlerin gün içinde dağıtılmasını sağlıyoruz.") + "\n\n" + extra_card("7/24 Çekici Hizmetleri", "7/24 çekici hizmeti sunarak yolda kaldığınız durumlarda hızlı şekilde destek sağlıyoruz.") + """

<!-- wp:column -->
<div class="wp-block-column"></div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# BÖLÜM 6: ACİL KURYE NASIL ALINIR
# ─────────────────────────────────────────────
howto_section = """<!-- wp:group {"align":"full","style":{"color":{"background":"#FFFFFF"},"spacing":{"padding":{"top":"80px","bottom":"80px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#FFFFFF;padding-top:80px;padding-bottom:80px;padding-left:24px;padding-right:24px">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"1100px"}} -->
<div class="wp-block-group">

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"left":"60px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

<!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%">

""" + badge("SÜRECİ ÖĞRENIN") + "\n\n" + spacer("16px") + "\n\n" + h2("Acil Kurye Hizmeti Almak İçin Ne Yapmak Gerekiyor?") + "\n\n" + spacer("20px") + "\n\n" + para("Acil kurye hizmetlerimizden yararlanma süreci oldukça basittir. Öncelik olarak gönderinizin boyutunu ve teslimat noktalarını belirtmeniz yeterlidir. Bu bilgiler tarafımıza ulaştıktan sonra sizlere en yakın kuryeyi yönlendirecek ve gönderilerinizi en kısa sürede teslim aldırtacağız.") + "\n\n" + spacer("16px") + "\n\n" + para("Hızlı kurye hizmetlerimizi toplantıya yetişmesi gereken evraklarda, yedek parçalarda, unutulan doğum günü hediyelerinde ve daha birçok alanda kullanabilirsiniz. İstanbul moto kurye kadromuz şehrin her tarafını bilen uzman kişilerden oluştuğu için teslimat süresi minimuma inecektir.") + "\n\n" + spacer("16px") + "\n\n" + para("İstanbul moto kurye fiyatları politikamız ise taşınacak gönderinin boyutuna, ağırlığına ve mesafeye göre değişkenlik göstermektedir. Ancak şüpheniz olmasın ki her zaman uygun fiyatlı hizmet vermeye özen gösteriyoruz.") + """

</div>
<!-- /wp:column -->

<!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%">

""" + """<!-- wp:group {"style":{"color":{"background":"#F0F5FF"},"spacing":{"padding":{"top":"40px","bottom":"40px","left":"40px","right":"40px"}},"border":{"radius":"12px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-background" style="background-color:#F0F5FF;padding-top:40px;padding-bottom:40px;padding-left:40px;padding-right:40px;border-radius:12px">

""" + h3("3 Adımda Kurye Çağırın", color="#0A1F33", size="20px", weight="700") + "\n\n" + spacer("24px") + """

<!-- wp:group {"style":{"spacing":{"blockGap":"20px"}},"layout":{"type":"flex","flexWrap":"nowrap","verticalAlignment":"top"}} -->
<div class="wp-block-group" style="gap:20px;display:flex;flex-wrap:nowrap;align-items:flex-start">
<!-- wp:group {"style":{"color":{"background":"#0D59F2"},"spacing":{"padding":{"top":"8px","bottom":"8px","left":"14px","right":"14px"}},"border":{"radius":"6px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-background" style="background-color:#0D59F2;padding-top:8px;padding-bottom:8px;padding-left:14px;padding-right:14px;border-radius:6px;min-width:36px;text-align:center"><p style="color:#fff;font-weight:700;font-size:16px;margin:0">1</p></div>
<!-- /wp:group -->
<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group">""" + h3("Bize Ulaşın", color="#0A1F33", size="16px", weight="600") + para("Telefon veya WhatsApp ile iletişime geçin.", color="#5A6A7A", size="14px") + """</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

""" + spacer("4px") + """

<!-- wp:group {"style":{"spacing":{"blockGap":"20px"}},"layout":{"type":"flex","flexWrap":"nowrap","verticalAlignment":"top"}} -->
<div class="wp-block-group" style="gap:20px;display:flex;flex-wrap:nowrap;align-items:flex-start">
<!-- wp:group {"style":{"color":{"background":"#0D59F2"},"spacing":{"padding":{"top":"8px","bottom":"8px","left":"14px","right":"14px"}},"border":{"radius":"6px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-background" style="background-color:#0D59F2;padding-top:8px;padding-bottom:8px;padding-left:14px;padding-right:14px;border-radius:6px;min-width:36px;text-align:center"><p style="color:#fff;font-weight:700;font-size:16px;margin:0">2</p></div>
<!-- /wp:group -->
<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group">""" + h3("Gönderinizi Bildirin", color="#0A1F33", size="16px", weight="600") + para("Boyut, ağırlık ve teslimat noktasını iletin.", color="#5A6A7A", size="14px") + """</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

""" + spacer("4px") + """

<!-- wp:group {"style":{"spacing":{"blockGap":"20px"}},"layout":{"type":"flex","flexWrap":"nowrap","verticalAlignment":"top"}} -->
<div class="wp-block-group" style="gap:20px;display:flex;flex-wrap:nowrap;align-items:flex-start">
<!-- wp:group {"style":{"color":{"background":"#0D59F2"},"spacing":{"padding":{"top":"8px","bottom":"8px","left":"14px","right":"14px"}},"border":{"radius":"6px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-background" style="background-color:#0D59F2;padding-top:8px;padding-bottom:8px;padding-left:14px;padding-right:14px;border-radius:6px;min-width:36px;text-align:center"><p style="color:#fff;font-weight:700;font-size:16px;margin:0">3</p></div>
<!-- /wp:group -->
<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group">""" + h3("Kuryeniz Yola Çıksın", color="#0A1F33", size="16px", weight="600") + para("En yakın kurye gönderinizi teslim alır.", color="#5A6A7A", size="14px") + """</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# BÖLÜM 7: NELER KAZANACAKSINIZ
# ─────────────────────────────────────────────
def benefit_card(title, desc):
    return f"""<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {{"style":{{"color":{{"background":"#FFFFFF"}},"spacing":{{"padding":{{"top":"36px","bottom":"36px","left":"36px","right":"36px"}}}},"border":{{"radius":"10px","width":"1px","color":"#E2E8F0","style":"solid"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-background" style="background-color:#FFFFFF;padding-top:36px;padding-bottom:36px;padding-left:36px;padding-right:36px;border-radius:10px;border:1px solid #E2E8F0">

{h3(title, color="#0A1F33", size="20px", weight="700")}

{spacer("14px")}

{para(desc, color="#5A6A7A", size="15px", line_height="1.7")}

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->"""

benefits_section = """<!-- wp:group {"align":"full","style":{"color":{"background":"#F0F5FF"},"spacing":{"padding":{"top":"80px","bottom":"80px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#F0F5FF;padding-top:80px;padding-bottom:80px;padding-left:24px;padding-right:24px">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"1100px"}} -->
<div class="wp-block-group">

""" + badge("AVANTAJLAR") + "\n\n" + spacer("16px") + "\n\n" + h2("Neler Kazanacaksınız?") + "\n\n" + spacer("48px") + """

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"top":"24px","left":"24px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

""" + benefit_card("Acil Hizmet İçin En İyi Çözüm", "Acil gönderileriniz için öncelikli ve hızlı teslimat imkanı sunarak en iyi çözümleri sunuyoruz. Bu sayede avantajlı hizmete kavuşuyorsunuz.") + "\n\n" + benefit_card("Uzman Kadro İle Çalışma Avantajı", "Firmamız bünyesinde uzman kadroyu bulundurarak müşterilerimizin en iyi hizmetlerimizden yararlanmalarını sağlıyoruz.") + """

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# BÖLÜM 8: FİNAL CTA
# ─────────────────────────────────────────────
final_cta = """<!-- wp:group {"align":"full","style":{"color":{"background":"#0A1F33"},"spacing":{"padding":{"top":"80px","bottom":"80px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#0A1F33;padding-top:80px;padding-bottom:80px;padding-left:24px;padding-right:24px">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"700px"}} -->
<div class="wp-block-group">

""" + h2("30 Dakika İçinde Kuryeniz Kapınızda Olsun!", color="#FFFFFF", align="center") + "\n\n" + spacer("20px") + "\n\n" + para("Hemen kuryenizi çağırın, kapıdan kapıya güvenli teslimatın keyfini sürün.", color="#94A3B8", size="18px", line_height="1.6", align="center") + "\n\n" + spacer("36px") + "\n\n" + buttons_two("Kurye Çağırın", "tel:+905322079609", "Hemen Bilgi Alın", "#iletisim", justify="center") + """

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# BÖLÜM 9: İLETİŞİM CTA
# ─────────────────────────────────────────────
contact_cta = """<!-- wp:group {"align":"full","style":{"color":{"background":"#0D59F2"},"spacing":{"padding":{"top":"60px","bottom":"60px","left":"24px","right":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#0D59F2;padding-top:60px;padding-bottom:60px;padding-left:24px;padding-right:24px">

<!-- wp:group {"layout":{"type":"constrained","contentSize":"1100px"}} -->
<div class="wp-block-group">

<!-- wp:columns {"isStackedOnMobile":true,"style":{"spacing":{"blockGap":{"left":"40px"}}}} -->
<div class="wp-block-columns is-stacked-on-mobile">

<!-- wp:column {"width":"70%","verticalAlignment":"center"} -->
<div class="wp-block-column" style="flex-basis:70%">

""" + h2("Teslimatlar İçin Doğru Adres: Aksoylar Kurye", color="#FFFFFF", size="28px") + "\n\n" + spacer("12px") + "\n\n" + para("Acil gönderileriniz için dakikalar içerisinde harekete geçiyoruz.", color="rgba(255,255,255,0.85)", size="16px") + """

</div>
<!-- /wp:column -->

<!-- wp:column {"width":"30%","verticalAlignment":"center"} -->
<div class="wp-block-column" style="flex-basis:30%">

""" + button_centered("Hemen İletişime Geçin", "tel:+905322079609", bg="#0A1F33", radius="6px") + """

</div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->"""

# ─────────────────────────────────────────────
# TÜM BLOKLAR BİRLEŞTİR
# ─────────────────────────────────────────────
all_blocks = "\n\n".join([
    hero,
    stats_section,
    services_section,
    about_section,
    extra_section,
    howto_section,
    benefits_section,
    final_cta,
    contact_cta,
])

page_data = {
    "title": "İstanbul Moto Kurye | Hızlı Kurye Hizmeti — Aksoylar Kurye",
    "status": "draft",
    "content": all_blocks,
    "template": "",
    "meta": {}
}

output_path = r"c:\Users\PC1\Desktop\claude-code-yeni\aksoylar-gutenberg-content.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(page_data, f, ensure_ascii=False, indent=2)

# Doğrulama
with open(output_path, "r", encoding="utf-8") as f:
    validated = json.load(f)

print("✓ JSON geçerli")
print(f"✓ content tipi: {type(validated['content']).__name__}")
print(f"✓ content uzunluğu: {len(validated['content'])} karakter")
print(f"✓ Dosya: {output_path}")
