from configure import Button, Label, LabelFrame, Scale, Entry, Frame, Tk, TopLevel
from tkinter import messagebox, ttk


class Manager(Tk):
    def __init__(self, callback_cam_list, callback_car_list, callback_add_car, callback_add_camera,
                 callback_make_smart, callback_search_car, callback_search_camera):
        super(Manager, self).__init__()
        self.callback_cam_list = callback_cam_list
        self.callback_car_list = callback_car_list
        self.callback_add_car = callback_add_car
        self.callback_add_camera = callback_add_camera
        self.callback_make_smart = callback_make_smart
        self.callback_search_car = callback_search_car
        self.callback_search_camera = callback_search_camera

        self.list_car = []
        self.list_cam = []

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        tab_frame = Frame(self)
        tab_frame.grid(row=0, column=0)
        self.not_tab.add(tab_frame, text="Manager")
        lbl_frame = LabelFrame(tab_frame)
        lbl_frame.grid(row=0, column=0)






