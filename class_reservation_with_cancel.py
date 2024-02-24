import json
from datetime import datetime
from desk import load_desks_from_file


class ReservationManager:
    def __init__(self):
        self.user_beginning_date_str, self.user_beginning_date = self.beginning_date()
        self.user_end_date_str, self.user_end_date, self.days_counter = self.end_date(self.user_beginning_date)
        self.user_choice_size = self.size_choosing()
        self.user_choice_display = self.display_choosing()
        self.reserved_desks = self.checking_availiability_by_date(self.user_beginning_date_str, self.user_end_date_str, filename='user_data.json')
        self.showing_desk(self.reserved_desks, self.user_choice_size, self.user_choice_display)
        self.total_cost, self.desk_name, self.desk_type = self.choosing_desk_from_displayed(self.user_desk_choice, self.days_counter)
        self.total_value = self.value_calculating(self.total_cost)
        ClientDataManager().confirming_imputed_data(self.desk_name, self.desk_type, self.user_beginning_date_str,
                                                    self.user_end_date_str, self.total_value)

    def beginning_date(self):
        print("Od kiedy chcesz wynająć stanowisko?")
        current_date = datetime.today().date()
        input_beginning_date = input("Wprowadź datę w formacie YYYY-MM-DD: ")
        try:
            user_beginning_date = datetime.strptime(input_beginning_date, "%Y-%m-%d").date()
            if user_beginning_date >= current_date:
                self.user_beginning_date_str = user_beginning_date.strftime("%Y-%m-%d")
                return self.user_beginning_date_str, user_beginning_date
            else:
                print("Data powinna być późniejsza niż dzisiejsza. Spróbuj ponownie.")
        except ValueError:
            print("Wprowadź odpowiednią datę w formacie YYYY-MM-DD")
        return self.beginning_date()

    def end_date(self, user_beginning_date):
        print("Do kiedy chcesz wynająć stanowisko (wprowadzony dzień włącznie)?")
        input_end_date = input("Wprowadź datę w formacie YYYY-MM-DD: ")
        try:
            user_end_date = datetime.strptime(input_end_date, "%Y-%m-%d").date()
            if user_end_date >= user_beginning_date:
                self.user_end_date_str = user_end_date.strftime("%Y-%m-%d")
                counter = user_end_date - user_beginning_date
                self.days_counter = counter.days + 1
                print(f"Wybrano biurko w przedziale czasowym od {user_beginning_date} do {user_end_date}.")
                print(f"Całkowita liczba dni wynosi: {self.days_counter}")
                return self.user_end_date_str, user_end_date, self.days_counter
            else:
                print("Data powinna być późniejsza niż data początkowa. Spróbuj ponownie.")
        except ValueError:
            print("Wprowadź odpowiednią datę w formacie YYYY-MM-DD")
        return self.end_date(user_beginning_date)

    def size_choosing(self):
        print("Jakie biurko Cię interesuje?: ")
        print("Biurko 1-osobowe - wprowadź cyfrę 1")
        print("Biurko 4-osobowe - wprowadź cyfrę 4")
        print("Biurko 10-osobowe - wprowadź cyfrę 10")
        self.user_choice_size = input("Wprowadź swój wybór: ")
        if self.user_choice_size in ["1", "4", "10"]:
            return self.user_choice_size
        else:
            print("Wprowadzono niewłaściwą wartość, podaj wartość cyfrą: 1, 4 lub 10.")
        return self.size_choosing()

    def display_choosing(self):
        print("Czy interesuje Cię biurko z monitorem czy bez?")
        print("Biurko z monitorem - wprowadź cyfrę 1")
        print("Biurko bez monitora - wprowadź cyfrę 0")
        self.user_choice_display = input("Wprowadź swój wybór: ")
        if self.user_choice_display in ["0", "1"]:
            return self.user_choice_display
        else:
            print("Wprowadzono niewłaściwą wartość, podaj wartość 0 lub 1.")
        return self.display_choosing()

    def checking_availiability_by_date(self, user_beginning_date_str, user_end_date_str, filename='user_data.json'):
        with open(filename, 'r') as file:
            data = json.load(file)

        user_beginning_date = datetime.strptime(user_beginning_date_str, "%Y-%m-%d")
        user_end_date = datetime.strptime(user_end_date_str, "%Y-%m-%d")

        reserved_desks = []

        for id_reservation, reservation_spec in data.items():
            reservation_start = datetime.strptime(reservation_spec['Wynajem od'], "%Y-%m-%d")
            reservation_end = datetime.strptime(reservation_spec['Wynajem do'], "%Y-%m-%d")

            if not (user_end_date <= reservation_start or user_beginning_date >= reservation_end):
                reserved_desks.append(reservation_spec['Biurko'])
        return reserved_desks


    def showing_desk(self, reserved_desks, user_choice_size, user_choice_display):
        desks_instances = load_desks_from_file(filename="desks.json")

        if reserved_desks is None:
            reserved_desks = []

        for idx, desk_info in desks_instances.items():
            if idx not in reserved_desks and (int(self.user_choice_size) == desk_info.size and int(
                    self.user_choice_display) == desk_info.monitor):
                print(f"Numer biurka: {idx}:")
                print(f"Specyfikacja: {desk_info.desk_type}, "
                      f"\nCena za jedno stanowisko: {desk_info.price} PLN")
                if desk_info.size > 1:
                    print(f"Całkowita cena wynajmu biurka (za 1 dzień): {desk_info.price * desk_info.size}")
                print("")
            else:
                continue
        print("Oto lista dostępnych biurek.")
        self.user_desk_choice = input("Wprowadź numer wybranego przez siebie biurka: ")
        return self.user_desk_choice


    def choosing_desk_from_displayed(self, user_desk_choice, days_counter):
        desks_instances = load_desks_from_file(filename="desks.json")
        for desk_name, desk_info in desks_instances.items():
            if desk_name == user_desk_choice:
                print(f"Numer biurka: {desk_name}:")
                print(f"Specyfikacja: {desk_info.desk_type}, "
                      f"\nCena za jedno stanowisko: {desk_info.price} PLN")
                self.total_cost = desk_info.price * desk_info.size * days_counter
                print("")
                return self.total_cost, desk_name, desk_info.desk_type

    def value_calculating(self, total_cost):
        total_value = total_cost
        print(f"Całkowita cena wynajmu wyniesie {total_value} PLN.")
        return total_value

