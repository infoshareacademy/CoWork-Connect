import json

def saving_clients_data(desk_name, date, user_hours_choice, name, surname, phone, email):
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
            reservation_id = data[-1]["ID rezerwacji"] + 1 if data else 1
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        reservation_id = 1
    new_entry = {
        "ID rezerwacji": reservation_id,
        "Biurko": desk_name,
        "Data wynajmu": date,
        "Długość wynajmu": user_hours_choice,
        "Imię": name,
        "Nazwisko": surname,
        "Telefon": phone,
        "Email": email
    }
    data.append(new_entry)

    with open('user_data.json', 'w') as file:
        json.dump(data, file, indent=4)

    return reservation_id

if __name__ == '__main__':
    saving_clients_data()