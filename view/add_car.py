from configure.configure import Button, Label, LabelFrame, Entry, Frame, Radiobutton
from tkinter import OptionMenu, messagebox, StringVar, BooleanVar


class AddCar(Frame):
    def __init__(self, callback_add_car, callback_li_tag, callback_list_model, close, refresh_car):
        super(AddCar, self).__init__()
        self.callback_add_car = callback_add_car
        self.tag_list = callback_li_tag
        self.callback_list_model = callback_list_model().find_prefix("")
        self.close = close
        self.refresh_car = refresh_car

        frm_tag = LabelFrame(self, text="TAG")
        frm_tag.grid(row=0, column=0, columnspan=4, pady=5, padx=20)
        Label(frm_tag, text="Car Tag: ").grid(row=0, column=0, pady=5)
        self.ent_fir_tag = Entry(frm_tag, width=6)
        self.ent_fir_tag.grid(row=0, column=1, pady=5, padx=10)
        self.sec_tag = StringVar()
        self.sec_tag.set(self.tag_list[0])
        opm = OptionMenu(frm_tag, self.sec_tag, *self.tag_list)
        opm.grid(row=0, column=2, padx=5)
        opm.configure(bg="#D3DBEB", activebackground="#CDD5E5", width=7)
        opm["menu"].config(bg="white")
        self.ent_tri_tag = Entry(frm_tag, width=10)
        self.ent_tri_tag.grid(row=0, column=3, padx=10)
        self.ent_for_tag = Entry(frm_tag, width=6)
        self.ent_for_tag.grid(row=0, column=4, padx=10)

        frm_hev = LabelFrame(self, text="Car INFO")
        frm_hev.grid(row=1, column=0, sticky="w")
        Label(frm_hev, text="Car Model: ").grid(row=0, column=0)
        self.mode_li = [i.name for i in self.callback_list_model]
        self.str_var_mode = StringVar()
        self.str_var_mode.set(self.mode_li[0])
        opm = OptionMenu(frm_hev, self.str_var_mode, *self.mode_li)
        opm.grid(row=0, column=1, padx=5)
        opm.configure(bg="#D3DBEB", activebackground="#CDD5E5", width=7)
        opm["menu"].config(bg="white")
        self.hev_li = BooleanVar()
        self.hev_li.set(False)
        Radiobutton(frm_hev, text="Truck", variable=self.hev_li, value=True).grid(row=1, column=0, pady=10)
        Radiobutton(frm_hev, text="Car   ", variable=self.hev_li, value=False).grid(row=1, column=1, pady=10)

        frm_per = LabelFrame(self, text="Personal INFO")
        frm_per.grid(row=1, column=1)
        Label(frm_per, text="Name Owner: ").grid(row=0, column=0, pady=5)
        self.ent_owner = Entry(frm_per)
        self.ent_owner.grid(row=0, column=1, pady=5)
        Label(frm_per, text="National Code: ").grid(row=1, column=0, pady=5)
        self.ent_nat = Entry(frm_per)
        self.ent_nat.grid(row=1, column=1, pady=5)

        Button(self, text="Add Car", command=self.add_car).grid(row=2, column=0, columnspan=2)

    def add_car(self):
        firs_tag = self.ent_fir_tag.get()
        if len(firs_tag) != 2 or not firs_tag.isnumeric():
            messagebox.showerror("Error", "please enter a tow-digit number")
            self.ent_fir_tag.delete(0, "end")
            return

        sec_tag = self.sec_tag.get()
        tir_tag = self.ent_tri_tag.get()
        if len(tir_tag) != 3 or not tir_tag.isnumeric():
            messagebox.showerror("Error", "please enter a tree-digit number")
            self.ent_tri_tag.delete(0, "end")
            return

        for_tag = self.ent_for_tag.get()
        if len(for_tag) != 2 or not for_tag.isnumeric():
            messagebox.showerror("Error", "please enter a tree-digit number")
            self.ent_for_tag.delete(0, "end")
            return

        model = self.str_var_mode.get()
        name_owner = self.ent_owner.get()
        national = self.ent_nat.get()
        if len(national) != 10 or not national.isnumeric():
            messagebox.showerror("Error", "please enter correct national code")
            self.ent_nat.delete(0, "end")
            return
        heavy = self.hev_li.get()
        tag = self.tag_list.index(sec_tag)
        if tag < 10:
            tag = f"0{tag}"
        res = self.callback_add_car(model, name_owner, national, firs_tag + str(tag)
                                    + tir_tag + for_tag, heavy)
        if res == 0:
            messagebox.showerror("Error", "this national code already registered in the system")
            self.ent_nat.delete(0, "end")
            return
        if res == 1:
            messagebox.showerror("Error", "this car tag already registered in the system")
            self.ent_fir_tag.delete(0, "end")
            self.sec_tag.set(self.tag_list[0])
            self.ent_tri_tag.delete(0, "end")
            return
        self.ent_fir_tag.delete(0, "end")
        self.sec_tag.set(self.tag_list[0])
        self.ent_tri_tag.delete(0, "end")
        self.ent_for_tag.delete(0, "end")
        self.str_var_mode.set(self.mode_li[0])
        self.ent_owner.delete(0, "end")
        self.ent_nat.delete(0, "end")
        self.hev_li.set(False)
        self.refresh_car()
        self.close()



