from desk import *
from desk_manager import DeskManager
import json


def delete_desk():
    desks_instances = load_desks_from_file("desks.json")

    print("Akturalne biurka:")
    for desk in desks_instances.values():
        print(f"Id: {desk.name}, {json.dumps(desk.to_dict(), indent=2)} ")

    if not desks_instances:
        print("Brak dostępnych biurek do usunięcia!")
        return

    try:
        del_desk_name = input(
            "Podaj indeks biurka do usunięcia (lub wpisz -1, żeby anulować): "
        )

        if del_desk_name == "-1":
            print("Anulowano usunięcie.")
            return

        if del_desk_name in desks_instances:
            desks_instances.pop(del_desk_name)
            print(f"Usunięto biurko: {del_desk_name}")

        else:
            print("Nieprawidłowa nazwa biurka. Nie usunięto żadnego biurka.")

        save_desks_to_file(desks_instances)

    except ValueError:
        print("Nieprawidłowe dane wejściowe. Podaj prawidłową nazwę biurka.")


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
            print(
                """
            7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI
            nie mamy jeszcze regulaminu i opcji płatności, ale stworzymy tekst i wrzucimy
                  """
            )
        elif user_choice == "8":
            print("8. WYJŚCIE Z APLIKACJI")
        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


def admin_board():
    user_choice = ""
    desk_manager = DeskManager()

    while user_choice != "8":
        print_menu_admin()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę:")

        if user_choice == "1":
            print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
            desk_manager.show_all_desks()

        elif user_choice == "2":
            print("2. DODWANIE BIURKA/STANOWISKA")
            desk_manager.add_desk()

        elif user_choice == "4":
            print("4. ANULOWANIE REZERWACJI")
        elif user_choice == "5":
            print("5. EDYCJA REGULAMINU USŁUG")
        elif user_choice == "6":
            print("6. EDYCJA DANYCH KONTAKTOWYCH")
        elif user_choice == "7":
            print("7. ZAPISZ ZMIANY")

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
