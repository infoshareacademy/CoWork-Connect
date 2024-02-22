from class_reservation_with_cancel import *
from desk import *
from desk_manager import DeskAdder, DeskDeleter


def customer_board():
    user_choice = ""

    while user_choice != "8":
        print_menu_customer()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę:")

        if user_choice == "1":
            with open("oferta_biura.json", "r") as file:
                offer = json.load(file)
                for key, value in offer.items():
                    print(value)
            print(input("POWRÓT DO MENU KLIENTA - NACIŚNIJ ENTER"))
        elif user_choice == "2":

            desks_instances = load_desks_from_file("desks.json")

            print(
                "\n",
                "Szczegółowe specyfikacje oraz cennik biurek (lista zawiera wszystkie dostępne biurka):",
            )
            for desk in desks_instances.values():
                print(
                    f" Numer {desk.name} - rodzaj: {desk.desk_type}, cena: {desk.price} PLN, status: {desk.status}"
                )
            print(input("POWRÓT DO MENU KLIENTA - NACIŚNIJ ENTER"))
        elif user_choice == "3":
            print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
        elif user_choice == "4":
            ReservationManager()
            DeskManager()
            ClientDataManager()
        elif user_choice == "5":
            ReservationCanceler.cancel_reservation()
        elif user_choice == "6":
            with open("dane_kontaktowe.json", "r") as file:
                offer = json.load(file)
                for key, value in offer.items():
                    print(value)
            print(input("POWRÓT DO MENU KLIENTA - NACIŚNIJ ENTER"))
        elif user_choice == "7":
            with open("regulamin_opcje_platnosci.json", "r") as file:
                offer = json.load(file)
                for key, value in offer.items():
                    print(value)
            print(input("POWRÓT DO MENU KLIENTA - NACIŚNIJ ENTER"))
        elif user_choice == "8":
            print("8. WYJŚCIE Z APLIKACJI")
        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


def admin_board():
    user_choice = ""

    while user_choice != "5":
        print_menu_admin()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę: ")

        if user_choice == "1":
            print("1. LISTA REZERWACJI I DANE SUMARYCZNE")

        elif user_choice == "2":
            print("2. DODWANIE BIURKA/STANOWISKA")
            desk_manager = DeskAdder()
            desk_manager.add_desk()

        elif user_choice == "3":
            print("3. USUWANIE BIURKA/STANOWISKA")
            desk_deleter = DeskDeleter()
            desk_deleter.delete_desk()

        elif user_choice == "4":
            print("4. ANULOWANIE REZERWACJI")
            ReservationCanceler.cancel_reservation()

        elif user_choice != "5":
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
    print("5. WYJŚCIE Z APLIKACJI")


def main_menu():
    user_choice = ""

    while user_choice != "3":
        print("1. Zaloguj się jako klient")
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
