def manage_payments():
    """=== To'lovlarni boshqarish ==="""
    print("1. To‘lov qo‘shish")
    print("2. To‘lovlar tarixi")

    tanlov = input("Tanlovni kiriting: ")
    if tanlov == '1':
        add_payment()
    elif tanlov == '2':
        view_payment_history()
    else:
        print("Noto‘g‘ri tanlov!")


def add_payment():
    pass

def view_payment_history():
    pass

