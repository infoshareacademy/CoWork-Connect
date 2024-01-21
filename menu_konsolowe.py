from CoWork_klasy import *
import json
def show_admin_desks_view():
    print("Admin Desks View:")
    for keys, values in desks_instances.items():
        print(keys, values)


def add_desk():
    name = input("Podaj nazwę biurka: ")
    desk_type = input("Podaj typ biurka: ")
    price = float(input("Podaj cenę biurka PLN/h: "))
    status = input("Podaj status biurka: ")

    new_desk = Desks(name, desk_type, price, status)
    desks_instances[name] = new_desk
    print("Dodano biurko!")



def delete_desk():
    desk_index = int(input("Podaj indeks biurka do usunięcia: "))

    if desk_index < 0 or desk_index > len(desks_instances) - 1:
        print("Biurko o tym indeksie nie istnieje")
        return

    desks_instances.pop(desk_index)
    print("Usunięto biurko!")


def save_tasks_to_file():
    with open("desks.json", "w") as file:
        data = {}
        for name, desk in desks_instances.items():
            data[name] = {
                "desk_type": desk.desk_type,
                "price": desk.price,
                "status": desk.status,
            }
        json.dump(data, file)
    print("Zapisano biurka do pliku.")

def customer_board():
    user_choice = ""

    while user_choice != "8":
        print_menu_customer()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę:")

        if user_choice == "1":
            print("1. NASZA OFERTA")
        elif user_choice == "2":
            print("2. SZCZEGÓŁOWE SPECYFIKACJE ORAZ CENNIK USŁUG")
        elif user_choice == "3":
            print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
        elif user_choice == "4":
            print("4. REZERWACJA BIURKA")
        elif user_choice == "5":
            print("5. ANULOWANIE REZERWACJI")
        elif user_choice == "6":
            print("6. DANE KONTAKTOWE BIURA")
        elif user_choice == "7":
            print("""
            7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI
            nie mamy jeszcze regulaminu i opcji płatności, ale stworzymy tekst i wrzucimy
                  """)
        elif user_choice == "8":
            print("8. WYJŚCIE Z APLIKACJI")
        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


def admin_board():
    user_choice = ""

    while user_choice != "8":
        print_menu_admin()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę:")

        if user_choice == "1":
            print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
            show_admin_desks_view()

        elif user_choice == "2":
            print("2. DODWANIE BIURKA/STANOWISKA")
            add_desk()

        elif user_choice == "3":
            print("3. USUWANIE BIURKA/STANOWISKA")
            delete_desk()

        elif user_choice == "4":
            print("4. ANULOWANIE REZERWACJI")
        elif user_choice == "5":
            print("5. EDYCJA REGULAMINU USŁUG")
        elif user_choice == "6":
            print("6. EDYCJA DANYCH KONTAKTOWYCH")
        elif user_choice == "7":
            print("7. ZAPISZ ZMIANY")
            save_tasks_to_file()

        elif user_choice != "8":
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


def print_menu_customer():
    print("1. NASZA OFERTA")
    print("2. SZCZEGÓŁOWE SPECYFIKACJE ORAZ CENNIK USŁUG")
    print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
    print("4. REZERWACJA BIURKA")
    print("5. ANULOWANIE REZERWACJI")
    print("6. DANE KONTAKTOWE BIURA")
    print("7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI")
    print("8. WYJŚCIE Z APLIKACJI")


def print_menu_admin():
    print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
    print("2. DODWANIE BIURKA/STANOWISKA")
    print("3. USUWANIE BIURKA/STANOWISKA")
    print("4. ANULOWANIE REZERWACJI")
    print("5. EDYCJA REGULAMINU USŁUG")
    print("6. EDYCJA DANYCH KONTAKTOWYCH")
    print("7. ZAPISZ ZMIANY")
    print("8. WYJŚCIE Z APLIKACJI")


def main_menu():
    user_choice = ""

    while user_choice != "3":
        print("1. Zaloguj się jako klienta")
        print("2. Zaloguj się jako administratora ")
        print("3. WYJŚCIE Z APLIKACJI")
        user_choice = input("Wybierz panel do którego chcesz się zalogować: ")

        if user_choice == "1":
            print("Panel Klienta")
            print("Zalogowałeś się do panelu klienta")

            customer_board()

        elif user_choice == "2":
            print("PANEL ADMINISTRATORA ")
            print("Zalogowałeś się do panelu administratora")

            admin_board()

        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


if __name__ == "__main__":
    main_menu()
