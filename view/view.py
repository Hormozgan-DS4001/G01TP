from tkinter import messagebox, ttk, OptionMenu, StringVar, Canvas, Listbox, Scrollbar
from add_camera import AddCamera
from add_car import AddCar
from info_car import CarInfo
from make_smart import MakeSmart
from add_model import AddModel
from configure.configure import Button, Label, LabelFrame, Entry, Frame, Tk


class Manager(Tk):
    def __init__(self, callback_cam_list, callback_car_list, callback_add_car, callback_add_camera,
                 callback_add_model, callback_search_camera, callback_check_violation,
                 callback_model_list, callback_list_steal, callback_add_steal, callback_search_car):
        super(Manager, self).__init__()
        self.callback_cam_list = callback_cam_list
        self.callback_add_car = callback_add_car
        self.callback_add_camera = callback_add_camera
        self.callback_search_camera = callback_search_camera
        self.callback_model_list = callback_model_list
        self.callback_add_mode = callback_add_model
        self.callback_add_steal = callback_add_steal
        self.callback_search_car = callback_search_car
        self.callback_check_violation = callback_check_violation
        self.item = 9
        self.method_steal = callback_list_steal
        self.end_steal = self.method_steal()
        self.start_steal = self.method_steal()
        self.list_steal = []

        self.method_car = callback_car_list
        self.callback_car_list = self.method_car()
        self.index_car = 0
        self.list_car = []

        self.method_cam = callback_cam_list
        self.callback_cam_list = self.method_cam()
        self.index_cam = 0
        self.list_cam = []

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
        lbl_box = Frame(lbl_frame)
        lbl_box.grid(row=1, column=0, columnspan=4)
        self.l_box = Listbox(lbl_box, width=100)
        self.l_box.pack(side="left", fill="both")
        s1 = Scrollbar(lbl_box)
        s1.pack(side="right", fill="both")
        self.l_box.configure(yscrollcommand=s1.set)
        s1.configure(command=self.l_box.yview)

        frm_cam_search = LabelFrame(lbl_frame, text="Search Camera")
        frm_cam_search.grid(row=2, column=0, pady=5)
        Label(frm_cam_search, text="ID: ").grid(row=0, column=0, pady=5)
        self.ent_id_cam = Entry(frm_cam_search)
        self.ent_id_cam.grid(row=0, column=1, pady=5)
        Label(frm_cam_search, text="Name Camera: ").grid(row=1, column=0, pady=5)
        self.ent_nam_cam = Entry(frm_cam_search)
        self.ent_nam_cam.grid(row=1, column=1, pady=5)
        Button(frm_cam_search, text="Search Camera", command=self.search_camera).grid(row=2, column=0, pady=5)
        Button(frm_cam_search, text="Show All", command=self.refresh_camera).grid(row=2, column=1, pady=5)

        frm_btn = Frame(lbl_frame)
        frm_btn.grid(row=2, column=2)
        Button(frm_btn, text="Add Car", command=self.add_car).grid(row=0, column=0)
        Button(frm_btn, text="Add Camera", command=self.add_camera).grid(row=1, column=0)
        Button(frm_btn, text="Make Smart", command=self.make_smart).grid(row=2, column=0)
        Button(frm_btn, text="Add Model", command=self.add_model).grid(row=3, column=0)

        self.treeview_cam = ttk.Treeview(lbl_frame, show="headings", selectmode="browse")
        self.treeview_cam["column"] = ("Name", "Id", "Max speed")
        self.treeview_cam.heading("Name", text="Name")
        self.treeview_cam.heading("Id", text="ID")
        self.treeview_cam.heading("Max speed", text="Max Speed")
        self.treeview_cam.grid(row=4, column=0, columnspan=3)
        frm_btn_ne = Frame(lbl_frame)
        frm_btn_ne.grid(row=5, column=0, columnspan=3)
        Button(frm_btn_ne, text="Show More", command=self.show_more_cam).grid(row=0, column=2)

        frm_car_search = LabelFrame(lbl_frame, text="Search Car")
        frm_car_search.grid(row=2, column=3, pady=5)
        frm_tag = LabelFrame(frm_car_search, text="TAG")
        frm_tag.grid(row=0, column=0, columnspan=4, pady=5)
        Label(frm_tag, text="Car Tag: ").grid(row=0, column=0, pady=5, padx=5)
        self.ent_fir_tag = Entry(frm_tag, width=6)
        self.ent_fir_tag.grid(row=0, column=1, pady=5, padx=10)
        self.str_var = StringVar()
        self.str_var.set(self.tag_list[0])
        opm = OptionMenu(frm_tag, self.str_var, *self.tag_list)
        opm.grid(row=0, column=2, padx=5)
        opm.configure(bg="#D3DBEB", activebackground="#CDD5E5", width=7)
        opm["menu"].config(bg="white")
        self.ent_tri_tag = Entry(frm_tag, width=10)
        self.ent_tri_tag.grid(row=0, column=3, padx=10)
        self.ent_for_tag = Entry(frm_tag, width=6)
        self.ent_for_tag.grid(row=0, column=4, padx=10)
        Label(frm_car_search, text="National Code: ").grid(row=1, column=0)
        self.nat_code = Entry(frm_car_search)
        self.nat_code.grid(row=1, column=1, pady=5, padx=5)
        Label(frm_car_search, text="Owner Name: ").grid(row=1, column=2, padx=5, sticky="E")
        self.owner_name = Entry(frm_car_search)
        self.owner_name.grid(row=1, column=3)
        Button(frm_car_search, text="Search Car", command=self.search_car).grid(row=2, column=1, pady=10)
        Button(frm_car_search, text="Show All", command=self.refresh_car).grid(row=2, column=2, pady=10)

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
        Button(frm_bt_ne, text="Show More", command=self.show_more_car).grid(row=0, column=0, columnspan=3)

        self.treeview_steal = ttk.Treeview(lbl_frame, show="headings", selectmode="browse")
        self.treeview_steal["column"] = ("name owner", "national code", "car tag", "model")
        self.treeview_steal.heading("name owner", text="Name Owner")
        self.treeview_steal.heading("national code", text="National Code")
        self.treeview_steal.heading("car tag", text="Car Tag")
        self.treeview_steal.heading("model", text="Model")
        self.treeview_steal.grid(row=6, column=0, columnspan=4, padx=5)
        self.treeview_steal.bind("<Double-1>", self.detail_car_steal)
        frm_s_ne = Frame(lbl_frame)
        frm_s_ne.grid(row=7, column=0, columnspan=4)
        Button(frm_s_ne, text="Prev", command=self.prev_steal).grid(row=0, column=1)
        Button(frm_s_ne, text="Next", command=self.next_steal).grid(row=0, column=2)

        self.show_more_car()
        self.show_more_cam()
        self.next_steal()
        self.time_line = 1
        with open("input.txt", "r") as f:
            self.line = f.readlines()

        self.f_out = open("output", "w")
        self.check_violation()

    def show_more_car(self):
        count = 0
        for it in self.callback_car_list:
            tag = f"{it.tag[:2]} {self.tag_list[int(it.tag[2: 4])]} {it.tag[4:7]} {it.tag[7:]}"
            item = (it.name_owner, it.national_code, tag, it.model.name)
            self.treeview_car.insert("", "end", values=item, text=str(self.index_car))
            self.list_car.append(it)
            self.index_car += 1
            if count > self.item:
                return
            count += 1

    def refresh_car(self):
        self.owner_name.delete(0, "end")
        self.nat_code.delete(0, "end")
        self.ent_fir_tag.delete(0, "end")
        self.ent_tri_tag.delete(0, "end")
        self.str_var.set(self.tag_list[0])
        self.treeview_car.delete(*self.treeview_car.get_children())
        self.index_car = 0
        self.list_car = []
        self.callback_car_list = self.method_car()
        self.show_more_car()

    def refresh_camera(self):
        self.ent_nam_cam.delete(0, "end")
        self.ent_id_cam.delete(0, "end")
        self.treeview_cam.delete(*self.treeview_cam.get_children())
        self.index_cam = 0
        self.list_cam = []
        self.callback_cam_list = self.method_cam()
        self.show_more_cam()

    def show_more_cam(self):
        count = 0
        for it in self.callback_cam_list:
            speed = it.max_speed_car
            if speed is None:
                speed = "-"
            item = (it.name, it.code, speed)
            self.treeview_cam.insert("", "end", values=item, text=str(self.index_cam))
            self.list_cam.append(it)
            self.index_cam += 1
            if count > self.item:
                return

    def search_car(self):
        name = self.owner_name.get()
        if name == "":
            name = None
        national_code = self.nat_code.get()
        if national_code == "":
            national_code = None
        fir_tag = self.ent_fir_tag.get()
        result = self.str_var.get()
        sec_tag = self.tag_list.index(result)
        tag = str(sec_tag)
        if sec_tag < 10:
            tag = f"0{sec_tag}"
        tir_tag = self.ent_tri_tag.get()
        for_tag = self.ent_for_tag.get()
        result_tag = f"{fir_tag}{tag}{tir_tag}{for_tag}"
        if tir_tag == "":
            result_tag = None
        if not name and not result_tag and not national_code:
            return
        self.treeview_car.delete(*self.treeview_car.get_children())
        self.index_car = 0
        self.list_car = []
        self.callback_car_list = self.callback_search_car(name, national_code, result_tag)
        if self.callback_car_list is not None:
            self.show_more_car()

    def search_camera(self):
        name = self.ent_nam_cam.get()
        code = self.ent_id_cam.get()
        if name == "":
            name = None
        if not code.isnumeric():
            self.ent_id_cam.delete(0, "end")
            messagebox.showerror("Error", "please enter number for camera code!!")
            return
        if code == "":
            code = 999
        self.treeview_cam.delete(*self.treeview_cam.get_children())
        self.index_cam = 0
        self.list_cam = []
        self.callback_cam_list = self.callback_search_camera(name)
        if self.callback_cam_list is not None:
            self.show_more_cam()
        it = self.callback_search_camera(code=int(code))
        if it is not None:
            speed = it.max_speed_car
            if speed is None:
                speed = "-"
            self.list_cam.append(it)
            self.treeview_cam.insert("", "end", values=(it.name, it.code, speed), text=str(len(self.list_cam) - 1))

    def refresh_steal(self):
        self.end_steal = self.method_steal()
        self.start_steal = self.method_steal()
        self.next_steal()

    def next_steal(self):
        if self.end_steal is None:
            return
        if self.end_steal.node.prev is None and self.end_steal.node.next is None:
            self.treeview_steal.delete(*self.treeview_steal.get_children())
            result = self.end_steal.get()
            if result.steal is False:
                self.end_steal.delete_node()
                self.end_steal = None
                self.start_steal = None
                return
            self.list_steal = []
            tag = f"{result.tag[:2]} {self.tag_list[int(result.tag[2: 4])]} {result.tag[4:7]} {result.tag[7:]}"
            self.treeview_steal.insert("", "end", values=(result.name_owner, result.national_code, tag,
                                                          result.model.name), text="0")
            self.list_steal.append(result)
            return
        if self.end_steal.node.next is None:
            return
        self.treeview_steal.delete(*self.treeview_steal.get_children())
        self.start_steal = self.end_steal.copy()
        count = 0
        self.list_steal = []
        for it in self.end_steal.traverse():
            if it.steal is False:
                self.end_steal.delete_node()
                continue
            tag = f"{it.tag[:2]} {self.tag_list[int(it.tag[2: 4])]} {it.tag[4:7]} {it.tag[7:]}"
            item = (it.name_owner, it.national_code, tag, it.model.name)
            self.treeview_steal.insert("", "end", values=item, text=str(count))
            self.list_steal.append(it)
            if count >= self.item:
                self.end_steal.next()
                break
            count += 1

    def prev_steal(self):
        if self.start_steal is None:
            return
        if self.start_steal.node.prev is None and self.start_steal.node.next is None:
            self.treeview_steal.delete(*self.treeview_steal.get_children())
            result = self.start_steal.get()
            if result.steal is False:
                self.start_steal.delete_node()
                return
            self.list_steal = []
            tag = f"{result.tag[:2]} {self.tag_list[int(result.tag[2: 4])]} {result.tag[4:7]} {result.tag[7:]}"
            self.treeview_steal.insert("", "end", values=(result.name_owner, result.national_code, tag,
                                                          result.model.name), text="0")
            self.list_steal.append(result)
            return
        if self.start_steal.node.prev is None:
            return
        self.end_steal = self.start_steal.copy()
        self.treeview_steal.delete(*self.treeview_steal.get_children())
        self.start_steal.prev()
        count = 0
        self.list_steal = []
        for it in self.start_steal.traverse(True):
            if it.steal is False:
                self.start_steal.delete_node()
                continue
            tag = f"{it.tag[:2]} {self.tag_list[int(it.tag[2: 4])]} {it.tag[4:7]} {it.tag[7:]}"
            item = (it.name_owner, it.national_code, tag, it.model.name)
            self.treeview_steal.insert("", 0, values=item, text=str(count))
            self.list_steal.append(it)
            if count >= self.item:
                break
            count += 1

    def add_model(self):
        panel = AddModel(self.callback_add_mode, self.close)
        self.not_tab.add(panel, text="add model")
        self.not_tab.select(panel)

    def add_car(self):
        if len(self.callback_model_list()) == 0:
            messagebox.showerror("Error", "Please enter model first")
            return
        panel = AddCar(self.callback_add_car, self.tag_list, self.callback_model_list, self.close, self.refresh_car)
        self.not_tab.add(panel, text="New Car")
        self.not_tab.select(panel)
        self.show_more_car()

    def make_smart(self):
        panel = MakeSmart(self.callback_search_camera, self.close, self.refresh_camera)
        self.not_tab.add(panel, text="Make Smart")
        self.not_tab.select(panel)

    def detail_car_steal(self, event):
        if self.treeview_steal.selection() == ():
            return
        item = self.treeview_steal.identify("item", event.x, event.y)
        ID = self.treeview_steal.item(item)["text"]
        res = self.list_steal[int(ID)]
        panel = CarInfo(res, self.tag_list, self.callback_add_steal, self.close, self.refresh_steal)
        self.not_tab.add(panel, text=f"Info {res.model.name}")
        self.not_tab.select(panel)

    def detail_car(self, event):
        if self.treeview_car.selection() == ():
            return
        item = self.treeview_car.identify("item", event.x, event.y)
        ID = self.treeview_car.item(item)["text"]
        res = self.list_car[int(ID)]
        panel = CarInfo(res, self.tag_list, self.callback_add_steal, self.close, self.refresh_steal)
        self.not_tab.add(panel, text=f"Info {res.model.name}")
        self.not_tab.select(panel)

    def add_camera(self):
        panel = AddCamera(self.callback_add_camera, self.close, self.refresh_camera)
        self.not_tab.add(panel, text="New Camera")
        self.not_tab.select(panel)

    def check_violation(self):
        if self.time_line > len(self.line):
            return
        i = self.line[self.time_line - 1]
        text = ""
        res = i.split(",")
        if len(res) > 1:

            for i in res[1:]:
                tag = i[5:16]
                result = tag.split("-")
                if len(result[1]) == 1:
                    tag = f"{result[0]}-0{result[1]}-{result[2]}-{result[3]}"
                vio = self.callback_check_violation(int(i[:4]), tag, int(i[17:19]))
                for j in vio:
                    if j:
                        text += f"{int(i[:4])}:{i[5:16]}:{j}, "
                        self.l_box.insert("end", f"{self.time_line}-{int(i[:4])}:{i[5:16]}:{j}")
        self.f_out.write(f"{self.time_line},{text}\n")
        self.time_line += 1
        self.after(1000, self.check_violation)

    def close(self):
        self.not_tab.hide(self.not_tab.select())





