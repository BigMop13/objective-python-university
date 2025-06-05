import random

class CardDeck():
    class Card:
        def __init__(self, type, value):
            self.type = type
            self.value = value

    def __init__(self):
        types = ['Kier', 'Karo', 'Trefl', 'Pik']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [self.Card(type, value) for type in types for value in values]

    def draw_a_single_card(self):
        if not self.cards:
            return None
        return self.cards.pop()
    
    def shuffle_the_deck(self):
        import random
        types = ['Kier', 'Karo', 'Trefl', 'Pik']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [self.Card(type, value) for type in types for value in values]
        random.shuffle(self.cards)

deck = CardDeck()
deck.shuffle_the_deck()
print(deck.draw_a_single_card())


class Vehicle:
    kolor = "biały"

    def __init__(self, max_speed=240, mileage=18):
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"({self.max_speed}, {self.mileage})"

    def oblicz_oplate(self, liczba_miejsc):
        return liczba_miejsc * 100


class Bus(Vehicle):
    def __init__(self, name, max_speed=180, mileage=12, total_capacity=50):
        super().__init__(max_speed, mileage)
        self.name = name
        self.total_capacity = total_capacity

    def __str__(self):
        return f"({self.name}, {self.max_speed}, {self.mileage})"

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.total_capacity} passengers"

    def oblicz_oplate(self, liczba_miejsc):
        base_fee = super().oblicz_oplate(liczba_miejsc)
        return base_fee * 1.1


class Samochod(Vehicle):
    def __init__(self, brand, model, max_speed=200, mileage=15, fuel_type="benzyna"):
        super().__init__(max_speed, mileage)
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def __str__(self):
        return f"({self.brand} {self.model}, {self.max_speed}, {self.mileage})"

    def get_fuel_info(self):
        return f"{self.brand} {self.model} uses {self.fuel_type}"


vehicle = Vehicle()
print("Vehicle:", vehicle)
print("Kolor pojazdu:", Vehicle.kolor)

bus = Bus("School Volvo")
print("Bus:", bus)
print("Kolor autobusu:", Bus.kolor)
print(bus.seating_capacity())
print("Opłata za autobus:", bus.oblicz_oplate(bus.total_capacity))

custom_bus = Bus("City Bus", 200, 15, 75)
print("Custom Bus:", custom_bus)
print(custom_bus.seating_capacity())
print("Opłata za custom autobus:", custom_bus.oblicz_oplate(custom_bus.total_capacity))

car = Samochod("Audi", "Q5", 240, 18)
print("Car:", car)
print("Kolor samochodu:", Samochod.kolor)
print(car.get_fuel_info())
print("Opłata za samochód:", car.oblicz_oplate(5))

custom_car = Samochod("BMW", "M3", 250, 12, "benzyna premium")
print("Custom Car:", custom_car)
print(custom_car.get_fuel_info())
print("Opłata za custom samochód:", custom_car.oblicz_oplate(5))
