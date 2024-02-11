import json
from datetime import datetime


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


user_beginning_date_str, user_beginning_date = beginning_date()
user_end_date_str, user_end_date, days_counter = end_date(user_beginning_date)

def checking_availiability_by_date(filename='user_data.json', user_beginning_date_str='', user_end_date_str=''):
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


def choosing_desk_v2(exclude_desk_ids=None, size=None, display=None):
    with open('desks.json', 'r') as file:
        data = json.load(file)

    if exclude_desk_ids is None:
        exclude_desk_ids = []

    for desk_name, desk_info in data.items():
        if desk_name not in exclude_desk_ids and (size == desk_info['rozmiar'] and display == desk_info['monitor']):
            print(f"Numer biurka: {desk_name}:")
            print(f"Specyfikacja: {desk_info['desk_type']}, "
                  f"\nCena za jedno stanowisko: {desk_info['price']} PLN")
            if desk_info['rozmiar'] > 1:
                print(f"Całkowita cena wynajmu biurka: {desk_info['price'] * desk_info['rozmiar']}")
            print("")
        else:
            continue


if __name__ == "__main__":
    reserved_desks = checking_availiability_by_date(user_beginning_date_str='2024-02-10',
                                                    user_end_date_str='2024-02-15')
    choosing_desk_v2(exclude_desk_ids=reserved_desks, size=1, display=True)

