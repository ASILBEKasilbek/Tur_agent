# from dastur_kodlari.abdumalik import example
# from dastur_kodlari.asilbek.admin_menu import admin_menu
# print("1-admin\n2-agent\n3-user")
KOK="\033[34m"
QIZIL="\033[31m"
YASHIL="\033[32m"
RANG="\033[0m"  
# print("\033[34m nimadir \033[0m")

# a=input(YASHIL+"Kim siz?:"+RANG)
# if a=="1":
#     print(QIZIL+"salom admin"+RANG)
# elif a=="2":
#     print(KOK+"salom agent"+RANG)
# elif a=="3":
#     print(YASHIL+"salom user"+RANG)
# admin_menu()
from dastur_kodlari.alibek.agent.agent import agent_menu

def tour_main():
    while True:
        print(f"""
    {QIZIL}Shaxslar:{RANG}
            {KOK}1-foydalanuvchi
            2-agent
            3-admin{RANG}
            """)
        a=input(f"{YASHIL}Tanlang tizimga kim bulib kirmoqchisiz(faqat son kiriting):{RANG}")
        if a=="1":
            # foyda
            pass
        elif a=="2":
            agent_menu()
        elif a=="3":
            # admin_menu()
            pass
        else:
            print(f"{QIZIL}Notogri buyruq kiritdingiz!!!{RANG}")
            print(f"{QIZIL}Boshidan tanlang:{RANG}")


if __name__=="__main__":
    tour_main()