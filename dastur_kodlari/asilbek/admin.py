KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m" 

TOURLAR=[
    {'id':1,'qayerdan': 'Toshkent', 'qayerga': 'Samarqand', 'davomiylik': ' 1.5 ', 'vaqt': '20.10.2025 13:24', 'narxi': 200000, 'chipta_turi': 'standart', 'joylar_soni': '4', 'transport_turi': 'avtomobil'},
    {'id':2,'qayerdan': 'Toshkent', 'qayerga': 'Istanbul', 'davomiylik': '3', 'vaqt': '25.10.2025 22:25', 'narxi': 5000000, 'chipta_turi': 'Business', 'joylar_soni': '50', 'transport_turi': 'Samalyot'},
    {'id':3,'qayerdan': 'Toshkent', 'qayerga': 'Istanbul', 'davomiylik': '3', 'vaqt': '25.10.2025 22:25', 'narxi': 2000000, 'chipta_turi': 'Business', 'joylar_soni': '50', 'transport_turi': 'Samalyot'}
]

def tour_qoshish():
    print(f"{KOK}Tour qushish uchun malumotlarni Kiriting!!{RANG}")
    qayerdan=input(f"{YASHIL}Qayerdan:{RANG}")
    qayerga=input(f"{YASHIL}Qayerga:{RANG}")
    davomiylik=input(f"{YASHIL}Davomiylik:{RANG}")
    vaqt=input(f"{YASHIL}Vaqt:{RANG}")
    narx=input(f"{YASHIL}Narxi:{RANG}")
    chipta_turi=input(f"{YASHIL}Chipta turi:{RANG}")
    joylar_soni=input(f"{YASHIL}Joylar soni:{RANG}")
    transport_turi=input(f"{YASHIL}Transport turi:{RANG}")
    id=len(TOURLAR)+1
    if not (qayerdan and qayerga and davomiylik and vaqt and narx and chipta_turi and joylar_soni and transport_turi):
        print(f"{QIZIL}Barcha malumotlarni kiriting!!!{RANG}")
        return
    
    TOURLAR.append({
        "id":id,
        "qayerdan": qayerdan, 
        "qayerga": qayerga, 
        "davomiylik": davomiylik,
        "vaqt" : vaqt,
        "narxi": narx,
        "chipta_turi": chipta_turi,
        "joylar_soni": joylar_soni,
        "transport_turi": transport_turi,
    })

    print(f"{KOK}Qo'shildi{RANG}")

def tour_uchirish():
    barcha_tour()
    a=int(input(f"{YASHIL}qaysi tourni uchirmoqchisiz(idsini kiriting):{RANG}"))

    for i in TOURLAR:
        if i["id"]==a:
            TOURLAR.pop(a-1)
            print(f"{KOK}{a} idli tour uchirildi{RANG}")
    

def statistikani_korsatish():
    from dastur_kodlari.alibek.foydalanuvchi import USER

    umumiy_user = len(USER)
    umumiy_balans = sum(int(i.get("balans", 0)) for i in USER if i.get("balans"))
    umumiy_orders = len(TOURLAR)
    umumiy_daromad = sum(int(i["narxi"]) for i in TOURLAR)

    print(f"""{KOK}
                STATISTIKA:
        Umumiy foydalanuvchilar soni: {umumiy_user}
        Umumiy balans: {umumiy_balans} so'm
        Umumiy tourlar soni: {umumiy_orders}
        Umumiy daromad:  {umumiy_daromad} so'm
    {RANG}
    """)



def barcha_tour():
    for i in TOURLAR:
        print(f"""{KOK}
        -------------------------
        🆔 ID: {i["id"]}
        📍 Qayerdan: {i["qayerdan"]}
        🎯 Qayerga: {i["qayerga"]}
        ⏳ Davomiylik: {i["davomiylik"]}
        🕒 Vaqt: {i["vaqt"]}
        💰 Narxi: {i["narxi"]}
        🎫 Chipta turi: {i["chipta_turi"]}
        🪑 Joylar soni: {i["joylar_soni"]}
        🚍 Transport turi: {i["transport_turi"]}
        -------------------------{RANG}
        """)

    print(f"{KOK}Barchasi chiqdi!!1{RANG}")
    
def admin_menu():
    login="asdfgh"
    parol="1234"
    l=input(f"{YASHIL}Login kiriting:{RANG}")
    par=input(f"{YASHIL}parol kiriting:{RANG}")

    if l!=login or par!=parol:
        print(f"{QIZIL}Notogri kiritdingiz!!!{RANG}")
        return 
    while True:
        print(f"""{KOK}
        ADMIN MENU
    1-tour qo'shish
    2-tour o'chirish
    3-barcha tourlar
    4-statistika{QIZIL}
    5-chiqish{RANG}
    """)
        a=input(f"{YASHIL}Tanlang:{RANG}")
        
        if a=="1":
            tour_qoshish()
        
        elif a=="2":
            tour_uchirish()

        elif a=="3":
            barcha_tour()

        elif a=="4":
            statistikani_korsatish()

        elif a=="5":
            return 
        else:
            print(f"{QIZIL}noto'g'ri kiritildi boshqa tanlang{RANG}")
            admin_menu()
        
