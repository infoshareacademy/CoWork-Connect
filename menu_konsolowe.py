


# pozostałość logowania - do rewizji
# def admin_account():
#     adm_login = input("Podaj login:")
#     adm_password = input("Podaj Hasło:")


def main_menu():

    print("1. ZALOGUJ SIĘ JAKO KLIENT")
    print("2. ZALOGUJ SIĘ JAKO ADMINISTRATOR")
    print("---------------------------------- \n")
    user_input = input("Wybierz panel do którego chcesz się zalogować: ")
    print("---------------------------------- \n")
    if user_input == "1":
        print("Zalogowałeś się do panelu klienta")

        customer_board()
    elif user_input == "2":
        print("Zalogowałeś się do panelu administratora")

        admin_board()
    else:
        print(f"Przepraszam, wybrałeś {user_input}, nie jest to poprawny wybór")



# PANEL KLIENTA
def customer_board():
    print("1. NASZA OFERTA")
    print("2. SZCZEGÓŁOWE SPECYFIKACJE ORAZ CENNIK USŁUG")
    print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
    print("4. REZERWACJA BIURKA")
    print("5. ANULOWANIE REZERWACJI")
    print("6. DANE KONTAKTOWE BIURA")
    print("7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI")
    print("8. WYJŚCIE Z APLIKACJI")
    print("---------------------------------- \n")
    user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę: ")
    while user_choice != "8":
        if user_choice == "1":
            print("1. NASZA OFERTA")
            # admin_account()
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
            print("7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI")
        elif user_choice == "8":
            print("8. WYJŚCIE Z APLIKACJI")
        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")



#PANEL ADMINISTRATORA
def admin_board():
    print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
    print("2. DODWANIE BIURKA/STANOWISKA")
    print("3. USUWANIE BIURKA/STANOWISKA")
    print("4. ANULOWANIE REZERWACJI")
    print("5. EDYCJA REGULAMINU USŁUG")
    print("6. EDYCJA DANYCH KONTAKTOWYCH")
    print("7. WYJŚCIE Z APLIKACJI/WYLOGOWANIE")
    print("---------------------------------- \n")
    user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę: ")
    while user_choice != "7":
        if user_choice == "1":
            print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
        elif user_choice == "2":
            print("2. DODWANIE BIURKA/STANOWISKA")
        elif user_choice == "3":
            print("3. USUWANIE BIURKA/STANOWISKA")
        elif user_choice == "4":
            print("4. ANULOWANIE REZERWACJI")
        elif user_choice == "5":
            print("5. EDYCJA REGULAMINU USŁUG")
        elif user_choice == "6":
            print("6. EDYCJA DANYCH KONTAKTOWYCH")
        elif user_choice == "7":
            print("7. WYJŚCIE Z APLIKACJI/WYLOGOWANIE")
        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")

main_menu()

