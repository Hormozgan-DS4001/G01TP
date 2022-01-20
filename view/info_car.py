from configure.configure import Button, Frame, Radiobutton, LabelFrame, Label
from tkinter import ttk


class CarInfo(Frame):
    def __init__(self, obj_car, callback_change_steal, callback_violations, close):
        super(CarInfo, self).__init__()
        self.obj_car = obj_car
        self.callback_violations = callback_violations
        self.callback_change_steal = callback_change_steal
        self.close = close

