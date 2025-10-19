

from dastur_kodlari.latofat.admin import barcha_tour,TOURLAR

users = []  # Barcha foydalanuvchilar saqlanadi
current_user = None  # Hozir tizimga kirgan foydalanuvchi


def register():
    login = input("Yangi login kiriting: ")
    password = input("Parol kiriting: ")

    # Login takrorlanmasligini tekshiramiz
    for user in users:
        if user["login"] == login:
            print(" Bu login allaqachon mavjud!")
            return

    # Yangi foydalanuvchini yaratamiz (balans 0)
    users.append({"login": login, "password": password, "balance": 0})
    print(" Ro‘yxatdan o‘tish muvaffaqiyatli!")


def login_user():
    global current_user
    login = input("Loginni kiriting: ")
    password = input("Parolni kiriting: ")

    for user in users:
        if user["login"] == login and user["password"] == password:
            current_user = user
            print(f" Xush kelibsiz, {login}!")
            return
    print(" Login yoki parol xato!")


def show_balance():
    if current_user:
        print(f" Sizning balansingiz: {current_user['balance']} so‘m")
    else:
        print(" Avval tizimga kiring!")


def add_balance():
    if current_user:
        amount = int(input(" Necha so‘m qo‘shmoqchisiz: "))
        current_user["balance"] += amount
        print(f" Hisobingiz to‘ldirildi! Yangi balans: {current_user['balance']} so‘m")
    else:
        print(" Avval tizimga kiring!")


def buy_ticket():
    if current_user:
        price = int(input(" Chipta narxi (so‘mda): "))
        if current_user["balance"] >= price:
            current_user["balance"] -= price
            print(f" Chipta sotib olindi! Qolgan balans: {current_user['balance']} so‘m")
        else:
            print(" Balans yetarli emas!")
    else:
        print(" Avval tizimga kiring!")

def shaxsiy_kabinet():
    while True:
        print("\n--- TUR AGENT TIZIMI ---")
        print("1. Ro‘yxatdan o‘tish")
        print("2. Tizimga kirish")
        print("3. Balansni ko‘rish")
        print("4. Balansga pul qo‘shish")
        print("5. Chipta sotib olish")
        print("6. Chiqish")
        tanlov = input("Tanlovni kiriting: ")

        if tanlov == "1":
            register()
        elif tanlov == "2":
            login_user()
        elif tanlov == "3":
            show_balance()
        elif tanlov == "4":
            add_balance()
        elif tanlov == "5":
            buy_ticket()
        elif tanlov == "6":
            print(" Dasturdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov!")



def uxshash(qayerdan1,qayerdan2):
    """Toshkent,Tashkent"""
    qayerdan1=qayerdan1.lower()#toshkent
    qayerdan2=qayerdan2.lower()#tashkent
    t=0
    for i in range(8):#range(8)==[0,1,2,3,4,5,6,7]
        if qayerdan1[i]==qayerdan2[i]:
            t+=1

    if qayerdan1==qayerdan2 or t>=5:
        return True
    else:
        return False
    
    



def tour_qidirish():
    print("""Qidirish""")
    qayerdan=input("qayerdan bormoqchisiz?:")
    qayerga=input("qayerga bormoqchisiz?:")
    qachon=input("Qachon bormoqchisiz?:")
    for i in TOURLAR:
        if uxshash(i["qayerdan"],qayerdan) and uxshash(i["qayerga"],qayerga) and i["vaqt"][:-6]==qachon:
            print("Topildi!!")
            print(f"""
            "id":{i["id"]},
            "qayerdan": {i["qayerdan"]}, 
            "qayerga": {i["qayerga"]}, 
            "davomiylik": {i["davomiylik"]},
            "vaqt" : {i["vaqt"]},
            "narxi": {i["narxi"]},
            "chipta_turi": {i["chipta_turi"]},
            "joylar_soni": {i["joylar_soni"]},
            "transport_turi": {i["transport_turi"]},""")
          
def foydalanuvchi_menu():
    print("""
    Foydalanuvchi panel

1-tourlarni kurish
2-tourlarni qidirish
3-shaxsiy kabinet
4-savatcha
5-chiqish

""")
    a=input("Tanlang:")


    if a=="1":
        barcha_tour()
    elif a=="2":
        tour_qidirish()
    elif a=="3":
        shaxsiy_kabinet()
    elif a=="4":
        pass
    elif a=="5":
        print("Foydalanuvchi paneldan chiqildi")
        return
    else:
        print("Notogri buyruq")
        foydalanuvchi_menu()