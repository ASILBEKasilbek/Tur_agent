
agent=[

        {
            "toliq ism-sharif": "Rasulov Bekzod Jamshid ogli",
            "tugilgan sana": "05-09-1999",
            "jinsi": "erkak",
            "passport seriyasi va raqami": "AC9876543",
            "telefon raqami": "+998933334455",
            "e_pochta": "bekzod@example.com",
            "manzil": "Samarqand viloyati, Kattaqorgon tumani",
        },

        {
            "Toliq ism-sharif": "Yusupov Azizbek Otabek ogli",
            "Tugilgan sana": "22-07-2000",
            "Jinsi": "erkak",
            "Pasport seriyasi va raqami": "AA1234589",
            "Telefon raqami": "+998971234567",
            "E-pochta": "azizbek.yusupov@example.com",
            "Manzil": "Fargona viloyati, Qoqon shahri"
        },
        {
            "Toliq ism-sharif": "Tursunova Mohira Shavkat qizi",
            "Tugilgan sana": "11-11-2002",
            "Jinsi": "ayol",
            "Pasport seriyasi va raqami": "AD7788990",
            "Telefon raqami": "+998935556677",
            "E-pochta": "mohira.tursunova@example.com",
            "Manzil": "Buxoro viloyati, G‘ijduvon tumani"
        },
        {
            "Toliq ism-sharif": "Abdullayev Diyorbek Rustam o‘g‘li",
            "Tugilgan sana": "03-05-1998",
            "Jinsi": "erkak",
            "Pasport seriyasi va raqami": "AE1122334",
            "Telefon raqami": "+998939991188",
            "E-pochta": "diyorbek.abdullayev@example.com",
            "Manzil": "Andijon viloyati, Asaka tumani"
        },
        {
            "Toliq ism-sharif": "Xoliqova Saodat Zokir qizi",
            "Tugilgan sana": "27-09-2003",
            "Jinsi": "ayol",
            "Pasport seriyasi va raqami": "AF5566778",
            "Telefon raqami": "+998909002233",
            "E-pochta": "saodat.xoliqova@example.com",
            "Manzil": "Namangan viloyati, Pop tumani"
        },



       
      ]
def list_all_agents():
    """ Agentlar royhati ko'rsatiladi """
    for key,value in agent.items():
        print(f"{key}:{value}")
    return "Agentlkar ro'yhati ko'rsatildi"



def add_agent(toliq_ism_sharif,tugilgan_sana,jinsi,passport_seriyasi_va_raqami,telefon_raqami,e_pochta,manzil):
    agent["toliq ism sharif"] = toliq_ism_sharif
    agent["tugilgan sana"] = tugilgan_sana
    agent["jinsi"] = jinsi
    agent["passport"] = passport_seriyasi_va_raqami
    agent["telefon raqam"] = telefon_raqami
    agent["e_pochta"] = e_pochta
    agent["manzil"] = manzil

    return "Yangi mijoz qo'shildi"

print(list_all_agents)
print(add_agent("Karimova Dilnoza Rustam qizi","22-03-2001","ayol","AB1234567","+998901234567","bekzod@example.com","Samarqand viloyati Kattaqorgon tumani"))
print(list_all_agents())

def delete_agent(agentlar, passport_seriyasi_va_raqami):
    oxirgi_royhat = []
    for i in agentlar:
        if i["Pasport seriyasi va raqami"] != passport_seriyasi_va_raqami:
            oxirgi_royhat.append(i)
    return oxirgi_royhat

print(delete_agent())


