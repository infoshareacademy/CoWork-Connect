from clients_db import saving_clients_data
from desk_database_checker import reading_database, choosing_desk
from userdata_input import user_data_input
from datetime import datetime


def user_reservation_module():
    print("Za chwilę zaprezentuję listę dostepnych biurek.")

    def beginning_date():
        while True:
            print("Od kiedy chcesz wynająć stanowisko?")
            current_date = datetime.today().date()
            input_beginning_date = input("Wprowadź datę w formacie YYYY-MM-DD: ")
            try:
                user_beginning_date = datetime.strptime(input_beginning_date, "%Y-%m-%d").date()
                if user_beginning_date >= current_date:
                    user_beginning_date_str = user_beginning_date.strftime("%Y-%m-%d")
                    return user_beginning_date_str, user_beginning_date
                else:
                    print("Data powinna być późniejsza niż dzisiejsza. Spróbuj ponownie.")
            except ValueError:
                print("Wprowadź odpowiednią datę w formacie YYYY-MM-DD")
    user_beginning_date_str, user_beginning_date = beginning_date()


    def end_date(user_beginning_date):
        while True:
            print("Do kiedy chcesz wynająć stanowisko (wprowadzony dzień włącznie)?")
            input_end_date = input("Wprowadź datę w formacie YYYY-MM-DD: ")
            try:
                user_end_date = datetime.strptime(input_end_date, "%Y-%m-%d").date()
                if user_end_date >= user_beginning_date:
                    user_end_date_str = user_end_date.strftime("%Y-%m-%d")
                    counter = user_end_date - user_beginning_date
                    days_counter = counter.days + 1
                    print(f"Wybrano biurko w przedziale czasowym od {user_beginning_date} do {user_end_date}.")
                    print(f"Całkowita liczba dni wynosi: {days_counter}")
                    return user_end_date_str, user_end_date, days_counter
                else:
                    print("Data powinna być późniejsza niż data początkowa. Spróbuj ponownie.")
            except ValueError:
                print("Wprowadź odpowiednią datę w formacie YYYY-MM-DD")
    user_end_date_str, user_end_date, days_counter = end_date(user_beginning_date)


    def size_choosing():
        print("Ile stanowisk Cię interesuje?: ")
        print("Biurko 1-osobowe - wprowadź cyfrę 1")
        print("Biurko 4-osobowe - wprowadź cyfrę 4")
        print("Biurko 10-osobowe - wprowadź cyfrę 10")
        while True:
            user_choice_size = input("Wprowadź swój wybór: ")
            if user_choice_size.isdigit():
                if int(user_choice_size) == 1:
                    print(f"Twój wybór to biurko {user_choice_size}-osobowe.")
                    return user_choice_size
                elif int(user_choice_size) == 4:
                    print(f"Twój wybór to biurko {user_choice_size}-osobowe.")
                    return user_choice_size
                elif int(user_choice_size) == 10:
                    print(f"Twój wybór to biurko {user_choice_size}-osobowe.")
                    return user_choice_size
                else:
                    print("Wprowadzono niewłaściwą wartość, podaj wartość cyfrą: 1, 4 lub 10.")
            else:
                print("Wprowadzono niewłaściwą wartość, podaj wartość cyfrą: 1, 4 lub 10.")
    user_choice_size = size_choosing()


    def display_choosing():
        print("Czy interesuje Cię biurko z monitorem czy bez?")
        print("Biurko z monitorem - wprowadź cyfrę 1")
        print("Biurko bez monitora - wprowadź cyfrę 2")
        while True:
            user_choice_display = input("Wprowadź swój wybór: ")
            if user_choice_display.isdigit():
                if int(user_choice_display) == 1:
                    return user_choice_display
                elif int(user_choice_display) == 2:
                    return user_choice_display
                else:
                    print("Wprowadzono niewłaściwą wartość, podaj 1 lub 2.")
            else:
                print("Wprowadzono niewłaściwą wartość, podaj wartość 1 lub 2.")
    user_choice_display = display_choosing()

    def presenting_avaliability():
        if int(user_choice_size) == 1 and int(user_choice_display) == 1:
            print("Prezentuję ofertę dostępnych biurek 1-osobowych z monitorem")
            rozmiar = 1
            monitor = True
            return rozmiar, monitor

        elif int(user_choice_size) == 1 and int(user_choice_display) == 2:
            print("Prezentuję ofertę dostępnych biurek 1-osobowych bez monitora")
            reading_database('desks.json')
            rozmiar = 1
            monitor = False
            return rozmiar, monitor

        elif int(user_choice_size) == 4 and int(user_choice_display) == 1:
            print("Prezentuję ofertę dostępnych biurek 4-osobowych z monitorem")
            rozmiar = 4
            monitor = True
            return rozmiar, monitor

        elif int(user_choice_size) == 4 and int(user_choice_display) == 2:
            print("Prezentuję ofertę dostępnych biurek 4-osobowych bez monitora")
            rozmiar = 4
            monitor = False
            return rozmiar, monitor

        elif int(user_choice_size) == 10 and int(user_choice_display) == 1:
            print("Prezentuję ofertę dostępnych biurek 10-osobowych z monitorem")
            rozmiar = 10
            monitor = True
            return rozmiar, monitor

        elif int(user_choice_size) == 10 and int(user_choice_display) == 2:
            print("Prezentuję ofertę dostępnych biurek 10-osobowych bez monitora")
            rozmiar = 10
            monitor = False
            return rozmiar, monitor
    size, display = presenting_avaliability()
    reading_database('desks.json', size, display)

    print("Oto lista dostępnych biurek.")
    user_desk_choice = input("Wprowadź numer wybranego przez siebie biurka: ")
    desk_price, desk_name = choosing_desk(user_desk_choice)

    def value_calculating(desk_price, days_counter):
        total_value = desk_price*days_counter
        print(f"Wybrałeś biurko nr: {desk_name}, całkowita cena wynajmu wyniesie {total_value} PLN.")
        return total_value
    total_value = value_calculating(desk_price, days_counter)

    def confirming_imputed_data(desk_name, user_beginning_date_str, user_end_date_str, total_value):
        while True:
            accepting_order = input("Potwierdź czy powyższe informacje się zgadzają (tak lub nie): ")
            if accepting_order.lower() == 'tak':
                print("Potwierdzono")
                name, surname, phone, email = user_data_input()
                reservation_id = saving_clients_data(desk_name, user_beginning_date_str, user_end_date_str, name, surname, phone, email)
                print(f"Zapisano pomyślnie dane.")
                print(f"Twoj numer rezerwacji to: {reservation_id}, który został przypisany do numeru telefonu: {phone}")
                return reservation_id
            elif accepting_order.lower() == 'nie':
                print("Nie potwierdzono")
            else:
                print("Wprowadzono niewłaściwą odpowiedź, wprowadź odpowiedź tak lub nie")
    confirming_imputed_data(desk_name, user_beginning_date_str, user_end_date_str, total_value)
    print("Do widzenia")

if __name__ == "__main__":
    user_reservation_module()