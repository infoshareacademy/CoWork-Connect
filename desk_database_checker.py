import json

def reading_database(filename='desks.json',size='', display=''):
    with open('desks.json', 'r') as file:
        data = json.load(file)

    for desk_name, desk_info in data.items():
        if size in desk_info['desk_type'] and display in desk_info['desk_type']:
            print(f"{desk_name}:")
            for key, value in desk_info.items():
                print(f"  {key}: {value}")


if __name__ == '__main__':
    reading_database()

def choosing_desk(user_desk_choice):
    with open('desks.json', 'r') as file:
        data = json.load(file)

    for desk_name, desk_info in data.items():
        if user_desk_choice in desk_name:
            print(f'{desk_name}')
            print(f'Specyfikacja: {desk_info["desk_type"]}')
            print(f'Cena: {desk_info["price"]} PLN za 1 miejsce')
            return int(desk_info["price"]), desk_name

if __name__ == '__main__':
    choosing_desk()

