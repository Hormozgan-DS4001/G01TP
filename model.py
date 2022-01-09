from data_structure import Sll, HashTable, HashTableCamera, Trie, BST
import time


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
        self.enter_smart = False
        self.smart_list = BST()

    def make_smart(self, camera: "Camera", minimum_speed):
        self.enter_smart = True
        cam = SmartCamera(camera, minimum_speed)
        self.smart_list.insert(cam, camera.code)

    def check_smart(self, car: "Car"):
        if not car.check_smart:
            return
        key = car.check_smart.code
        res = self.smart_list.find(key)
        if car.check_smart and res:
            if time.time() - car.start_time > res.minimum_speed:
                car.add_violation(3)
                return 3
            car.off_smart()

        if self.enter_smart:
            car.on_smart(self)

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


class SmartCamera:
    def __init__(self, camera: Camera, minimum_speed: int):
        self.camera = camera
        self.minimum_speed = minimum_speed

    def re_code(self):
        return self.camera.code


class Model:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, model: Model, name_owner, national_code, heavy, tag, steal=False):
        self.model = model
        self.name_owner = name_owner
        self.national_code = national_code
        self.heavy = heavy
        self.tag = tag
        self.steal = steal
        self.check_smart = None
        self.violations = Sll()
        self.start_time = 0

    def check_steal(self):
        return self.steal

    def steal_car(self, steal):
        self.steal = steal

    def on_smart(self, camera: Camera):
        self.check_smart = camera
        self.start_time = time.time()

    def off_smart(self):
        self.check_smart = None
        self.start_time = 0

    def heavy(self):
        if self.heavy:
            return True

    def add_violation(self, violation):
        self.violations.append(violation)


class Core:
    def __init__(self):
        self.car_list = Trie()
        self.camera_list_name = Trie()
        self.camera_code_list = HashTableCamera()

    def add_car(self, model_name, name_owner, national_code, heavy, tag, steal=False):
        model = Model(model_name)
        car = Car(model, name_owner, national_code, heavy, tag, steal)
        self.car_list.insert(name_owner, car)
        self.car_list.insert(national_code, car)
        self.car_list.insert(tag, car)

    def add_camera(self, name: str, address: str, code: int, out, max_speed_truck: int = None,
                   max_speed_car: int = None, min_speed: int = None):
        cam = Camera(name, address, code, out, max_speed_truck, max_speed_car, min_speed)
        self.camera_list_name.insert(name, cam)
        self.camera_code_list[code] = cam

    @staticmethod
    def make_smart(enter_camera: Camera, exit_camera: Camera, max_speed):
        enter_camera.make_smart(exit_camera, max_speed)

    def check_violation(self, camera_code, car_tag, speed):
        car_tag = car_tag[:2] + car_tag[3] + car_tag[5:]
        cam = self.camera_code_list[camera_code]
        car = self.car_list.find_exact(car_tag)
        cam.check_smart(car)
        cam.check_speed(car, speed)
        if cam.enter_smart:
            car.on_smart(cam)

    def search_car(self, name: str = None, national_code: str = None, tag: str = None):
        if name:
            return self.car_list.find_prefix(name)
        if national_code:
            return self.car_list.find_prefix(national_code)
        if tag:
            return self.car_list.find_prefix(tag)

    def search_camera(self, name: str = None, code: int = None):
        if name:
            return self.camera_list_name.find_prefix(name)
        if code:
            return self.camera_code_list[code]

    def show_all_car(self):
        return self.car_list.find_prefix("")

    def show_add_camera(self):
        return self.car_list.find_prefix("")
















