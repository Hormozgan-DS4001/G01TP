
from configure.configure import Frame, Radiobutton, LabelFrame, Label, Listbox
from tkinter import BooleanVar, Listbox


class CarInfo(Frame):
    def __init__(self, obj_car, tag_list, close):
        super(CarInfo, self).__init__()
        self.obj_car = obj_car
        self.callback_violations = obj_car.show_violation()
        self.tag_list = tag_list
        self.close = close

        self.lbl_steal = Label(self, text="This car is STEAL", bg="red", foreground="yellow")

        self.val_name = ["Unauthorized high speed", "Unauthorized low speed", "intelligent speed control",
                         "Unauthorized traffic"]

        Label(self, text="Name Owner: ").grid(row=1, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.name_owner}", font=('Helvetica', 11)).grid(row=1, column=1, sticky="w",
                                                                                    padx=10)
        Label(self, text="National Code: ").grid(row=2, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.national_code}", font=('Helvetica', 11)).grid(row=2, column=1, sticky="w",
                                                                                       padx=10)
        Label(self, text="Model: ").grid(row=3, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.model}", font=('Helvetica', 11)).grid(row=3, column=1, sticky="w", padx=10)
        Label(self, text="Car Tag: ").grid(row=4, column=0, sticky="w", pady=5)
        Label(self, text=f"{self.obj_car.tag[:2]} {self.tag_list[int(self.obj_car.tag[2])]} {self.obj_car.tag[3:]}",
              font=('Helvetica', 11)).grid(row=4, column=1, sticky="w", padx=10)
        Label(self, text="Truck or Car: ").grid(row=5, column=0, sticky="w", pady=5)
        if self.obj_car.heavy:
            Label(self, text=f"Truck", font=('Helvetica', 11)).grid(row=5, column=1, sticky="w", padx=10)
        else:
            Label(self, text=f"Car", font=('Helvetica', 11)).grid(row=5, column=1, sticky="w", padx=10)

        frm_steal = LabelFrame(self, text="Steal Car")
        frm_steal.grid(row=6, column=0, columnspan=2)
        self.steal_var = BooleanVar()
        self.steal_var.set(self.obj_car.steal)
        Radiobutton(frm_steal, text="ON", variable=self.steal_var, value=True, command=self.check_steal).grid(row=0,
                                                                                                              column=0)
        Radiobutton(frm_steal, text="OFF", variable=self.steal_var, value=False, command=self.check_steal).grid(
                    row=0, column=1)
        self.show_steal()
        Label(self, text="Violation List").grid(row=7, column=0, columnspan=2, pady=5)
        self.treeview = Listbox(self, height=10, width=40)
        self.treeview.grid(row=8, column=0, columnspan=2)
        self.show_violation()

    def show_violation(self):
        for i in self.callback_violations:
            self.treeview.insert(0, self.val_name[i - 1])

    def check_steal(self):
        res = self.steal_var.get()
        if res is not self.obj_car.steal:
            self.obj_car.steal_car(res)
        self.show_steal()

    def show_steal(self):
        if self.obj_car.steal:
            self.lbl_steal.grid(row=0, column=0, columnspan=2)
        else:
            self.lbl_steal.grid_forget()
