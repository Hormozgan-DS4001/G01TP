from configure.configure import Button, Entry, Label, LabelFrame, Frame, Scale, Radiobutton, Text, Tk, Spinbox
from tkinter import BooleanVar


class AddCamera(Tk):
    def __init__(self, callback_add_camera):
        super(AddCamera, self).__init__()
        self.callback_add_camera = callback_add_camera

        Label(self, text="Camera Name: ").grid(row=0, column=0)
        self.en_name = Entry(self)
        self.en_name.grid(row=0, column=1, sticky="w")

        Label(self, text="Camera Code: ").grid(row=1, column=0)
        self.ent_code = Spinbox(self, from_=1000, to=9999)
        self.ent_code.grid(row=1, column=1, sticky="w", pady=10)

        frm_in = LabelFrame(self, text="OUT OR IN")
        frm_in.grid(row=2, column=0, columnspan=2)
        self.out_in = BooleanVar()
        self.out_in.set(False)
        Radiobutton(frm_in, text="IN", variable=self.out_in, value=False, command=self.check_out).grid(row=0, column=1)
        Radiobutton(frm_in, text="OUT", variable=self.out_in, value=True, command=self.check_out).grid(row=0, column=0)
        frm_time = Frame(frm_in)
        frm_time.grid(row=1, column=0, columnspan=2)
        Label(frm_time, text="No Stop Time").grid(row=0, column=0, columnspan=4)
        Label(frm_time, text="Hour: ").grid(row=1, column=0)
        self.ent_h = Spinbox(frm_time, from_=00, to=23, format="%02.0f", state="readonly")
        self.ent_h.grid(row=1, column=1)
        Label(frm_time, text="Min: ").grid(row=1, column=2)
        self.ent_min = Spinbox(frm_time, from_=0, to=60, state="readonly")
        self.ent_min.grid(row=1, column=3)




        # Label(self, text="Address: ").grid(row=2, column=0)
        # self.ent_address = Text(self, height=10, width=50)
        # self.ent_address.grid(row=2, column=1, columnspan=4)

    def check_out(self):
        if



m = AddCamera(8434)
m.mainloop()