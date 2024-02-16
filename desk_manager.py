from desk import load_desks_from_file, Desks, save_desks_to_file
import json


class DeskManager:

    def __init__(self):
        self.desks_instances = load_desks_from_file("desks.json")
        self.desk = Desks(
            idx=self.add_idx(),
            name=self.add_name(),
            desk_type=self.add_desk_type(),
            monitor=self.add_monitor_options(),
            size=self.add_rozmiar(),
            price=self.add_price(),
            status=self.add_status(),
        )

    def add_idx(self):
        # Automatyczne nadawanie indeksu
        return len(self.desks_instances.keys()) + 1

    def add_name(self):
        # Podanie nazwy biurka
        return input("Podaj nazwę biurka: ")

    def add_desk_type(self):
        # Podanie typu biurka
        return input("Podaj typ biurka: ")

    def add_monitor_options(self):
        # Walidacja monitora
        while True:
            try:
                monitor_input = input(f"Czy biurko ma monitor? 0 - nie, 1 - tak: ")
                monitor_choice = bool(int(monitor_input))
                break
            except ValueError:
                print("Błąd: Wprowadź cyfrę 0 lub 1, aby wybrać opcję.")
        return monitor_choice

    def add_rozmiar(self):
        # Walidacja rozmiaru
        while True:
            try:
                size = int(input("Podaj rozmiar biurka: "))
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę całkowitą dla rozmiaru.")
        return size

    def add_price(self):
        # Walidacja ceny
        while True:
            try:
                price = float(input("Podaj cenę biurka PLN/h: "))
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę dla ceny.")
        return price

    def add_status(self):
        # Walidacja statusu
        status_options = {1: "czynne", 2: "zajęte", 3: "inne"}
        while True:
            status_options_string = ", ".join(
                f"{key}. / {value}" for key, value in status_options.items()
            )
            status = input(
                f"Podaj status biurka, wybierając odpowiednią opcję ({status_options_string}): "
            )
            if int(status) in status_options:
                break
            else:
                print("Błąd: Wprowadź prawidłowy status.")
        return status_options[int(status)]

    # Zapis do pliku wcześniej podanych danych
    def add_desk(self):
        self.desks_instances[self.desk.name] = self.desk
        print("Dodano biurko!")
        save_desks_to_file(self.desks_instances)

    def delete_desk():
        desks_instances = load_desks_from_file("desks.json")

        print("Akturalne biurka:")
        for desk in desks_instances.values():
            print(f"Id: {desk.name}, {json.dumps(desk.to_dict(), indent=2)} ")

        if not desks_instances:
            print("Brak dostępnych biurek do usunięcia!")
            return

        try:
            del_desk_name = input(
                "Podaj indeks biurka do usunięcia (lub wpisz -1, żeby anulować): "
            )

            if del_desk_name == "-1":
                print("Anulowano usunięcie.")
                return

            if del_desk_name in desks_instances:
                desks_instances.pop(del_desk_name)
                print(f"Usunięto biurko: {del_desk_name}")

            else:
                print("Nieprawidłowa nazwa biurka. Nie usunięto żadnego biurka.")

            save_desks_to_file(desks_instances)

        except ValueError:
            print("Nieprawidłowe dane wejściowe. Podaj prawidłową nazwę biurka.")

    def show_all_desks(self):
        for desk in self.desks_instances.values():
            print(desk.user_friendly_dict())
