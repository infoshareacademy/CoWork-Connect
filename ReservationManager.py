import json
from datetime import datetime
from desk import load_desks_from_file

class ReservationManager:
    def __init__(self, user_choice_size=None, user_choice_display=None, user_beginning_date_str=None, user_end_date_str=None,
                 desk_price=None, days_counter=None, size=None, desk_name=None, desk_type=None):
        self.user_choice_size = user_choice_size
        self.user_choice_display = user_choice_display
        self.user_beginning_date_str = user_beginning_date_str
        self.user_end_date_str = user_end_date_str
        self.desk_price = desk_price
        self.days_counter = days_counter
        self.size = size
        self.desk_name = desk_name
        self.desk_type = desk_type
    print("Za chwilę zaprezentuję listę dostepnych biurek.")

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


    def checking_availiability_by_date(self, filename='user_data.json'):
        with open(filename, 'r') as file:
            data = json.load(file)

        user_beginning_date = datetime.strptime(self.user_beginning_date_str, "%Y-%m-%d")
        user_end_date = datetime.strptime(self.user_end_date_str, "%Y-%m-%d")

        reserved_desks = []

        for id_reservation, reservation_spec in data.items():
            reservation_start = datetime.strptime(reservation_spec['Wynajem od'], "%Y-%m-%d")
            reservation_end = datetime.strptime(reservation_spec['Wynajem do'], "%Y-%m-%d")

            if not (user_end_date <= reservation_start or user_beginning_date >= reservation_end):
                reserved_desks.append(reservation_spec['Biurko'])
        return reserved_desks


    def showing_desk(self, reserved_desks):
        desks_instances = load_desks_from_file(filename="desks.json")

        if reserved_desks is None:
            reserved_desks = []

        for idx, desk_info in desks_instances.items():
            if idx not in reserved_desks and (int(self.user_choice_size) == desk_info.size and int(self.user_choice_display) == desk_info.monitor):
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
        for idx, desk_info in desks_instances.items():
            if idx == user_desk_choice:
                print(f"Numer biurka: {idx}:")
                print(f"Specyfikacja: {desk_info.desk_type}, "
                      f"\nCena za jedno stanowisko: {desk_info.price} PLN")
                if desk_info.size > 1:
                    print(f"Całkowita cena wynajmu biurka: {desk_info.price * desk_info.size * days_counter}")
                print("")

    def complete_reservation_process(self):
        user_beginning_date_str, user_beginning_date = self.beginning_date()
        user_end_date_str, user_end_date, days_counter = self.end_date(user_beginning_date)
        user_choice_size = self.size_choosing()
        user_choice_display = self.display_choosing()
        reserved_desks = self.checking_availiability_by_date(filename='user_data.json')
        user_desk_choice = self.showing_desk(reserved_desks)
        self.choosing_desk_from_displayed(user_desk_choice, days_counter)
        print("Rezerwacja zakończona sukcesem.")


manager = ReservationManager()
manager.complete_reservation_process()
