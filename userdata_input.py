def user_data_input():
    valid_choice = True
    while valid_choice:
        print("Wprowadź dane osobowe")
        valid_name = True
        while valid_name:
            name = input("Podaj swoje imie: ")
            if name.isalpha():
                valid_name = False
            else:
                print("Podaj poprawne imię")

        valid_surname = True
        while valid_surname:
            surname = input("Podaj swoje nazwisko: ")
            if name.isalpha():
                valid_surname = False
            else:
                print("Podaj poprawne nazwisko")

        valid_phone = True
        while valid_phone:
            phone = input("Podaj numer telefonu liczbami bez kierunkowego (9 cyfr): ")
            if phone.isdigit() and len(phone) == 9:
                valid_phone = False
        valid_mail = True

        while valid_mail:
            email = input("Podaj swoj adres e-mail: ")
            if '@' in email and len(email) >= 10:
                valid_mail = False
            else:
                print("Podaj poprawny adres e-mail")

        print(f"Twoje dane to:"
              f"\nImię: {name}"
              f"\nNazwisko: {surname}"
              f"\nNume telefonu: {phone}"
              f"\nE-mail: {email}")
        accepting_data = input("Czy powyższe dane się zgadzają? (tak lub nie): ")
        if accepting_data.lower() == "tak":
            print("Potwierdzono")
            return name, surname, phone, email
            valid_choice = False
        elif accepting_data.lower() == "nie":
            print("Generuję formularz od nowa")
        else:
            print("Wprowadzono niepoprawne dane, wprowadź dane od nowa")

if __name__ == "__main__":
    user_data_input()