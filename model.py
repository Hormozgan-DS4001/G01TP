from data_structure import Sll, HashTable, HashTableCamera, Trie


class Camera:
    def __init__(self, name: str, address: str, code: int, out, max_speed_truck: int = None,
                 max_speed_car: int = None, min_speed: int = None):
        self.name = name
        self.address = address
        self.code = code
        self.out = out
        self.max_speed_truck = max_speed_truck
        self.max_speed_car = max_speed_car
        self.min_speed = min_speed

    def check_speed(self, car: "Car", speed):
        if car.check_steal():
            return 4
        if car.heavy() and self.max_speed_truck:
            if speed > self.max_speed_truck:
                car.add_violation(1)
                return 1
        if not car.heavy() and self.max_speed_car:
            if speed > self.max_speed_car:
                car.add_violation(1)
                return 1


class Model:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, model: Model, name, national_code: int, heavy, tag: int, steal=False):
        self.model = model
        self.name = name
        self.national_code = national_code
        self.heavy = heavy
        self.tag = tag
        self.steal = steal
        self.violations = Sll()

    def check_steal(self):
        return self.steal

    def steal_car(self, steal):
        self.steal = steal

    def heavy(self):
        if self.heavy:
            return True

    def add_violation(self, violation):
        self.violations.append(violation)


class Core:
    def __init__(self):
        pass


