from configure.configure import Button, Label, LabelFrame, Scale, Entry, Frame, Tk, TopLevel
from tkinter import messagebox, ttk, OptionMenu, StringVar
from data_structure import Dll
from add_car import AddCar
from add_camera import AddCamera
from info_car import CarInfo


class Manager(Tk):
    def __init__(self, callback_cam_list, callback_car_list, callback_add_car, callback_add_camera,
                 callback_make_smart, callback_search_car, callback_search_camera, callback_check_violation,
                 callback_model_list, callback_change_steal):
        super(Manager, self).__init__()
        self.callback_cam_list = callback_cam_list
        self.callback_car_list = callback_car_list
        self.callback_add_car = callback_add_car
        self.callback_add_camera = callback_add_camera
        self.callback_make_smart = callback_make_smart
        self.callback_search_car = callback_search_car
        self.callback_search_camera = callback_search_camera
        self.callback_check_violation = callback_check_violation
        self.callback_model_list = callback_model_list
        self.callback_change_steal = callback_change_steal

        self.list_car = Dll()
        self.list_car_2 = []

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        tab_frame = Frame(self)
        tab_frame.grid(row=0, column=0)
        self.not_tab.add(tab_frame, text="Manager")
        lbl_frame = LabelFrame(tab_frame)
        lbl_frame.grid(row=0, column=0)

        self.tag_list = ["الف", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض",
                         "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"]

        Label(lbl_frame, text="Console").grid(row=0, column=0, columnspan=4)
        self.console = Frame(lbl_frame, height=200, width=1000, bg="#f5f3f4", highlightbackground="black",
                             highlightthickness=2)
        self.console.grid(row=1, column=0, columnspan=4, pady=5)

        frm_cam_search = LabelFrame(lbl_frame, text="Search Camera")
        frm_cam_search.grid(row=2, column=0, pady=5)
        Label(frm_cam_search, text="ID: ").grid(row=0, column=0, pady=5)
        self.ent_id_cam = Entry(frm_cam_search)
        self.ent_id_cam.grid(row=0, column=1, pady=5)
        Label(frm_cam_search, text="Name Camera: ").grid(row=1, column=0, pady=5)
        self.ent_nam_cam = Entry(frm_cam_search)
        self.ent_nam_cam.grid(row=1, column=1, pady=5)
        Button(frm_cam_search, text="Search Camera", command=self.search_camera).grid(row=2, column=1, pady=5)

        frm_btn = Frame(lbl_frame)
        frm_btn.grid(row=2, column=2)
        Button(frm_btn, text="Add Car", command=self.add_car).grid(row=0, column=0)
        Button(frm_btn, text="Add Camera", command=self.add_camera).grid(row=1, column=0)
        Button(frm_btn, text="Make Smart", command=self.make_smart).grid(row=2, column=0)

        self.treeview_cam = ttk.Treeview(lbl_frame, show="headings", selectmode="browse")
        self.treeview_cam["column"] = ("Name", "Id", "Max speed")
        self.treeview_cam.heading("Name", text="Name")
        self.treeview_cam.heading("Id", text="ID")
        self.treeview_cam.heading("Max speed", text="Max Speed")
        self.treeview_cam.grid(row=4, column=0, columnspan=3)
        frm_btn_ne = Frame(lbl_frame)
        frm_btn_ne.grid(row=5, column=0, columnspan=3)
        Button(frm_btn_ne, text="Prev", command=self.prev_cam).grid(row=0, column=1)
        Button(frm_btn_ne, text="Next", command=self.next_cam).grid(row=0, column=2)

        frm_car_search = LabelFrame(lbl_frame, text="Search Car")
        frm_car_search.grid(row=2, column=3, pady=5)
        frm_tag = LabelFrame(frm_car_search, text="TAG")
        frm_tag.grid(row=0, column=0, columnspan=4, pady=5)
        Label(frm_tag, text="Car Tag: ").grid(row=0, column=0, pady=5, padx=5)
        self.ent_fir_tag = Entry(frm_tag)
        self.ent_fir_tag.grid(row=0, column=1, pady=5, padx=10)
        self.str_var = StringVar()
        self.str_var.set(self.tag_list[0])
        opm = OptionMenu(frm_tag, self.str_var, *self.tag_list)
        opm.grid(row=0, column=2, padx=5)
        opm.configure(bg="#D3DBEB", activebackground="#CDD5E5", width=7)
        opm["menu"].config(bg="white")
        self.ent_tri_tag = Entry(frm_tag)
        self.ent_tri_tag.grid(row=0, column=3, padx=10)
        Label(frm_car_search, text="National Code: ").grid(row=1, column=0)
        self.nat_code = Entry(frm_car_search)
        self.nat_code.grid(row=1, column=1, pady=5, padx=5)
        Label(frm_car_search, text="Owner Name: ").grid(row=1, column=2, padx=5)
        self.owner_name = Entry(frm_car_search)
        self.owner_name.grid(row=1, column=3)
        Button(frm_car_search, text="Search Car", command=self.search_car).grid(row=2, column=1, pady=10)

        self.treeview_car = ttk.Treeview(lbl_frame, show="headings", selectmode="browse")
        self.treeview_car["column"] = ("name owner", "national code", "car tag", "model")
        self.treeview_car.heading("name owner", text="Name Owner")
        self.treeview_car.heading("national code", text="National Code")
        self.treeview_car.heading("car tag", text="Car Tag")
        self.treeview_car.heading("model", text="Model")
        self.treeview_car.grid(row=4, column=3, padx=5)
        self.treeview_car.bind("<Double-1>", self.detail_car)
        frm_bt_ne = Frame(lbl_frame)
        frm_bt_ne.grid(row=5, column=3)
        Button(frm_bt_ne, text="Prev", command=self.prev_car).grid(row=0, column=1)
        Button(frm_bt_ne, text="Next", command=self.next_car).grid(row=0, column=2)

    def add_car(self):
        panel = AddCar(self.callback_add_car, self.tag_list, self.callback_model_list, self.close)
        self.not_tab.add(panel, text="New Car")
        self.not_tab.select(panel)

    def add_camera(self):
        panel = AddCamera(self.callback_add_camera, self.close)
        self.not_tab.add(panel, text="New Camera")
        self.not_tab.select(panel)

    def search_camera(self):
        pass

    def search_car(self):
        pass

    def make_smart(self):
        pass

    def detail_car(self, event):
        if self.treeview_car.selection() == ():
            return
        item = self.treeview_car.identify("item", event.x, event.y)
        ID = self.treeview_car.item(item)["text"]
        res = self.list_car_2[int(ID)]
        panel = CarInfo(res, self.tag_list, self.close)
        self.not_tab.add(panel, text=f"Info {res.model.name}")
        self.not_tab.select(panel)

    def prev_cam(self):
        pass

    def next_cam(self):
        pass

    def prev_car(self):
        pass

    def next_car(self):
        pass

    def close(self):
        self.not_tab.hide(self.not_tab.select())


m1 = Manager(2, 2, 2, 23, 2, 23, 32, 3, 52, 343)
m1.mainloop()







