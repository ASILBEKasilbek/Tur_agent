from dastur_kodlari.asilbek.admin import barcha_tour,TOURLAR

KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m" 
# print(f"{QIZIL} ozodbek magic{RANG}")

def shaxsiy_kabinet(foydalanuvchi_id):
    print(f"""{KOK}
        1. Malumotlarim
        2. Balansni ko‘rish
        3. Balansga pul qo‘shish
        4. Ortga
        {RANG}""")
    tanlov = input(f"{YASHIL}Tanlovni kiriting: {RANG}")

    if tanlov == "1":
        malumotlar(foydalanuvchi_id)
    elif tanlov == "2":
        balans_kurish(foydalanuvchi_id)
    elif tanlov == "3":
        pul_qushish(foydalanuvchi_id)
    elif tanlov == "4":
        return
    else:
        print(f"{QIZIL} Noto‘g‘ri tanlov! {RANG}")

def balans_kurish(foydalanuvchi_id):
    for i in USER:
        if i["id"] ==  foydalanuvchi_id:
            print(foydalanuvchi_id)
            print(f"{KOK} Sizning balansingiz:  {YASHIL}{ i["balans"]}{RANG}")

def pul_qushish(foydalanuvchi_balans):
    if foydalanuvchi_balans is None:
        print(f"{QIZIL} Foydalanuvchi topilmadi! {RANG}")
        return
    for i in USER:
        if i["id"] == foydalanuvchi_balans:

            pul = int(input(f"{YASHIL}Qancha pul qoshasiz: {RANG}"))

            if i["balans"]:
                i["balans"]  = int(i["balans"]) + pul
                
            else:
                i["balans"] = pul
            print(f"{KOK}Sizning balansingiz: {i['balans']}{RANG}")
            

def malumotlar(foydalanuvchi_id):
    foydalanuvchi_malumoti=USER[foydalanuvchi_id-1]
    if foydalanuvchi_malumoti:
        print(f"""{KOK}
            Malumotlarim
    Login:{YASHIL}{foydalanuvchi_malumoti['login']}
    {KOK}Parol:{YASHIL}{foydalanuvchi_malumoti['parol']}
            {KOK}Xaridlarim:{YASHIL}
""")
        for i in foydalanuvchi_malumoti['xaridlar']:
            for j in TOURLAR:
                if i==j['id']:
                    print(f"""{YASHIL}
    {j['qayerdan']} ➜ {j['qayerga']} | Narxi: {j['narxi']} so‘m | Vaqt: {j['vaqt']}
        {RANG}""")

def uxshash(qayerdan1,qayerdan2):
    qayerdan1=qayerdan1.lower()
    qayerdan2=qayerdan2.lower()
    t=0
    for i in range(8):
        if qayerdan1[i]==qayerdan2[i]:
            t+=1

    if qayerdan1==qayerdan2 or t>=5:
        return True
    else:
        return False
    

def tour_qidirish():
    print(f"{KOK}Qidirish{RANG}")
    qayerdan=input(f"{YASHIL}qayerdan bormoqchisiz?:{RANG}")
    qayerga=input(f"{YASHIL}qayerga bormoqchisiz?:{RANG}")
    qachon=input(f"{YASHIL}Qachon bormoqchisiz?:{RANG}")
    if not (qayerdan and qayerga and qachon):
        print(f"{QIZIL}Biror nima kiritng!!!{RANG}")
        return
    for i in TOURLAR:
        if uxshash(i["qayerdan"],qayerdan) and uxshash(i["qayerga"],qayerga) and i["vaqt"][:-6]==qachon:
            print(f"{KOK}Topildi!!{RANG}")
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

def foydalanuvchi():
    print(f"""{KOK}
    1-Kirish
    2-Ro'yxatdan o'tish
    3-Ortga{RANG}
""")
    a=input(f" {YASHIL} Tanlang: {RANG}")

    if a=="1":
        d=kirish()#(True, 1)
        if d[0]==True:
            return True,d[1]
        else:
            return False,0
    
    elif a=="2":

        q=ruyxatdan_utish()
        if q[0]==True:
            return True,q[1]
        else:
            return False, 0
    elif a=="3":
        return None
    else:
        print(f"{QIZIL}No'togri buyruq kiritdingiz!!!{RANG}")
        print(f"{QIZIL}Boshidan tanlang:{RANG}")
        foydalanuvchi()


USER=[
    {
        'id':1,
        'login':'Asilbek',
        'parol':'1234',
        'balans':'12345'
    },
    {
        'id':2,
        'login':'Alibek',
        'parol':'1234',
        'balans':'12344'
    },
    {
        'id':3,
        'login':'Ozodbek',
        'parol':'1234',
        'balans':'12344'
    }

]

def ruyxatdan_utish():
    login=input(f"{YASHIL}Login kiriting:{RANG}")
    for i in USER:
        if i['login']==login:
            print(f"{QIZIL}Bu login allaqachon tizimdan ruyxatdan utgan!!!{RANG}")
            return
    parol=input(f"{YASHIL}Parol kiriting:{RANG}")
    parol2=input(f"{YASHIL}Parolni qaytadan kiriting:{RANG}")
    if parol==parol2:

        id_len=len(USER)+1

        USER.append(
            {
                "id":id_len,
                "login":login,
                "parol":parol
            }
        )
        print(f"{KOK}Ro'yxatdan o'tingiz{RANG}")
        return (True,id_len)

    elif parol!=parol2:
        print(f"{QIZIL}Xato{RANG}")
        print(f"{QIZIL}Bir xil kiriting!!{RANG}")
        ruyxatdan_utish()
    else:
        return False



