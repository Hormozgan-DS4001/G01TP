from configure.configure import Button, Frame, Radiobutton, LabelFrame, Label, Tk
from tkinter import ttk


class CarInfo(Tk):
    def __init__(self, obj_car, callback_change_steal, callback_violations, tag_list, close):
        super(CarInfo, self).__init__()
        self.obj_car = obj_car
        self.callback_violations = callback_violations
        self.callback_change_steal = callback_change_steal
        self.tag_list = tag_list
        self.close = close

        # if self.obj_car.steal:
        #     self.configure(bg="red")

        Label(self, text="Name Owner: ").grid(row=0, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.name_owner}", font=('Helvetica', 11)).grid(row=0, column=1, sticky="w",
                                                                                    padx=10)
        Label(self, text="National Code: ").grid(row=1, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.national_code}", font=('Helvetica', 11)).grid(row=1, column=1, sticky="w",
                                                                                       padx=10)
        Label(self, text="Model: ").grid(row=2, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.model}", font=('Helvetica', 11)).grid(row=2, column=1, sticky="w", padx=10)
        Label(self, text="Car Tag: ").grid(row=3, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.tag[:2]} {self.tag_list[int(self.obj_car.tag[2])]} {self.obj_car.tag[3:]}",
              font=('Helvetica', 11)).grid(row=3, column=1, sticky="w", padx=10)
        Label(self, text="Truck or Car: ").grid(row=4, column=0, sticky="w", pady=5)
        if self.obj_car.heavy:
            Label(self, text=f"Truck", font=('Helvetica', 11)).grid(row=4, column=1, sticky="w", padx=10)
        else:
            Label(self, text=f"Car", font=('Helvetica', 11)).grid(row=4, column=1, sticky="w", padx=10)











class Car:
    def __init__(self, model, name_owner, national_code, tag, heavy: bool = False):
        self.model = model
        self.name_owner = name_owner
        self.national_code = national_code
        self.heavy = heavy
        self.tag = tag
        self.steal = False
        self.check_smart = None
        self.violations = []
        self.start_time = 0



c = Car("pride", "kamand", "3480159222", "2541875", False)

m = CarInfo(c, "skdf", 542, ["a", "b", "c", "d", "e", "f"], 223513)
m.mainloop()














