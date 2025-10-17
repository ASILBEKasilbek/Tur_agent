
def manage_customers():
    print("\n--- Mijozlarni boshqarish ---")
    print("1. Mijozlar ro‘yxati")
    print("2. Yangi mijoz qo‘shish")
    print("3. Mijozni tahrirlash")
    print("4. Mijozni o‘chirish")

    tanlov = input("Tanlovni kiriting: ")
    if tanlov == '1':
        list_customers()
    elif tanlov == '2':
        add_customer()
    elif tanlov == '3':
        edit_customer()
    elif tanlov == '4':
        delete_customer()
    else:
        print("Noto‘g‘ri tanlov!")


def list_customers():
    pass

def add_customer():
    pass

def edit_customer():
    pass

def delete_customer():
    pass