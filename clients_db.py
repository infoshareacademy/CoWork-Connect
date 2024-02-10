import json

def saving_clients_data(desk_name, user_beginning_date_str, user_end_date_str, name, surname, phone, email, total_value):
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
            # Generowanie nowego ID rezerwacji
            reservation_id = max([int(k) for k in data.keys()]) + 1 if data else 1
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        reservation_id = 1

    # Dodawanie nowej rezerwacji do słownika
    data[str(reservation_id)] = {
        "Biurko": desk_name,
        "Imie": name,
        "Nazwisko": surname,
        "Telefon": phone,
        "Email": email,
        "Wynajem od": user_beginning_date_str,
        "Wynajem do": user_end_date_str,
        "Calkowita wartosc wynajmu": total_value
    }

    with open('user_data.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

    return reservation_id

if __name__ == '__main__':
    saving_clients_data()