class User_Input:
    def choosing_desk_from_displayed(self, user_desk_choice, days_counter):
        desks_instances = load_desks_from_file(filename="desks.json")
        for desk_name, desk_info in desks_instances.items():
            if desk_name == user_desk_choice:
                print(f"Numer biurka: {desk_name}:")
                print(f"Specyfikacja: {desk_info.desk_type}, "
                      f"\nCena za jedno stanowisko: {desk_info.price} PLN")
                self.total_cost = desk_info.price * desk_info.size * days_counter
                print("")
                return self.total_cost, desk_name, desk_info.desk_type

    def value_calculating(self, total_cost):
        total_value = total_cost
        print(f"Całkowita cena wynajmu wyniesie {total_value} PLN.")
        return total_value


class ReservationCanceler:
    # @staticmethod
    def cancel_reservation():
        reservation_id = input("Podaj numer rezerwacji do odwołania: ")
        phone = input("Podaj numer telefonu podany przy rezerwacji: ")

        try:
            with open('user_data.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nie znaleziono danych rezerwacji.")
            return

        reservation = data.get(reservation_id)
        if reservation and reservation['Telefon'] == phone:
            del data[reservation_id]
            with open('user_data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Rezerwacja numer {reservation_id} została odwołana.")
        else:
            print("Nie znaleziono rezerwacji pasującej do podanych danych.")


class ClientDataManager:

    def confirming_imputed_data(self, desk_name, desk_type, user_beginning_date_str, user_end_date_str, total_value):
        accepting_order = input("Potwierdź czy powyższe informacje się zgadzają (tak lub nie): ")
        if accepting_order.lower() == 'tak':
            print("Potwierdzono")
            name, surname, phone, email = self.user_data_input()
            reservation_id = self.saving_clients_data(name, surname, phone, email, desk_name, desk_type,
                                                      user_beginning_date_str, user_end_date_str, total_value)
            print(f"Zapisano pomyślnie dane.")
            print(f"Twoj numer rezerwacji to: {reservation_id}, który został przypisany do numeru telefonu: {phone}")
            return reservation_id
        elif accepting_order.lower() == 'nie':
            print("Nie potwierdzono")
        else:
            print("Wprowadzono niewłaściwą odpowiedź, wprowadź odpowiedź tak lub nie")

        confirming_imputed_data(self, desk_name, desk_type, user_beginning_date_str, user_end_date_str, total_value)
        print("Do widzenia")

    def user_data_input(self):
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

    def saving_clients_data(self, name, surname, phone, email, desk_name, desk_type,
                            user_beginning_date_str, user_end_date_str, total_value):
        try:
            with open('user_data.json', 'r') as file:
                data = json.load(file)
                reservation_id = max([int(k) for k in data.keys()]) + 1 if data else 1
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            reservation_id = 1

        data[str(reservation_id)] = {
            "Imie": name,
            "Nazwisko": surname,
            "Telefon": phone,
            "Email": email,
            "Biurko": desk_name,
            "Specyfikacja": desk_type,
            "Wynajem od": user_beginning_date_str,
            "Wynajem do": user_end_date_str,
            "Calkowita wartosc wynajmu": total_value
        }

        with open('user_data.json', 'w') as file:
            json.dump(data, file, indent=4, sort_keys=False)

        return reservation_id


class ReservationSystem:
    def __init__(self):
        self.run()

    def run(self):
        while True:
            print("1. Dokonaj rezerwacji")
            print("2. Odwołaj rezerwację")
            print("3. Wyjdź")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                ReservationManager()
                ClientDataManager()
            elif choice == "2":
                ReservationCanceler.cancel_reservation()
            elif choice == "3":
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    ReservationSystem()
