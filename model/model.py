from data_structure.data_structure import Sll, HashTableCamera, Trie, BST, Dll
import datetime


class Camera:
    def __init__(self, name: str, address: str, code: int, out=False, max_speed_truck: int = None,
                 max_speed_car: int = None, min_speed: int = None):
        self.name = name
        self.address = address
        self.code = code
        self.out = out
        self.max_speed_truck = max_speed_truck
        self.max_speed_car = max_speed_car
        self.min_speed = min_speed
        self.enter_smart = False
        self.time_from = None
        self.time_to = None
        self.smart_list = BST()

    def set_time(self, hour_from, minutes_from, hour_to, minutes_to):
        self.time_from = datetime.timedelta(hours=float(hour_from), minutes=float(minutes_from))
        self.time_to = datetime.timedelta(hours=float(hour_to), minutes=float(minutes_to))

    def make_smart(self, camera, hour, minute, second):
        self.enter_smart = True
        minimum_speed = datetime.timedelta(hours=float(hour), minutes=float(minute), seconds=float(second))
        cam = SmartCamera(self, minimum_speed)
        camera.smart_list.insert(cam, self.code)

    def check_smart(self, car):
        res = self.smart_list.find(car.check_smart.code)
        if res:
            now = datetime.timedelta(hours=float(datetime.datetime.now().hour),
                                     minutes=float(datetime.datetime.now().minute),
                                     seconds=float(datetime.datetime.now().second))
            if now - car.start_time < res.minimum_speed:
                car.add_violation(3)
                return 3
            car.off_smart()

    def time_check(self, car):
        res = datetime.timedelta(hours=float(datetime.datetime.now().hour),
                                 minutes=float(datetime.datetime.now().minute))
        fro = self.time_from
        to = self.time_to
        if fro < res < to:
            car.add_violation(5)
            return 5

    def check_speed(self, car, speed):
        if car.heavy and self.max_speed_truck:
            if speed > self.max_speed_truck:
                car.add_violation(1)
                return 1
        if not car.heavy and self.max_speed_car:
            if speed > self.max_speed_car:
                car.add_violation(1)
                return 1
        if self.min_speed and speed < self.min_speed:
            car.add_violation(2)
            return 2


class SmartCamera:
    def __init__(self, camera: Camera, minimum_speed):
        self.camera = camera
        self.minimum_speed = minimum_speed


class Model:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, model: Model, name_owner, national_code, tag, heavy: bool = False):
        self.model = model
        self.name_owner = name_owner
        self.national_code = national_code
        self.heavy = heavy
        self.tag = tag
        self.steal = False
        self.check_smart = None
        self.violations = Sll()
        self.start_time = datetime.timedelta(hours=float(0), minutes=float(0), seconds=float(0))

    def check_steal(self):
        return self.steal

    def steal_car(self, steal):
        self.steal = steal

    def on_smart(self, camera: Camera):
        self.check_smart = camera
        self.start_time = datetime.timedelta(hours=float(datetime.datetime.now().hour),
                                             minutes=float(datetime.datetime.now().minute),
                                             seconds=float(datetime.datetime.now().second))

    def off_smart(self):
        self.check_smart = None
        self.start_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

    def show_violation(self):
        return self.violations

    def add_violation(self, violation):
        self.violations.append(violation)


class Core:
    def __init__(self):
        self.car_list = Trie()
        self.camera_list_name = Trie()
        self.model_list = Trie()
        self.camera_code_list = HashTableCamera()
        self.steal_cars = Dll()

    def add_car(self, model_name, name_owner, national_code, tag, heavy):
        nat_code = self.car_list.find_exact(national_code)
        ta = self.car_list.find_exact(tag)
        if nat_code:
            return 0
        if ta:
            return 1
        model = self.model_list.find_exact(model_name)
        car = Car(model, name_owner, national_code, tag, heavy)
        self.car_list.insert("*" + name_owner, car)
        self.car_list.insert(national_code, car)
        self.car_list.insert(tag, car)

    def show_steal(self):
        if len(self.steal_cars) == 0:
            return
        return self.steal_cars.get_node_handler(0)

    def add_steal(self, car: Car):
        self.steal_cars.append(car)

    def add_camera(self, name: str, address: str, code: int, out, max_speed_truck: int = None,
                   max_speed_car: int = None, min_speed: int = None):
        if self.camera_code_list[code]:
            return 0
        cam = Camera(name, address, code, out, max_speed_truck, max_speed_car, min_speed)
        self.camera_list_name.insert(name, cam)
        self.camera_code_list[code] = cam
        return cam

    def check_violation(self, camera_code, car_tag, speed):
        car_tag = car_tag[:2] + car_tag[3:5] + car_tag[6:9] + car_tag[10:]
        cam = self.camera_code_list[camera_code]
        car = self.car_list.find_exact(car_tag)
        if car.check_steal():
            yield 4
        yield cam.check_speed(car, speed)
        if not cam.out and car.heavy:
            yield cam.time_check(car)
        if car.check_smart:
            yield cam.check_smart(car)
        if cam.enter_smart:
            car.on_smart(cam)

    def search_camera(self, name: str = None, code: int = None):
        if name:
            return self.camera_list_name.find_prefix(name)
        if code:
            return self.camera_code_list[code]

    def search_car(self, name_owner: str = None, national_code: str = None, tag: str = None):
        if name_owner:
            return self.car_list.find_prefix(f"*{name_owner}")
        if national_code:
            return self.car_list.find_prefix(national_code)
        if tag:
            return self.car_list.find_prefix(tag)

    def show_all_car(self, text: str = "*"):
        return self.car_list.find_prefix(text)

    def show_all_camera(self, text: str = ""):
        return self.camera_list_name.find_prefix(text)

    def show_model(self):
        return self.model_list

    def add_model(self, name):
        model = Model(name)
        self.model_list.insert(name, model)

    def all_violation(self):
        list_car_full = Sll()
        for car in self.car_list.find_prefix("*"):
            if len(car.violations) == 0:
                list_car_full.append(car)

        for i in list_car_full:
            print(i.name_owner)
