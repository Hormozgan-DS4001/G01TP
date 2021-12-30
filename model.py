

class Camera:
    def __init__(self, name: str, address: str, code: int, out: bool, max_speed_truck: int = None,
                 max_speed_car: int = None, min_speed: int = None):
        self.name = name
        self.address = address
        self.code = code
        self.out = out
        self.max_speed_truck = max_speed_truck
        self.max_speed_car = max_speed_car
        self.min_speed = min_speed


class Car:
    def __init__(self):
        pass


class Core:
    def __init__(self):
        pass


