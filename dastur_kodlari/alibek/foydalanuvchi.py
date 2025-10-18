

from dastur_kodlari.latofat.admin import barcha_tour,TOURLAR

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
        pass
    elif a=="4":
        pass
    elif a=="5":
        print("Foydalanuvchi paneldan chiqildi")
        return
    else:
        print("Notogri buyruq")
        foydalanuvchi_menu()