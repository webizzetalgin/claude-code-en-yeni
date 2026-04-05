import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

# ─────────────────────────────────────────────
# TASARIM TOKEN'LARI — Medicora Paleti
# ─────────────────────────────────────────────
PRIMARY    = "#0D59F2"   # Medicora mavi
DARK       = "#0A1F33"   # Lacivert (koyu bölüm bg)
LIGHT_BG   = "#F0F5FF"   # Açık mavi-gri bg
WHITE      = "#FFFFFF"
TEXT_MAIN  = "#0A1F33"
TEXT_BODY  = "#5A6A7A"
TEXT_MUTED = "#94A3B8"
FONT_HEAD  = "Inter Tight"
FONT_BODY  = "Inter"

# ID üretici
_id_counter = [1000]
def uid(prefix=""):
    _id_counter[0] += 1
    return f"{prefix}{_id_counter[0]:04x}"

# ─────────────────────────────────────────────
# WIDGET YARDIMCILAR
# ─────────────────────────────────────────────

def spacer(px):
    return {"id": uid("sp"), "elType": "widget", "widgetType": "spacer",
            "settings": {"space": {"unit": "px", "size": px}}, "elements": []}

def heading(text, tag="h2", color=TEXT_MAIN, size=36, size_m=26, weight="700", line_h=1.2, align="left"):
    return {
        "id": uid("hd"), "elType": "widget", "widgetType": "heading",
        "settings": {
            "title": text,
            "header_size": tag,
            "align": align,
            "title_color": color,
            "typography_typography": "custom",
            "typography_font_family": FONT_HEAD,
            "typography_font_size": {"unit": "px", "size": size},
            "typography_font_size_tablet": {"unit": "px", "size": int(size * 0.8)},
            "typography_font_size_mobile": {"unit": "px", "size": size_m},
            "typography_font_weight": weight,
            "typography_line_height": {"unit": "em", "size": line_h}
        },
        "elements": []
    }

def text_editor(html, color=TEXT_BODY, size=16, size_m=15, weight="400", line_h=1.75):
    return {
        "id": uid("tx"), "elType": "widget", "widgetType": "text-editor",
        "settings": {
            "editor": html,
            "text_color": color,
            "typography_typography": "custom",
            "typography_font_family": FONT_BODY,
            "typography_font_size": {"unit": "px", "size": size},
            "typography_font_size_mobile": {"unit": "px", "size": size_m},
            "typography_font_weight": weight,
            "typography_line_height": {"unit": "em", "size": line_h}
        },
        "elements": []
    }

def badge_widget(text, dark=False):
    bg    = "rgba(255,255,255,0.12)" if dark else "#E8F0FE"
    color = WHITE if dark else PRIMARY
    html  = (f'<p style="margin:0;">'
             f'<span style="display:inline-block;background:{bg};color:{color};'
             f'font-family:{FONT_BODY};font-size:11px;font-weight:600;'
             f'letter-spacing:1.4px;text-transform:uppercase;'
             f'padding:5px 12px;border-radius:4px;">{text}</span></p>')
    return text_editor(html, color=color, size=11, weight="600")

def button_widget(text, url="#", bg=PRIMARY, txt_color=WHITE, rounded=False):
    radius_px = 50 if rounded else 6
    return {
        "id": uid("bt"), "elType": "widget", "widgetType": "button",
        "settings": {
            "text": text,
            "link": {"url": url, "is_external": False, "nofollow": False},
            "align": "left",
            "size": "lg",
            "background_color": bg,
            "button_text_color": txt_color,
            "border_radius": {"unit": "px", "top": str(radius_px), "right": str(radius_px),
                              "bottom": str(radius_px), "left": str(radius_px), "isLinked": True},
            "typography_typography": "custom",
            "typography_font_family": FONT_BODY,
            "typography_font_size": {"unit": "px", "size": 15},
            "typography_font_weight": "600",
            "button_hover_background_color": "#0946C5",
            "button_hover_color": WHITE
        },
        "elements": []
    }

