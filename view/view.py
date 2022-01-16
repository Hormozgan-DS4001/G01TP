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

        self.treeview_car = ttk.Treeview(lbl_frame, show="headings", selectmode="browse")

    def search_camera(self):
        pass

    def add_camera(self):
        pass


















