"""  
    "qayerdan": "Davlat,Shahar,Viloyat", 
    "qayerga": "Davlatm,Shahar", 
    "davomiylik": 5,
    "vaqt" : "25.10.2025 22:25";
    "narxi":"1$,5$,100$,500$";
    "chipta_turi": "standart,business";
    "joylar_soni": "3,40,50";
    "transport_turi": "avtomobil,poyezd,samolyot:

"""
   
KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m" 

TOURLAR=[
    {'id':1,'qayerdan': 'Toshkent', 'qayerga': 'Samarqand', 'davomiylik': ' 1.5 ', 'vaqt': '20.10.2025 13:24', 'narxi': 200000, 'chipta_turi': 'standart', 'joylar_soni': '4', 'transport_turi': 'avtomobil'},
    {'id':2,'qayerdan': 'Toshkent', 'qayerga': 'Istanbul', 'davomiylik': '3', 'vaqt': '25.10.2025 22:25', 'narxi': 5000000, 'chipta_turi': 'Business', 'joylar_soni': '50', 'transport_turi': 'Samalyot'},
    {'id':3,'qayerdan': 'Toshkent', 'qayerga': 'Istanbul', 'davomiylik': '3', 'vaqt': '25.10.2025 22:25', 'narxi': 2000000, 'chipta_turi': 'Business', 'joylar_soni': '50', 'transport_turi': 'Samalyot'}
]


import json

JSON_FILE = "turlar.json"

# TOURLAR ro'yxatini JSON faylga saqlash
def saqlash_json():
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(TOURLAR, f, ensure_ascii=False, indent=4)
    print("Ma'lumotlar JSON faylga saqlandi!")
    
def yuklash_json():
    global TOURLAR
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            TOURLAR = json.load(f)
        print("Ma'lumotlar JSON fayldan yuklandi!")
    except FileNotFoundError:
        print("JSON fayl topilmadi, yangi fayl yaratiladi.")
        TOURLAR = []
def tour_qoshish():
    print("Tour qushish uchun malumotlarni Kiriting!!")
    qayerdan=input("Qayerdan:")
    qayerga=input("Qayerga:")
    davomiylik=input("Davomiylik:")
    vaqt=input("Vaqt:")
    narx=input("Narxi:")
    chipta_turi=input("Chipta turi:")
    joylar_soni=input("Joylar_soni:")
    transport_turi=input("Transport_turi:")
    id=len(TOURLAR)+1
    
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

    print("Qo'shildi")

def tour_uchirish():
    barcha_tour()
    a=int(input("qaysi tourni uchirmoqchisiz(idsini kiriting):"))

    for i in TOURLAR:
        if i["id"]==a:
            TOURLAR.pop(a-1)
            print(f"{a} idli tour uchirildi")
    
# Admin panel statistika funksiyas
def statistikani_korsatish():
     print(f"""
     Umumiy foydalanuvchilar soni: {len(users)}
     Umumiy buyurtmalar soni: {len(orders)}
     Umumiy daromad: {sum(order['amount'] for order in orders)}$
     """)
users = [
    {"id": 1, "name": "Alibek"},
    {"id": 2, "name": "Asilbek"},
    {"id": 3, "name": "Ozodbek"},
]

orders = [
    {"user_id": 1, "amount": 100},
    {"user_id": 2, "amount": 150},
    {"user_id": 1, "amount": 200},
    {"user_id": 3, "amount": 50},
]

def statistics(users, orders):
    total_users = len(users)
    total_orders = len(orders)
    total_income = sum(order["amount"] for order in orders)

    
    count = {}
    for order in orders:
        count[order["user_id"]] = count.get(order["user_id"], 0) + 1

    
    top_user_id = max(count, key=count.get)
    top_user_name = [user["name"] for user in users if user["id"] == top_user_id][0]

    return {
        "total_users": total_users,
        "total_orders": total_orders,
        "total_income": total_income,
        "top_user": top_user_name,
        "top_user_orders": count[top_user_id]
    }

print(statistics(users, orders))




def barcha_tour():
    for i in TOURLAR:
        print(f"""
        "id":{i["id"]},
        "qayerdan": {i["qayerdan"]}, 
        "qayerga": {i["qayerga"]}, 
        "davomiylik": {i["davomiylik"]},
        "vaqt" : {i["vaqt"]},
        "narxi": {i["narxi"]},
        "chipta_turi": {i["chipta_turi"]},
        "joylar_soni": {i["joylar_soni"]},
        "transport_turi": {i["transport_turi"]},
            """)
    print("Barchasi chiqdi!!1")
        
# login_user=[{
#     "login":"asilbek"
#     "parol":"1234"
#     },
#     {
#     "login":"asilbek"
#     "parol":"1234"
#     }
# ]
def admin_menu():
    login="asdfgh"
    parol="1234"
    l=input(f"{YASHIL}Login kiriting:{RANG}")
    par=input(f"{YASHIL}parol kiriting:{RANG}")

    if l!=login or par!=parol:
        print(f"{QIZIL}Notogri kiritdingiz!!!{RANG}")
        return 

    print("""
    ADMIN MENU
1-tour qo'shish
2-tour o'chirish
3-barcha tourlar
4-statistika
5-chiqish
""")
    a=input("Tanlang:")
    
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
        print("notogri kirtildi boshqa tanlang")
        admin_menu()
    