def button_outline(text, url="#"):
    return {
        "id": uid("bo"), "elType": "widget", "widgetType": "button",
        "settings": {
            "text": text,
            "link": {"url": url, "is_external": False, "nofollow": False},
            "align": "left",
            "size": "lg",
            "background_color": "rgba(0,0,0,0)",
            "button_text_color": WHITE,
            "border_border": "solid",
            "border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
            "border_color": "rgba(255,255,255,0.35)",
            "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True},
            "typography_typography": "custom",
            "typography_font_family": FONT_BODY,
            "typography_font_size": {"unit": "px", "size": 15},
            "typography_font_weight": "600",
            "button_hover_background_color": "rgba(255,255,255,0.10)",
            "button_hover_color": WHITE
        },
        "elements": []
    }

def icon_box(icon, title, desc, icon_color=PRIMARY, title_color=TEXT_MAIN, desc_color=TEXT_BODY):
    return {
        "id": uid("ib"), "elType": "widget", "widgetType": "icon-box",
        "settings": {
            "selected_icon": {"value": icon, "library": "fa-solid"},
            "title_text": title,
            "description_text": desc,
            "icon_color": icon_color,
            "title_color": title_color,
            "description_color": desc_color,
            "icon_size": {"unit": "px", "size": 28},
            "title_size": "h3",
            "title_typography_typography": "custom",
            "title_typography_font_family": FONT_HEAD,
            "title_typography_font_size": {"unit": "px", "size": 18},
            "title_typography_font_weight": "700",
            "title_typography_line_height": {"unit": "em", "size": 1.25},
            "description_typography_typography": "custom",
            "description_typography_font_family": FONT_BODY,
            "description_typography_font_size": {"unit": "px", "size": 14},
            "description_typography_line_height": {"unit": "em", "size": 1.65},
            "position": "top"
        },
        "elements": []
    }

def stat_icon_box(number, title, icon, dark=False):
    tc  = WHITE if dark else TEXT_MAIN
    dtc = "rgba(255,255,255,0.72)" if dark else TEXT_BODY
    ic  = WHITE if dark else PRIMARY
    return {
        "id": uid("si"), "elType": "widget", "widgetType": "icon-box",
        "settings": {
            "selected_icon": {"value": icon, "library": "fa-solid"},
            "title_text": number,
            "description_text": title,
            "icon_color": ic,
            "title_color": tc,
            "description_color": dtc,
            "icon_size": {"unit": "px", "size": 32},
            "title_size": "h3",
            "title_typography_typography": "custom",
            "title_typography_font_family": FONT_HEAD,
            "title_typography_font_size": {"unit": "px", "size": 32},
            "title_typography_font_weight": "700",
            "title_typography_line_height": {"unit": "em", "size": 1.05},
            "description_typography_typography": "custom",
            "description_typography_font_family": FONT_BODY,
            "description_typography_font_size": {"unit": "px", "size": 14},
            "position": "left"
        },
        "elements": []
    }

# ─────────────────────────────────────────────
# SECTION (BÖLÜM) YARDIMCISI
# ─────────────────────────────────────────────

def section(columns, bg=WHITE, pad_v=80, pad_h=32, max_w=1200, gap="no"):
    return {
        "id": uid("sc"),
        "elType": "section",
        "settings": {
            "layout": "full_width",
            "content_width": {"size": max_w, "unit": "px"},
            "gap": gap,
            "padding": {"unit": "px", "top": str(pad_v), "right": str(pad_h),
                        "bottom": str(pad_v), "left": str(pad_h), "isLinked": False},
            "padding_tablet": {"unit": "px", "top": str(int(pad_v * 0.75)), "right": "24",
                               "bottom": str(int(pad_v * 0.75)), "left": "24", "isLinked": False},
            "padding_mobile": {"unit": "px", "top": str(int(pad_v * 0.6)), "right": "18",
                               "bottom": str(int(pad_v * 0.6)), "left": "18", "isLinked": False},
            "background_background": "classic",
            "background_color": bg
        },
        "elements": columns,
        "isInner": False
    }

def col(widgets, size=100, size_t=100, size_m=100,
        pad=None, bg=None, border_right=False, valign="top"):
    settings = {
        "_column_size": size,
        "_inline_size": size,
        "_inline_size_tablet": size_t,
        "_inline_size_mobile": size_m,
        "vertical_align": valign
    }
    if pad:
        settings["padding"] = {"unit": "px", "top": str(pad[0]), "right": str(pad[1]),
                                "bottom": str(pad[2]), "left": str(pad[3]), "isLinked": False}
    if bg:
        settings["background_background"] = "classic"
        settings["background_color"] = bg
    if border_right:
        settings["border_border"] = "solid"
        settings["border_width"] = {"unit": "px", "top": "0", "right": "1", "bottom": "0", "left": "0", "isLinked": False}
        settings["border_color"] = "rgba(0,0,0,0.08)"
    return {"id": uid("cl"), "elType": "column", "settings": settings,
            "elements": widgets, "isInner": False}

