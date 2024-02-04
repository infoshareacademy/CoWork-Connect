def user_data_input():
    print("Wprowadź dane osobowe")
    valid_choice = True
    while valid_choice:

        def name_insert():
            valid_name = True
            while valid_name:
                name = input("Podaj swoje imie: ")
                if name.isalpha():
                    return name
                    valid_name = False
                else:
                    print("Podaj poprawne imię")
        name = name_insert()

        def surname_insert():
            valid_surname = True
            while valid_surname:
                surname = input("Podaj swoje nazwisko: ")
                if surname.isalpha():
                    return surname
                    valid_surname = False
                else:
                    print("Podaj poprawne nazwisko")
        surname = surname_insert()

        def valid_phone_insert():
            valid_phone = True
            while valid_phone:
                phone = input("Podaj numer telefonu liczbami bez kierunkowego (9 cyfr): ")
                if phone.isdigit() and len(phone) == 9:
                    return phone
                    valid_phone = False
                else:
                    print("Podaj poprawny numer telefonu")
        phone = valid_phone_insert()

        def valid_email_insert():
            valid_mail = True
            while valid_mail:
                email = input("Podaj swoj adres e-mail: ")
                if '@' in email and '.' in email and len(email) >= 6:
                    return email
                    valid_mail = False
                else:
                    print("Podaj poprawny adres e-mail")
        email = valid_email_insert()

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