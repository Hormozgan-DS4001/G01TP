from configure import Button, Label, LabelFrame, Scale, Entry, Frame, Tk, TopLevel
from tkinter import messagebox, ttk


class Manager(Tk):
    def __init__(self, callback_cam_list, callback_car_list, callback_add_car, callback_add_camera,
                 callback_make_smart, callback_search_car, callback_search_camera, callback_check_violation):
        super(Manager, self).__init__()
        self.callback_cam_list = callback_cam_list
        self.callback_car_list = callback_car_list
        self.callback_add_car = callback_add_car
        self.callback_add_camera = callback_add_camera
        self.callback_make_smart = callback_make_smart
        self.callback_search_car = callback_search_car
        self.callback_search_camera = callback_search_camera
        self.callback_check_violation = callback_check_violation

        self.list_car = []
        self.list_cam = []

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        tab_frame = Frame(self)
        tab_frame.grid(row=0, column=0)
        self.not_tab.add(tab_frame, text="Manager")
        lbl_frame = LabelFrame(tab_frame)
        lbl_frame.grid(row=0, column=0)

        tag_list = ["الف", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",
                    "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"]

        self.console = Frame(lbl_frame)
        self.console.grid(row=0, column=0, columnspan=1)

        frm_cam = Frame(lbl_frame)
        frm_cam.grid(row=1, column=0)
        Label(frm_cam, text="ID: ").grid(row=0, column=0)
        self.ent_id_cam = Entry(frm_cam)
        self.ent_id_cam.grid(row=0, column=1)
        Label(frm_cam, text="Name Camera: ").grid(row=1, column=0)
        self.ent_nam_cam = Entry(frm_cam)
        self.ent_nam_cam.grid(row=1, column=1)
        Button(frm_cam, text="Search Camera", command=self.search_camera).grid(row=2, column=0)
        Button(frm_cam, text="Add Camera", command=self.add_camera).grid(row=2, column=1)
        Button(frm_cam, text="Make Smart", command=self.make_smart).grid(row=2, column=3)
        self.treeview_cam = ttk.Treeview(lbl_frame, show="headings", selectmode="browse")
        self.treeview_cam["column"] = ("Name", "Id", "Max speed")
        self.treeview_cam.heading("Name", text="Name")
        self.treeview_cam.heading("Id", text="ID")
        self.treeview_cam.heading("Max speed", text="Max Speed")
        self.treeview_cam.grid(row=3, column=0, columnspan=3)

        frm_car = Frame(self)
        frm_car.grid(row=1, column=1)





    def search_camera(self):
        pass

    def add_camera(self):
        pass

    def make_smart(self):
        pass


