# ─────────────────────────────────────────────
# BÖLÜM 1: HERO
# ─────────────────────────────────────────────
hero_left = col([
    badge_widget("İSTANBUL MOTO KURYE"),
    spacer(16),
    heading("Aksoylar Kurye İle Zamanında Teslimat Avantajı",
            tag="h1", color=WHITE, size=54, size_m=34, weight="700", line_h=1.12),
    spacer(20),
    text_editor(
        "<p>İstanbul moto kurye firması olarak acil iletilmesi gereken gönderilere "
        "ivedilikle karşılık veriyoruz. Şehrin her noktasına hızlı ve güvenilir teslimat hizmetindeyiz.</p>",
        color="rgba(255,255,255,0.72)", size=17, size_m=15
    ),
    spacer(36),
    button_widget("Kurye Çağır", url="tel:+905322079609", bg=PRIMARY),
    spacer(12),
    button_outline("Hizmetlerimizi Keşfet", url="#hizmetler"),
], size=55, size_t=100, size_m=100,
   pad=(0, 40, 0, 0), valign="middle")

hero_right = col([
    {
        "id": uid("im"), "elType": "widget", "widgetType": "image",
        "settings": {
            "image": {
                "url": "https://placehold.co/620x440/0A1F33/0D59F2?text=Aksoylar+Kurye",
                "alt": "İstanbul moto kurye hizmetleri"
            },
            "image_size": "full",
            "align": "center",
            "border_radius": {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
        },
        "elements": []
    }
], size=45, size_t=100, size_m=100,
   pad=(0, 0, 0, 0), valign="middle")

hero_section = section(
    [hero_left, hero_right],
    bg=DARK, pad_v=110, pad_h=32
)

# ─────────────────────────────────────────────
# BÖLÜM 2: İSTATİSTİK BANDI
# ─────────────────────────────────────────────
stat_cols = []
stats = [
    ("%99", "Hızlı Kurye Desteği",       "fas fa-bolt"),
    ("30 dk", "Kapıdan Kapıya Teslimat", "fas fa-clock"),
    ("7/24", "Kesintisiz Hizmet",        "fas fa-headset"),
    ("✓",   "Profesyonel Kadro",         "fas fa-user-check"),
]
for i, (num, lbl, icon) in enumerate(stats):
    border = (i < len(stats) - 1)
    stat_cols.append(col(
        [stat_icon_box(num, lbl, icon, dark=False)],
        size=25, size_t=50, size_m=100,
        pad=(32, 36, 32, 24),
        border_right=border
    ))

stats_section = section(stat_cols, bg=LIGHT_BG, pad_v=0, pad_h=32, gap="no")

# ─────────────────────────────────────────────
# BÖLÜM 3: HİZMETLER BAŞLIK
# ─────────────────────────────────────────────
services_header_section = section(
    [col([
        badge_widget("HİZMETLERİMİZ"),
        spacer(14),
        heading("Aksoylar Kurye Hizmetlerimizle Tanışın", tag="h2",
                color=TEXT_MAIN, size=38, weight="700"),
        spacer(10),
        text_editor("<p>Sunmuş olduğumuz hizmet seçeneklerimizle tanışın.</p>",
                    color=TEXT_BODY, size=16),
        spacer(20),
        button_widget("Hizmetlerimiz Sayfasını Görüntüle", url="/hizmetlerimiz", bg=DARK),
    ], size=100, pad=(0, 0, 0, 0))],
    bg=WHITE, pad_v=72, pad_h=32
)

# ─────────────────────────────────────────────
# BÖLÜM 4: HİZMET KARTLARI (4 kart)
# ─────────────────────────────────────────────
def service_col(label, title, desc, icon):
    return col([
        icon_box(icon, title, desc,
                 icon_color=PRIMARY, title_color=TEXT_MAIN, desc_color=TEXT_BODY),
        spacer(18),
        text_editor(
            f'<p style="margin:0;"><span style="color:{PRIMARY};font-weight:600;font-size:13px;">'
            f'<strong>{label}</strong></span></p>',
            color=PRIMARY, size=13, weight="600"
        ),
        spacer(12),
        text_editor(
            f'<p style="margin:0;"><a href="#" style="color:{PRIMARY};font-size:14px;font-weight:600;'
            f'text-decoration:none;">→ İncele</a></p>',
            color=PRIMARY, size=14
        ),
    ], size=25, size_t=50, size_m=100, pad=(30, 24, 30, 24))

service_cards_section = {
    "id": uid("sc"),
    "elType": "section",
    "settings": {
        "layout": "full_width",
        "content_width": {"size": 1200, "unit": "px"},
        "gap": "no",
        "padding": {"unit": "px", "top": "0", "right": "32", "bottom": "72", "left": "32", "isLinked": False},
        "background_background": "classic",
        "background_color": WHITE,
        "border_border": "solid",
        "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
        "border_color": "#E2E8F0"
    },
    "elements": [
        service_col("Gün içi teslimat", "Moto Kurye",
                    "Evrakların, paketlerin, hediyelik ürünlerin ve benzeri eşyaların gün içinde teslimatının yapıldığı hizmettir.",
                    "fas fa-motorcycle"),
        service_col("Hızlı teslimat çözümü", "Acil Kurye",
                    "Acil olan tüm teslimat işleri için en iyi çözüm. Gönderiler en kısa sürede ulaştırılmaktadır.",
                    "fas fa-bolt"),
        service_col("Güvenilir taşıma", "Araçlı Kurye",
                    "Büyük ebatlı ya da hassas gönderilerin taşınması için tercih edilen geniş zamanlı, ekonomik fiyatlı hizmettir.",
                    "fas fa-car"),
        service_col("Geniş hizmet kapsamı", "Şehirler Arası Kurye",
                    "Acil ya da planlı olarak farklı şehirlere gerçekleştirilecek teslimatlar için kullanılan hizmettir.",
                    "fas fa-road"),
    ],
    "isInner": False
}

# ─────────────────────────────────────────────
# BÖLÜM 5: HAKKIMIZDA (2 sütun)
# ─────────────────────────────────────────────
about_left = col([
    badge_widget("HAKKIMIZDA"),
    spacer(16),
    heading("İstanbul Moto Kurye Olarak Hızlı Teslimatlarda Yanınızdayız!",
            tag="h2", color=TEXT_MAIN, size=36, weight="700", line_h=1.2),
    spacer(20),
    text_editor(
        "<p>İstanbul motor kurye hizmetlerimiz sayesinde gönderileri hızlı ve güvenli bir şekilde "
        "varış noktasına ulaştırıyoruz. İstanbul'da gönderilerin araba ile teslimatın yapılması her zaman "
        "kolay olamayabiliyor. Bu nedenle hızlı kurye firması olarak bizler devreye giriyoruz.</p>",
        color=TEXT_BODY, size=16
    ),
    spacer(16),
    text_editor(
        "<p>Gönderileri ivedi bir şekilde alıcı adresinden alıyor ve kısa süre içerisinde varış "
        "noktasına ulaştırıyoruz. İstanbul kurye olarak sunduğumuz bu çözümlerle, fabrikaların, "
        "işletmelerin ve bireylerin günlük iş akışını aksatmamalarını sağlıyoruz.</p>",
        color=TEXT_BODY, size=16
    ),
    spacer(16),
    text_editor(
        "<p>İster acil bir evrak gönderiniz, isterseniz de önemli bir paket teslimatınız olsun, "
        "tüm gönderiler için her zaman yanınızda oluyoruz. Gönderilerin güvenliğini sağlamak adına "
        "ise her kuryeyi, uzman kadromuz ile birlikte eğitiyoruz.</p>",
        color=TEXT_BODY, size=16
    ),
    spacer(32),
    button_widget("Hizmetlerimizi Keşfedin", url="/hizmetlerimiz", bg=PRIMARY),
], size=55, size_t=100, size_m=100, pad=(0, 48, 0, 0), valign="middle")

about_right = col([
    icon_box("fas fa-map-marker-alt", "İstanbul'un Her Noktasına",
             "Şehrin tüm ilçelerine hızlı ve güvenli teslimat yapıyoruz.",
             icon_color=PRIMARY),
    spacer(24),
    icon_box("fas fa-shield-alt", "Güvenli Teslimat Garantisi",
             "Her kurye uzman kadromuzla eğitilmiş, gönderileriniz güvende.",
             icon_color=PRIMARY),
    spacer(24),
    icon_box("fas fa-wallet", "Uygun Fiyat Politikası",
             "Boyut, ağırlık ve mesafeye göre şeffaf ve rekabetçi fiyatlandırma.",
             icon_color=PRIMARY),
], size=45, size_t=100, size_m=100, pad=(0, 0, 0, 24), valign="middle")

about_section = section([about_left, about_right], bg=LIGHT_BG, pad_v=80, pad_h=32)

# ─────────────────────────────────────────────
# BÖLÜM 6: EKSTRA HİZMETLER (koyu bg)
# ─────────────────────────────────────────────
extra_header = col([
    badge_widget("EKSTRA HİZMETLER", dark=True),
    spacer(16),
    heading("Ekstra Hizmet Verdiğimiz Alanlar",
            tag="h2", color=WHITE, size=38, weight="700"),
    spacer(10),
    text_editor(
        "<p>Vermiş olduğumuz hizmetlerin yanında ekstra olarak hizmet verdiğimiz alanlar şu şekildedir:</p>",
        color="rgba(255,255,255,0.65)", size=16
    ),
], size=100, pad=(0, 0, 32, 0))

extra_items = [
    ("fas fa-car",            "Vale & Şoför / Araç Muayene",
     "Vale, şoför ve araç muayene hizmetleri sunarak hayatınızı daha kolay hale getiriyoruz."),
    ("fas fa-shopping-basket","Mağaza ve Market Alışverişi",
     "Kurye kadromuz ile mağaza ve market alışverişlerinizde istekleriniz için yardımcı oluyoruz."),
    ("fas fa-truck-moving",   "Ev Nakliyesi (Büyük Araç)",
     "Ev nakliyesi gibi durumlarda büyük araç ile nakliye sorunlarına uygun fiyatlarla çözüm getiriyoruz."),
    ("fas fa-boxes",          "Toplu Dağıtım Günlük Kurye",
     "Toplu dağıtım kuryelerimizle tüm ürünlerin gün içinde dağıtılmasını sağlıyoruz."),
    ("fas fa-truck-pickup",   "7/24 Çekici Hizmetleri",
     "7/24 çekici hizmeti sunarak yolda kaldığınız durumlarda hızlı şekilde destek sağlıyoruz."),
]

extra_row1 = []
extra_row2 = []
for i, (icon, title, desc) in enumerate(extra_items):
    c = col([
        icon_box(icon, title, desc,
                 icon_color="rgba(255,255,255,0.80)",
                 title_color=WHITE,
                 desc_color="rgba(255,255,255,0.60)"),
    ], size=20 if i < 3 else 25, size_t=50, size_m=100, pad=(24, 20, 24, 20))
    if i < 3:
        extra_row1.append(c)
    else:
        extra_row2.append(c)

# Dummy 3. sütun for row2 balance
extra_row2.append(col([], size=25, size_t=50, size_m=100))
extra_row2.append(col([], size=25, size_t=50, size_m=100))

extra_header_section = section([extra_header], bg=DARK, pad_v=72, pad_h=32)
extra_row1_section   = section(extra_row1, bg=DARK, pad_v=0, pad_h=32, gap="no")
extra_row2_section   = section(extra_row2, bg=DARK, pad_v=0, pad_h=32, gap="no")
extra_bottom_pad     = section([col([], size=100)], bg=DARK, pad_v=40, pad_h=0, gap="no")

# ─────────────────────────────────────────────
# BÖLÜM 7: ACİL KURYE NASIL ALINIR
# ─────────────────────────────────────────────
howto_left = col([
    badge_widget("SÜRECİ ÖĞRENIN"),
    spacer(16),
    heading("Acil Kurye Hizmeti Almak İçin Ne Yapmak Gerekiyor?",
            tag="h2", color=TEXT_MAIN, size=36, weight="700", line_h=1.2),
    spacer(20),
    text_editor(
        "<p>Acil kurye hizmetlerimizden yararlanma süreci oldukça basittir. Öncelik olarak "
        "gönderinizin boyutunu ve teslimat noktalarını belirtmeniz yeterlidir. Bu bilgiler "
        "tarafımıza ulaştıktan sonra sizlere en yakın kuryeyi yönlendirecek ve gönderilerinizi "
        "en kısa sürede teslim aldırtacağız.</p>",
        color=TEXT_BODY, size=16
    ),
    spacer(16),
    text_editor(
        "<p>Hızlı kurye hizmetlerimizi toplantıya yetişmesi gereken evraklarda, yedek parçalarda, "
        "unutulan doğum günü hediyelerinde ve daha birçok alanda kullanabilirsiniz. İstanbul moto "
        "kurye kadromuz şehrin her tarafını bilen uzman kişilerden oluştuğu için teslimat süresi "
        "minimuma inecektir.</p>",
        color=TEXT_BODY, size=16
    ),
    spacer(16),
    text_editor(
        "<p>İstanbul moto kurye fiyatları politikamız ise taşınacak gönderinin boyutuna, ağırlığına "
        "ve mesafeye göre değişkenlik göstermektedir. Ancak her zaman uygun fiyatlı hizmet vermeye "
        "özen gösteriyoruz.</p>",
        color=TEXT_BODY, size=16
    ),
    spacer(32),
    button_widget("Hizmet Alın", url="tel:+905322079609", bg=PRIMARY),
], size=55, size_t=100, size_m=100, pad=(0, 48, 0, 0), valign="middle")

def step_item(num, title, desc):
    html = (f'<div style="display:flex;gap:16px;align-items:flex-start;margin-bottom:20px;">'
            f'<span style="min-width:36px;height:36px;background:{PRIMARY};color:#fff;'
            f'font-family:{FONT_HEAD};font-size:16px;font-weight:700;border-radius:6px;'
            f'display:flex;align-items:center;justify-content:center;">{num}</span>'
            f'<div><p style="margin:0 0 4px;font-family:{FONT_HEAD};font-size:16px;font-weight:700;color:{TEXT_MAIN};">{title}</p>'
            f'<p style="margin:0;font-family:{FONT_BODY};font-size:14px;color:{TEXT_BODY};line-height:1.6;">{desc}</p></div>'
            f'</div>')
    return text_editor(html, color=TEXT_MAIN, size=15)

howto_right = col([
    heading("3 Adımda Kurye Çağırın", tag="h3", color=TEXT_MAIN, size=22, weight="700"),
    spacer(24),
    step_item("1", "Bize Ulaşın", "Telefon veya WhatsApp ile iletişime geçin."),
    step_item("2", "Gönderinizi Bildirin", "Boyut, ağırlık ve teslimat noktasını iletin."),
    step_item("3", "Kuryeniz Yola Çıksın", "En yakın kurye gönderinizi teslim alır."),
], size=45, size_t=100, size_m=100, pad=(40, 40, 40, 40),
   bg=LIGHT_BG, valign="middle")

howto_section = section([howto_left, howto_right], bg=WHITE, pad_v=80, pad_h=32)

# ─────────────────────────────────────────────
# BÖLÜM 8: NELER KAZANACAKSINIZ
# ─────────────────────────────────────────────
benefits_header = col([
    badge_widget("AVANTAJLAR"),
    spacer(14),
    heading("Neler Kazanacaksınız?", tag="h2", color=TEXT_MAIN, size=38, weight="700"),
], size=100, pad=(0, 0, 36, 0))

def benefit_col(icon, title, desc):
    return col([
        icon_box(icon, title, desc, icon_color=PRIMARY,
                 title_color=TEXT_MAIN, desc_color=TEXT_BODY),
    ], size=33, size_t=50, size_m=100, pad=(32, 28, 32, 28))

benefits_cards_section = section(
    [
        benefits_header,
        benefit_col("fas fa-bolt", "Acil Hizmet İçin En İyi Çözüm",
                    "Acil gönderileriniz için öncelikli ve hızlı teslimat imkanı sunarak en iyi çözümleri sunuyoruz."),
        benefit_col("fas fa-users", "Uzman Kadro İle Çalışma Avantajı",
                    "Firmamız bünyesinde uzman kadroyu bulundurarak müşterilerimizin en iyi hizmetlerimizden yararlanmalarını sağlıyoruz."),
        benefit_col("fas fa-star", "Özel Teslimat Kolaylığı",
                    "Özel teslimat kolaylığı sayesinde herkes kişiye özel kurye hizmetine sahip oldu."),
    ],
    bg=LIGHT_BG, pad_v=72, pad_h=32, gap="no"
)

# ─────────────────────────────────────────────
# BÖLÜM 9: FİNAL CTA
# ─────────────────────────────────────────────
cta_section = section(
    [col([
        heading("30 Dakika İçinde Kuryeniz Kapınızda Olsun!",
                tag="h2", color=WHITE, size=40, size_m=28, weight="700", align="center"),
        spacer(18),
        text_editor(
            "<p style='text-align:center;'>Hemen kuryenizi çağırın, "
            "kapıdan kapıya güvenli teslimatın keyfini sürün.</p>",
            color="rgba(255,255,255,0.75)", size=18
        ),
        spacer(36),
        {
            "id": uid("tb"),
            "elType": "widget",
            "widgetType": "button",
            "settings": {
                "text": "Kurye Çağırın",
                "link": {"url": "tel:+905322079609", "is_external": False},
                "align": "center",
                "size": "xl",
                "background_color": PRIMARY,
                "button_text_color": WHITE,
                "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True},
                "typography_typography": "custom",
                "typography_font_family": FONT_BODY,
                "typography_font_size": {"unit": "px", "size": 17},
                "typography_font_weight": "700",
                "button_hover_background_color": "#0946C5"
            },
            "elements": []
        },
    ], size=100, pad=(0, 100, 0, 100))],
    bg=DARK, pad_v=80, pad_h=32
)

# ─────────────────────────────────────────────
# BÖLÜM 10: İLETİŞİM CTA BANDI
# ─────────────────────────────────────────────
contact_left = col([
    heading("Teslimatlar İçin Doğru Adres: Aksoylar Kurye",
            tag="h2", color=WHITE, size=28, weight="700", line_h=1.25),
    spacer(10),
    text_editor("<p>Acil gönderileriniz için dakikalar içerisinde harekete geçiyoruz.</p>",
                color="rgba(255,255,255,0.80)", size=16),
], size=70, size_t=100, size_m=100, valign="middle")

contact_right = col([
    {
        "id": uid("bt"),
        "elType": "widget",
        "widgetType": "button",
        "settings": {
            "text": "Hemen İletişime Geçin",
            "link": {"url": "tel:+905322079609", "is_external": False},
            "align": "right",
            "align_tablet": "left",
            "size": "lg",
            "background_color": DARK,
            "button_text_color": WHITE,
            "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True},
            "typography_typography": "custom",
            "typography_font_family": FONT_BODY,
            "typography_font_size": {"unit": "px", "size": 15},
            "typography_font_weight": "700",
            "button_hover_background_color": "#0A1520"
        },
        "elements": []
    }
], size=30, size_t=100, size_m=100, valign="middle")

contact_section = section([contact_left, contact_right], bg=PRIMARY, pad_v=50, pad_h=32)

# ─────────────────────────────────────────────
# JSON ÇIKTISI
# ─────────────────────────────────────────────
page = {
    "title": "Aksoylar Kurye — Ana Sayfa (Medicora Teması)",
    "type": "page",
    "version": "0.4",
    "page_settings": {
        "hide_title": "yes",
        "template": "elementor_canvas"
    },
    "content": [
        hero_section,
        stats_section,
        services_header_section,
        service_cards_section,
        about_section,
        extra_header_section,
        extra_row1_section,
        extra_row2_section,
        extra_bottom_pad,
        howto_section,
        benefits_cards_section,
        cta_section,
        contact_section,
    ]
}

output_path = r"c:\Users\PC1\Desktop\claude-code-yeni\aksoylar-kurye-medicora.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(page, f, ensure_ascii=False, indent=2)

# Doğrulama
with open(output_path, "r", encoding="utf-8") as f:
    validated = json.load(f)

print("JSON gecerli")
print(f"Bolum sayisi: {len(validated['content'])}")
print(f"Dosya: {output_path}")
total_size = len(json.dumps(validated, ensure_ascii=False))
print(f"Dosya boyutu: {total_size // 1024} KB")
