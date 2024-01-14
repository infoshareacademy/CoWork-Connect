



def admin_account():
    adm_login = input("Podaj login:")
    adm_password = input("Podaj Hasło:")

    ###TODO JSON FILE
    # if (adm_login and adm_password) == :

print("1. Panel klienta")
print("2. Panel administratora ")
user_input = int(input("Wybierz panel do którego chcesz się zalogować: "))
if user_input == 1:
    print("Panel Klienta wciśnij 1")
    print("Zalogowałeś się do panelu klienta")
elif user_input == 2:
    print("PANEL ADMINISTRATORA ")
    print("Zalogowałeś się do panelu administratora")

print("1. NASZA OFERTA")
print("2. SZCZEGÓŁOWE SPECYFIKACJE ORAZ CENNIK USŁUG")
print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
print("4. REZERWACJA BIURKA")
print("5. ANULOWANIE REZERWACJI")
print("6. DANE KONTAKTOWE BIURA")
print("7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI")
user_choice = input("Wybierz z ")
# PANEL KLIENTA
if user_choice == 1:
    print("1. NASZA OFERTA")
elif user_choice == 2:
    print("2. SZCZEGÓŁOWE SPECYFIKACJE ORAZ CENNIK USŁUG")
elif user_choice == 3:
    print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
elif user_choice == 4:
    print("4. REZERWACJA BIURKA")
elif user_choice == 5:
    print("5. ANULOWANIE REZERWACJI")
elif user_choice == 6:
    print("6. DANE KONTAKTOWE BIURA")
elif user_choice == 7:
    print("7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI")


elif user_choice == 8:
    print("8. WYJŚCIE Z APLIKACJI")
#PANEL ADMINISTRATORA

if user_choice == 1:
    print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
elif user_choice == 2:
    print("2. DODWANIE BIURKA/STANOWISKA")
elif user_choice == 3:
    print("3. USUWANIE BIURKA/STANOWISKA")
elif user_choice == 4:
    print("4. ANULOWANIE REZERWACJI")
elif user_choice == 5:
    print("5. EDYCJA REGULAMINU USŁUG")
elif user_choice == 6:
    print("6. EDYCJA DANYCH KONTAKTOWYCH")
elif user_choice == 7:
    print("7. WYJŚCIE Z APLIKACJI/WYLOGOWANIE")