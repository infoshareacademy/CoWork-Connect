import json
class Desks:
    def __init__(self, idx, name, desk_type, monitor, size, price, status):
        self.idx = idx
        self.name = name
        self.desk_type = desk_type
        self.monitor = monitor
        self.size = size
        self.price = price
        self.status = status

    def __str__(self):
        return f"{self.idx}: {self.name} - {self.desk_type}  {self.price} PLN/h - {self.status}"

    def to_dict(self):
        return {
            "desk_type": self.desk_type,
            "monitor": self.monitor,
            "rozmiar": self.size,
            "price": self.price,
            "status": self.status,
            "name": self.name
        }



# Create instances for each entry in the dictionary
def load_desks_from_file():
    try:
        with open("desks.json", "r") as file:
            desks_data = json.load(file)

        desks_instances = {}
        for idx, (name, desk_data) in enumerate(desks_data.items(), start=1):
            desks_instances[name] = Desks(
                idx,
                name,
                desk_data["desk_type"],
                desk_data.get("monitor", None),
                desk_data.get("rozmiar", None),
                desk_data["price"],
                desk_data["status"]
            )

        return desks_instances

    except FileNotFoundError:
        print("Plik desks.json nie został znaleziony.")
        return {}
