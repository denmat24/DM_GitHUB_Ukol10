from typing import List
"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        # Inicializace objektu Person
        self.name = name
        self.surname = surname
        self.age = age
        self._vehicle_count = 0  # atribut sleduje počet vozidel osoby

    def __eq__(self, other: 'Person') -> bool:
        # Porovnání-dva objekty Person podle jména, příjmení a věku
        return (self.name == other.name and
                self.surname == other.surname and
                self.age == other.age)

    def get_vehicle_count(self) -> int:
        # Vrací počet vozidel, které osoba vlastní
        return self._vehicle_count

    def plus_vehicle_count(self):
        # Zvyšuje počet vozidel vlastněných osobou o 1
        self._vehicle_count += 1

    def minus_vehicle_count(self):
        # Snižuje počet vozidel vlastněných osobou o 1
        self._vehicle_count -= 1


class Vehicle:
    def __init__(self, registration_plate: str, creation_date: str, owner: Person) -> None:
        # Inicializace objektu Vehicle
        self.registration_plate = registration_plate
        self.creation_date = creation_date
        self.owner = owner

    def __eq__(self, other: 'Vehicle') -> bool:
        # Porovnává - dvě vozidla podle registrační značky
        return self.registration_plate == other.registration_plate


class Register:
    def __init__(self) -> None:
        # Registr vozidel a vlastníků
        self.vehicles = []  # Seznam všech registrovaných vozidel
        self.owners = []    # Seznam všech registrovaných vlastníků

    def find_owner(self, owner: Person) -> Person:
        # Hledání vlastníka v registru
        for o in self.owners:
            if o == owner:
                return o
        return None

    def find_vehicle(self, registration_plate: str) -> Vehicle:
        # Hhledání vozidla v registru podle registrační značky
        for v in self.vehicles:
            if v.registration_plate == registration_plate:
                return v
        return None

    def insert_vehicle(self, vehicle: Vehicle) -> int:
        # Vložení nového vozidla do registru, pokud ještě neexistuje

        if self.find_vehicle(vehicle.registration_plate):
            return 0  # Existuje -> vložení je přerušeno

        # Kontrola zda vlastník vozidla už existuje v registru
        owner = self.find_owner(vehicle.owner)

        if not owner:
            # Přidání nového vlastníka, pokud tam ještě není
            self.owners.append(vehicle.owner)
            owner = vehicle.owner
        else:
            # Nastavení existujícího vlastníka jako vlastníka vozidla
            vehicle.owner = owner

        # zvýšení početu vozidel pro vlastníka a přidání vozidla do seznamu vozidel
        owner.plus_vehicle_count()
        self.vehicles.append(vehicle)
        return 1

    def update_vehicle_owner(self, registration_plate: str, new_owner: Person) -> int:
        # Aktualizace vlastníka vozidla, pokud vozidlo existuje a nový vlastník je jiný než původní
        vehicle = self.find_vehicle(registration_plate)
        if not vehicle or vehicle.owner == new_owner:
            return 0  # pokud vozidlo neexistuje nebo je nový vlastník stejný -> žádná aktualizace

        # Snížení početu vozidel u starého vlastníka a pokud nemá další vozidla, odstranění z registru

        old_owner = vehicle.owner
        old_owner.minus_vehicle_count()
        if old_owner.get_vehicle_count() == 0:
            self.owners.remove(old_owner)

        # nový vlastník do registru a nastavení vlastníka vozidla
        existing_new_owner = self.find_owner(new_owner)
        if existing_new_owner:
            vehicle.owner = existing_new_owner
        else:
            self.owners.append(new_owner)
            vehicle.owner = new_owner

        # Zvyšení početu vozidel u nového vlastníka
        vehicle.owner.plus_vehicle_count()
        return 1

    def delete_vehicle(self, registration_plate: str) -> int:
        # Smaže vozidlo z registru, pokud existuje
        vehicle = self.find_vehicle(registration_plate)
        if not vehicle:
            return 0  # Vozidlo neexistuje->přerušení

        # Snížení početu vozidel u vlastníka vozidla a pokud nemá další vozidla, odstranění z registru
        owner = vehicle.owner
        owner.minus_vehicle_count()
        if owner.get_vehicle_count() == 0:
            self.owners.remove(owner)

        # Odstranění vozidla z registru
        self.vehicles.remove(vehicle)
        return 1

    def list_vehicles(self) -> List[Vehicle]:
        # seznam všech registrovaných vozidel v pořadí, jak byla přidána
        return self.vehicles

    def list_owners(self) -> List[Person]:
        # seznam všech registrovaných vlastníků v pořadí, jak byli přidáni
        return self.owners

    def list_vehicle_by_owner(self, owner: Person) -> List[Vehicle]:
        #  seznam vozidel konkrétního vlastníka v pořadí, jak byla přidána
        return [vehicle for vehicle in self.vehicles if vehicle.owner == owner]

"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


register = Register()

person1 = Person("John", "Doe", 20)
person2 = Person("Alice", "Doe", 22)

car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)

# car1 = Vehicle("abc", "20221122", person1)

# test insertion
assert register.insert_vehicle(car1) == 1
assert register.insert_vehicle(car2) == 1
assert register.insert_vehicle(car3) == 0
assert register.insert_vehicle(car4) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 2 and register.list_owners()[1].get_vehicle_count() == 1

# test update
assert register.update_vehicle_owner("abc1", person1) == 0
assert register.update_vehicle_owner("not in register", person1) == 0
assert register.update_vehicle_owner("abc1", person2) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 1 and register.list_owners()[1].get_vehicle_count() == 2
assert register.update_vehicle_owner("abc0", person2) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person2), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 3

# test delete
assert register.delete_vehicle("not in register") == 0
assert register.delete_vehicle("abc0") == 1
assert register.delete_vehicle("abc1") == 1
assert register.delete_vehicle("xyz") == 1
assert register.list_vehicles() == []
assert register.list_owners() == []

# test lists
car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)

register.insert_vehicle(car1)
register.insert_vehicle(car2)
register.insert_vehicle(car3)
register.insert_vehicle(car4)

assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)]
assert register.list_vehicle_by_owner(person1) == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1)]
