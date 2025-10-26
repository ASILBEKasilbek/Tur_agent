

from dastur_kodlari.asilbek.admin import barcha_tour,TOURLAR

KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m" 
# print(f"{QIZIL} ozodbek magic{RANG}")

def shaxsiy_kabinet(foydalanuvchi_id):
    print(f"""{YASHIL}
        1. Malumotlarim
        2. Balansni ko‘rish
        3. Balansga pul qo‘shish
        4. Chiqish
        {RANG}""")
    
    tanlov = input(f"{KOK}Tanlovni kiriting: {RANG}")

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
    for i in user:
        if i["id"] ==  foydalanuvchi_id:
            print(foydalanuvchi_id)
            print(f"{KOK} Sizning balansingiz:  {YASHIL}{ i["balans"]}{RANG}")
            

def pul_qushish(foydalanuvchi_balans):
    for i in user:
        if i["id"] == foydalanuvchi_balans:
        
            pul = int(input("Qancha pul qoshasiz: "))

            if i["balans"]:
                print(type(pul),type(i["balans"]))
                i["balans"]  = int(i["balans"]) + pul
                
            else:
                i["balans"] = pul
            print(f"Sizning balansingiz: {i["balans"]}")
            
        

    
    
    


def malumotlar(foydalanuvchi_id):
    for i in user:
        if i["id"]==foydalanuvchi_id:
            print(f"""
        Malumotlarim
login:{i['login']}
parol:{i['parol']}
""")

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
          
def foydalanuvchi():
    print("""
    1-KIRISH
    2-RO'YXTADAN O'TISH
    3-ortga
""")
    a=input(f" {YASHIL} Tanlang: {RANG}")

    if a=="1":
        d=kirish()#(True, 1)
        print(d)
        if d[0]==True:
            return True,d[1]
        else:
            return False,0
    
    elif a=="2":

        q=ruyxatdan_utish()
        print(q)
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


user=[
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
    login=input("Login kiriting:")
    for i in user:
        if i['login']==login:
            print("Bu login allaqachon tizimdan ruyxatdan utgan!!!")
            return 
    parol=input("Parol kiriting:")
    parol2=input("parolni qaytadan kiriting:")
    if parol==parol2:

        id_len=len(user)+1

        user.append(
            {
                "id":id_len,
                "login":login,
                "parol":parol
            }
        )
        print("Ro'yxatdan o'tingiz")
        return (True,id_len)

    elif parol!=parol2:
        print("Xato")
        print("Bir xil kiriting!!")
        ruyxatdan_utish()
    else:
        return False



def kirish():
    login=input("Login kiritng:")
    
    parol=input("parol kiriting:")
    
    for i in user:
        if i["login"]==login and i["parol"]==parol:
            print("Tizimga kirdingiz!!!")
            return (True,i['id'])
           

    print("Xato")
    print("Qaytadan kriting!!!")
    return False, 1
        


def foydalanuvchi_menu():
    a=foydalanuvchi()#(True,id)
    if a==None:
        return 
    elif a[0]==False:
        foydalanuvchi_menu()
    foydalanuvchi_id=a[1]
    print("""
    Foydalanuvchi panel

1-tourlarni kurish
2-tourlarni qidirish
3-shaxsiy kabinet
4-savatcha
5-chiqish

""")
    a=input(f" {YASHIL} Tanlang: {RANG}")

    if a=="1":
        barcha_tour()
    elif a=="2":
        tour_qidirish()
    elif a=="3":
        shaxsiy_kabinet(foydalanuvchi_id)
    elif a=="4":
        pass
    elif a=="5":
        print("Foydalanuvchi paneldan chiqildi")
        return
    else:
        print("Notogri buyruq")
        foydalanuvchi_menu()