def kirish():
    login=input(f"{YASHIL}Login kiritng:{RANG}")

    parol=input(f"{YASHIL}Parol kiriting:{RANG}")

    for i in USER:
        if i["login"]==login and i["parol"]==parol:
            print(f"{KOK}Tizimga kirdingiz!!!{RANG}")
            return (True,i['id'])
           

    print(f"{QIZIL}Xato{RANG}")
    print(f"{QIZIL}Qaytadan kriting!!!{RANG}")
    return False, 1


SAVAT = []   

def tour_tanlash(foydalanuvchi_id):   
    barcha_tour()
    tanlov = input(f"{YASHIL}Qaysi tur paketini xarid qilasiz? ID raqamini kiriting: {RANG}")
    for i in TOURLAR:
        if str(i["id"]) == tanlov:
            SAVAT.append(
                {
                    "id": foydalanuvchi_id,
                    "tour_id": i["id"],
                })
            print(f"{KOK}Siz {YASHIL}{i['qayerga']} {KOK}yo‘nalishidagi tur paketini tanladingiz!{RANG}")
            print(f"{KOK}Savatingizga qo‘shildi.{RANG}")
            break
    else:
        print(f"{QIZIL}Bunday ID mavjud emas.{RANG}")


def savat(foydalanuvchi_id):
    if not SAVAT:
        print(f"{QIZIL}Savat hozircha bo‘sh.{RANG}")
        return

    print(f"{YASHIL}Sizning savatingiz:{RANG}")
    jami_summa = 0
    k=[]
    for j in SAVAT:
        if j['id'] == foydalanuvchi_id:
            for i in TOURLAR:
                if i['id'] == j['tour_id']:
                    k.append(i)
                    jami_summa += int(i["narxi"])
                    print(f"{KOK}{i['qayerdan']} ➜ {i['qayerga']} | Narxi: {i['narxi']} so‘m | Vaqt: {i['vaqt']}{RANG}")
    else:
        if not k:
            print(f"{QIZIL}Savat hozircha bo‘sh.{RANG}")
            return
        
    for i in USER:
        if i['id'] == foydalanuvchi_id:
            balans = int(i['balans'])
            print(f"{KOK}Sizning balansingiz: {balans} so‘m{RANG}")
            break

    print(f"{KOK}\nJami summa: {YASHIL}{jami_summa} so‘m{RANG}")

    tasdiq = input(f"{KOK}Savatdagi turlarni xarid qilasizmi? (ha/yo‘q): {RANG}").lower()
    if tasdiq != "ha":
        print(f"{QIZIL}Xarid bekor qilindi.{RANG}")
        return

 
    for i in USER:
        if i["id"] == foydalanuvchi_id:
            foydalanuvchi = i
            break
    else:
        print(f"{QIZIL}Foydalanuvchi topilmadi!{RANG}")
        return

    balans = int(foydalanuvchi["balans"])

    if balans >= jami_summa:
        
        foydalanuvchi["balans"] = balans - jami_summa
        print(f"{YASHIL}Xarid muvaffaqiyatli amalga oshirildi!{RANG}")
        print(f"{KOK}Yangi balans: {foydalanuvchi['balans']} so‘m{RANG}")
        
        if "xaridlar" not in foydalanuvchi:
            foydalanuvchi["xaridlar"] = []

        for i in SAVAT[:]:
            if i['id'] == foydalanuvchi_id:
                SAVAT.remove(i)
                foydalanuvchi["xaridlar"].append(i['tour_id'])
    else:
        kerak = jami_summa - balans
        print(f"{QIZIL}Balans yetarli emas! Sizga {kerak} so‘m kerak.{RANG}")
        tanlov = input(f"{YASHIL}Balansni to‘ldirasizmi? (ha/yo‘q): {RANG}").lower()

        if tanlov == "ha":
            pul = int(input(f"{YASHIL}Qancha pul qo‘shmoqchisiz?: {RANG}"))
            foydalanuvchi["balans"] = balans + pul
            print(f"{KOK}Yangi balans: {foydalanuvchi['balans']} so‘m{RANG}")

            if foydalanuvchi["balans"] >= jami_summa:
                foydalanuvchi["balans"] -= jami_summa
                print(f"{KOK}Xarid amalga oshirildi!{RANG}")
                print(f"{KOK}Yangi balans: {foydalanuvchi['balans']} so‘m{RANG}")

                if "xaridlar" not in foydalanuvchi:
                    foydalanuvchi["xaridlar"] = []
                for i in SAVAT[:]:
                    if i['id'] == foydalanuvchi_id:
                        SAVAT.remove(i)
                        foydalanuvchi["xaridlar"].append(i['tour_id'])
            else:
                print(f"{QIZIL}Balans hali ham yetarli emas.{RANG}")
        else:
            print(f"{QIZIL}Xarid bekor qilindi.{RANG}")


def foydalanuvchi_menu():
    a=foydalanuvchi()#(True,id)
    if a==None:
        return 
    elif a[0]==False:
        foydalanuvchi_menu()
    foydalanuvchi_id=a[1]
    while True:
        print(f"""
        {KOK}Foydalanuvchi panel

    1-tourlarni kurish
    2-tourlarni qidirish
    3-shaxsiy kabinet
    4-savatcha{QIZIL}
    5-chiqish
{RANG}
    """)
        a=input(f" {YASHIL} Tanlang: {RANG}")
        
        if a=="1":
            tour_tanlash(foydalanuvchi_id)
        elif a=="2":
            tour_qidirish()
        elif a=="3":
            shaxsiy_kabinet(foydalanuvchi_id)
        elif a=="4":
            savat(foydalanuvchi_id)
        elif a=="5":
            print(f"{KOK}Foydalanuvchi paneldan chiqildi{RANG}")
            return
        else:
            print(f"{QIZIL}Notogri buyruq{RANG}")