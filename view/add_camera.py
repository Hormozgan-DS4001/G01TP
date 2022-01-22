from configure.configure import Button, Entry, Label, LabelFrame, Frame, Scale, Radiobutton, Text, Spinbox
from tkinter import BooleanVar, messagebox


class AddCamera(Frame):
    def __init__(self, callback_add_camera, close):
        super(AddCamera, self).__init__()
        self.callback_add_camera = callback_add_camera
        self.close = close

        Label(self, text="Camera Name: ").grid(row=0, column=0)
        self.en_name = Entry(self)
        self.en_name.grid(row=0, column=1, sticky="w")

        Label(self, text="Camera Code: ").grid(row=1, column=0)
        self.ent_code = Spinbox(self, from_=1000, to=9999)
        self.ent_code.grid(row=1, column=1, sticky="w", pady=10)

        frm_in = LabelFrame(self, text="OUT OR IN")
        frm_in.grid(row=2, column=0, columnspan=2)
        self.out_in = BooleanVar()
        self.out_in.set(True)
        Radiobutton(frm_in, text="OUT", variable=self.out_in, value=True, command=self.check_out).grid(row=0, column=0)
        Radiobutton(frm_in, text="IN", variable=self.out_in, value=False, command=self.check_out).grid(row=0, column=1)
        self.frm_time = Frame(frm_in)
        Label(self.frm_time, text="No Stop Time").grid(row=0, column=0, columnspan=4)
        frm_time_from = LabelFrame(self.frm_time, text="From")
        frm_time_from.grid(row=1, column=0, columnspan=3)
        Label(frm_time_from, text="Hour: ").grid(row=1, column=0)
        self.ent_h_from = Spinbox(frm_time_from, from_=00, to=23, format="%02.0f", state="readonly")
        self.ent_h_from.grid(row=1, column=1)
        Label(frm_time_from, text="Minutes: ").grid(row=1, column=2)
        self.ent_min_from = Spinbox(frm_time_from, from_=0, to=60, state="readonly")
        self.ent_min_from.grid(row=1, column=3)
        frm_time_to = LabelFrame(self.frm_time, text="To")
        frm_time_to.grid(row=2, column=0, columnspan=3)
        Label(frm_time_to, text="Hour: ").grid(row=1, column=0)
        self.ent_h = Spinbox(frm_time_to, from_=00, to=23, format="%02.0f", state="readonly")
        self.ent_h.grid(row=1, column=1)
        Label(frm_time_to, text="Minutes: ").grid(row=1, column=2)
        self.ent_min = Spinbox(frm_time_to, from_=0, to=60, state="readonly")
        self.ent_min.grid(row=1, column=3)

        frm_max = LabelFrame(self, text="Max Speed")
        frm_max.grid(row=3, column=0, columnspan=2, pady=10)
        self.max_speed = BooleanVar()
        self.max_speed.set(False)
        Radiobutton(frm_max, text="ON", variable=self.max_speed, value=True, command=self.check_speed).grid(row=0,
                                                                                                            column=1)
        Radiobutton(frm_max, text="OFF", variable=self.max_speed, value=False, command=self.check_speed).grid(row=0,
                                                                                                              column=0)
        self.frm_max_speed = Frame(frm_max)
        Label(self.frm_max_speed, text="Max Speed Car: ").grid(row=0, column=0)
        self.max_speed_car = Scale(self.frm_max_speed, from_=0, to=250)
        self.max_speed_car.grid(row=0, column=1)
        Label(self.frm_max_speed, text="Max Speed Track: ").grid(row=1, column=0)
        self.max_speed_track = Scale(self.frm_max_speed, from_=0, to=250)
        self.max_speed_track.grid(row=1, column=1)

        frm_min = LabelFrame(self, text="Min Speed")
        frm_min.grid(row=4, column=0, columnspan=2)
        self.min_speed = BooleanVar()
        self.min_speed.set(False)
        Radiobutton(frm_min, text="ON", variable=self.min_speed, value=True, command=self.check_min_speed).grid(
                    row=0, column=1)
        Radiobutton(frm_min, text="OFF", variable=self.min_speed, value=False, command=self.check_min_speed).grid(
                    row=0, column=0)

        self.frm_min_speed = Frame(frm_min)
        Label(self.frm_min_speed, text="Min Speed Car: ").grid(row=0, column=0)
        self.min_speed_car = Scale(self.frm_min_speed, from_=0, to=250)
        self.min_speed_car.grid(row=0, column=1)

        Label(self, text="Address: ").grid(row=5, column=0, columnspan=4, pady=5)
        self.ent_address = Text(self, height=10, width=50)
        self.ent_address.grid(row=6, column=0, columnspan=4)

        Button(self, text="Add Camera", command=self.add_camera).grid(row=7, column=0, columnspan=4)

    def add_camera(self):
        name = self.en_name.get()
        address = self.ent_address.get(0, "end")
        code = self.ent_code.get()
        max_car = None
        max_truck = None
        min_speed = None
        if len(name) > 40 or not name:
            messagebox.showerror("Error", "Name Camera can not be more than forty characters or none")
            self.en_name.delete(0, "end")
            return
        if len(address) > 200:
            messagebox.showerror("Error", "Address can not be more than forty characters")
            self.ent_address.delete(0, "end")
            return
        if self.max_speed.get():
            max_car = self.max_speed_car.get()
            max_truck = self.max_speed_track.get()
        if self.min_speed.get():
            min_speed = self.min_speed_car.get()
        cam = self.callback_add_camera(name, address, code, self.out_in.get(), max_truck, max_car, min_speed)
        if cam == 0:
            messagebox.showerror("Error", "this code already exit in list")
            self.ent_code.delete(0, "end")
            self.ent_code.insert(0, 1000)
            return
        if not self.out_in.get():
            hours_from = self.ent_h_from.get()
            minutes_from = self.ent_min_from.get()
            hours = self.ent_h.get()
            minutes = self.ent_min.get()
            cam.set_time(hours_from, minutes_from, hours, minutes)

        self.en_name.delete(0, "end")
        self.ent_code.delete(0, "end")
        self.ent_code.insert(0, 1000)
        self.ent_address.delete(0, "end")
        self.max_speed_car.set(0)
        self.max_speed_track.set(0)
        self.min_speed_car.set(0)
        self.ent_h_from.configure(state="normal")
        self.ent_h_from.delete(0, "end")
        self.ent_h_from.insert(0, 00)
        self.ent_h_from.configure(state="readonly")
        self.ent_min_from.configure(state="normal")
        self.ent_min_from.delete(0, "end")
        self.ent_min_from.insert(0, 0)
        self.ent_min_from.configure(state="readonly")
        self.out_in.set(True)
        self.max_speed.set(False)
        self.min_speed.set(False)

    def check_min_speed(self):
        if self.min_speed.get():
            self.frm_min_speed.grid(row=4, column=0, columnspan=4)
        if not self.min_speed.get():
            self.frm_min_speed.grid_forget()

    def check_speed(self):
        if self.max_speed.get():
            self.frm_max_speed.grid(row=4, column=0, columnspan=4)
        if not self.max_speed.get():
            self.frm_max_speed.grid_forget()

    def check_out(self):
        if not self.out_in.get():
            self.frm_time.grid(row=1, column=0, columnspan=2)
        if self.out_in.get():
            self.frm_time.grid_forget()

