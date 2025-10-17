import json
from view_all_tours.view_tour import view_all_tours
from search_tour.search import search_tours
from  bron.book_tour import book_tour
from mijozlarni_boshqarish.manage_customers import manage_customers
from manage_payments.manage_payments import manage_payments
from view_my_customers_bookings.my_customers_bookings import my_bookings
from log_out.logout import logout
# JSON fayldan o‘qish funksiyasi
# def load_data(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         return json.load(f)
# print(load_data("agent.json"))
# # JSON faylga yozish funksiyasi
# def save_data(filename, data):
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)

# Asosiy menyu
def agent_menu():
    """=== Agent Menu ==="""
    while True:
        print("\n--- Agent Menyusi ---")
        print("1. Barcha turlarni ko‘rish")
        print("2. Turlarni qidirish")
        print("3. Mijoz uchun bron qilish")
        print("4. Mijozlarni boshqarish")
        print("5. To‘lovlarni boshqarish")
        print("6. Mening mijozlarimning bronlari")
        print("7. Chiqish (Logout)")

        tanlov = input("Tanlovni kiriting: ")

        if tanlov == '1':
            view_all_tours()
        elif tanlov == '2':
            search_tours()
        elif tanlov == '3':
            book_tour()
        elif tanlov == '4':
            manage_customers()
        elif tanlov == '5':
            manage_payments()
        elif tanlov == '6':
            my_bookings()
        elif tanlov == '7':
            logout()
        else:
            print("Noto‘g‘ri tanlov! Qaytadan urinib ko‘ring.")


# # === Dastur ishga tushirish ===
if __name__ == "__main__":
    agent_menu()











