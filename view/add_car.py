from configure.configure import Button, Label, LabelFrame, TopLevel, Tk, Entry, Scale, Frame
from tkinter import OptionMenu, messagebox, StringVar


class AddCar(Tk):
    def __init__(self, callback_add_car, callback_li_tag):
        super(AddCar, self).__init__()
        self.callback_add_car = callback_add_car
        self.tag_list = callback_li_tag

        frm_tag = LabelFrame(self, text="TAG")
        frm_tag.grid(row=0, column=0, columnspan=4, pady=5)
        Label(frm_tag, text="Car Tag: ").grid(row=0, column=0, pady=5, padx=5)
        self.ent_fir_tag = Entry(frm_tag)
        self.ent_fir_tag.grid(row=0, column=1, pady=5, padx=10)
        self.ent_sec_tag = None
        self.str_var = StringVar()
        self.str_var.set("-----------")
        opm = OptionMenu(frm_tag, self.str_var, *self.tag_list, command=self.result_op)
        opm.grid(row=0, column=2, padx=5)
        opm.configure(bg="#D3DBEB", activebackground="#CDD5E5", width=7)
        opm["menu"].config(bg="white")
        self.ent_tri_tag = Entry(frm_tag)
        self.ent_tri_tag.grid(row=0, column=3, padx=10)

    def result_op(self, even):
        pass















