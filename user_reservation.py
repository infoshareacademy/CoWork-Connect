from clients_db import saving_clients_data
from desk_database_checker import reading_database, choosing_desk
from userdata_input import user_data_input

def user_reservation_module():
    print("Za chwilę zaprezentuję listę dostepnych biurek. Ile stanowisk Cię interesuje?: ")
    print("Biurko 1-osobowe - wprowadź cyfrę 1")
    print("Biurko 4-osobowe - wprowadź cyfrę 4")
    print("Biurko 10-osobowe - wprowadź cyfrę 10")
    def size_choosing():
        valid_choice = True
        while valid_choice:
            user_choice_size = input("Wprowadź swój wybór: ")
            if user_choice_size.isdigit():
                if int(user_choice_size) == 1:
                    return user_choice_size
                    valid_choice = False
                elif int(user_choice_size) == 4:
                    return user_choice_size
                    valid_choice = False
                elif int(user_choice_size) == 10:
                    return user_choice_size
                    valid_choice = False
                else:
                    print("Wprowadzono niewłaściwą wartość, podaj wartość cyfrą: 1, 4 lub 10.")
            else:
                print("Wprowadzono niewłaściwą wartość, podaj wartość cyfrą: 1, 4 lub 10.")
    user_choice_size = size_choosing()

    print(f"Twój wybór to biurko {user_choice_size}-osobowe.")
    print("Czy interesuje Cię biurko z monitorem czy bez?")
    print("Biurko z monitorem - wprowadź cyfrę 1")
    print("Biurko bez monitora - wprowadź cyfrę 2")
    def display_choosing():
        valid_choice = True
        while valid_choice:
            user_choice_display = input("Wprowadź swój wybór: ")
            if user_choice_display.isdigit():
                if int(user_choice_display) == 1:
                    return user_choice_display
                    valid_choice = False
                elif int(user_choice_display) == 2:
                    return user_choice_display
                    valid_choice = False
                else:
                    print("Wprowadzono niewłaściwą wartość, podaj 1 lub 2.")
            else:
                print("Wprowadzono niewłaściwą wartość, podaj wartość 1 lub 2.")
    user_choice_display = display_choosing()

    def presenting_avaliability():
        if int(user_choice_size) == 1 and int(user_choice_display) == 1:
            print("Prezentuję ofertę dostępnych biurek 1-osobowych z monitorem")
            size = 'pojedyncze'
            display = 'monitorem'
            return size, display

        elif int(user_choice_size) == 1 and int(user_choice_display) == 2:
            print("Prezentuję ofertę dostępnych biurek 1-osobowych bez monitora")
            reading_database('desks.json')
            size = 'pojedyncze'
            display = 'bez monitora'
            return size, display

        elif int(user_choice_size) == 4 and int(user_choice_display) == 1:
            print("Prezentuję ofertę dostępnych biurek 4-osobowych z monitorem")
            size = '4 osobowe'
            display = 'z monitorami'
            return size, display

        elif int(user_choice_size) == 4 and int(user_choice_display) == 2:
            print("Prezentuję ofertę dostępnych biurek 4-osobowych bez monitora")
            size = '4 osobowe'
            display = 'bez monitorów'
            return size, display

        elif int(user_choice_size) == 10 and int(user_choice_display) == 1:
            print("Prezentuję ofertę dostępnych biurek 10-osobowych z monitorem")
            size = '10 osobowe'
            display = 'monitorami'
            return size, display

        elif int(user_choice_size) == 10 and int(user_choice_display) == 2:
            print("Prezentuję ofertę dostępnych biurek 10-osobowych bez monitora")
            size = '10 osobowe'
            display = 'monitorów'
            return size, display
    size, display = presenting_avaliability()
    reading_database('desks.json', size, display)

    print("Oto lista dostępnych biurek.")
    user_desk_choice = input("Wprowadź numer wybranego przez siebie biurka: ")
    desk_price, desk_name = choosing_desk(user_desk_choice)

    def value_calculating(desk_price):
        valid_choice = True
        while valid_choice:
            user_hours_choice = input("Wprowadź liczbę godzin, na jakie chciałbyś wynająć biurko (wpisz cyfrę - np. 8): ")

            if user_hours_choice.isdigit():
                user_hours_choice = int(user_hours_choice)
                total_value = desk_price*user_hours_choice
                print(f"Wynajem biurka będzie kosztował {total_value} PLN")
                return total_value, user_hours_choice
                valid_choice = False
            else:
                print("Wprowadź poprawną wartość liczbową (cyfrę - np. 8).")
    total_value, user_hours_choice = value_calculating(desk_price)
    print(f"Wybrałeś {desk_name}, całkowita cena wynajmu wyniesie {total_value} PLN.")

    def confirming_inputed_data(desk_name, user_hours_choice):
        valid_choice = True
        while valid_choice:
            accepting_order = input("Potwierdź czy powyższe informacje się zgadzają (tak lub nie): ")
            if accepting_order.lower() == 'tak':
                print("Potwierdzono")
                name, surname, phone, email = user_data_input()
                date = '10.01.2024'
                reservation_id = saving_clients_data(desk_name, date, user_hours_choice, name, surname, phone, email)
                print(f"Zapisano pomyślnie dane.")
                print(f"Twoj numer rezerwacji to: {reservation_id}, który został przypisany do numeru telefonu: {phone}")
                valid_choice = False
            elif accepting_order.lower() == 'nie':
                print("Nie potwierdzono")
            else:
                print("Wprowadzono niewłaściwą odpowiedź, wprowadź odpowiedź tak lub nie")
    confirming_inputed_data(desk_name, user_hours_choice)
    print("Do widzenia")

if __name__ == "__main__":
    user_reservation_module()