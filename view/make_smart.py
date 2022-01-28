from configure.configure import Button, Frame, LabelFrame, Label, Spinbox
from tkinter import messagebox


class MakeSmart(Frame):
    def __init__(self, callback_search_camera, close):
        super(MakeSmart, self).__init__()
        self.callback_search_camera = callback_search_camera
        self.close = close

        frm_enter = LabelFrame(self, text="Enter Camera")
        frm_enter.grid(row=0, column=0, padx=5)
        Label(frm_enter, text="Camera Code: ").grid(row=0, column=0)
        self.ent_code = Spinbox(frm_enter, from_=1000, to=9999)
        self.ent_code.grid(row=0, column=1, sticky="w", pady=10)

        frm_ex = LabelFrame(self, text="Exit Camera")
        frm_ex.grid(row=0, column=1)
        Label(frm_ex, text="Camera Code: ").grid(row=0, column=0)
        self.ex_code = Spinbox(frm_ex, from_=1000, to=9999)
        self.ex_code.grid(row=0, column=1, sticky="w", pady=10)

        frm_time = LabelFrame(self, text="Time")
        frm_time.grid(row=1, column=0, columnspan=2, pady=5)
        Label(frm_time, text="Hour: ").grid(row=1, column=0, padx=5)
        self.ent_h_from = Spinbox(frm_time, from_=00, to=23, format="%02.0f", state="readonly")
        self.ent_h_from.grid(row=1, column=1)
        Label(frm_time, text="Minutes: ").grid(row=1, column=2, padx=5)
        self.ent_min_from = Spinbox(frm_time, from_=0, to=60, state="readonly")
        self.ent_min_from.grid(row=1, column=3)
        Label(frm_time, text="Second: ").grid(row=1, column=4, padx=5)
        self.ent_sec_from = Spinbox(frm_time, from_=0, to=60, state="readonly")
        self.ent_sec_from.grid(row=1, column=5)

        Button(self, text="Done", command=self.make_smart).grid(row=2, column=0, columnspan=2)

    def make_smart(self):
        code_ent = self.ent_code.get()
        code_exit = self.ex_code.get()
        if not code_ent.isnumeric() or not 1000 <= int(code_ent) <= 9999:
            messagebox.showerror("Error", "Please enter correct code!!")
            return
        if not code_exit.isnumeric() or not 1000 <= int(code_exit) <= 9999:
            messagebox.showerror("Error", "Please enter correct code!!")
            return
        cam_ent = self.callback_search_camera(code=int(code_ent))
        if not cam_ent:
            messagebox.showerror("Error", "Enter Camera is not available")
            return
        cam_ex = self.callback_search_camera(code=int(code_exit))
        if not cam_ex:
            messagebox.showerror("Error", "Enter Camera is not available")
            return
        hour = self.ent_h_from.get()
        minute = self.ent_min_from.get()
        second = self.ent_sec_from.get()
        cam_ent.make_smart(cam_ex, hour, minute, second)
        self.ent_code.delete(0, "end")
        self.ent_code.insert(0, 1000)
        self.ex_code.delete(0, "end")
        self.ex_code.insert(0, 1000)
        self.ent_h_from.configure(state="normal")
        self.ent_h_from.delete(0, "end")
        self.ent_h_from.insert(0, 00)
        self.ent_h_from.configure(state="readonly")
        self.ent_min_from.configure(state="normal")
        self.ent_min_from.delete(0, "end")
        self.ent_min_from.insert(0, 0)
        self.ent_min_from.configure(state="readonly")
        self.ent_sec_from.configure(state="normal")
        self.ent_sec_from.delete(0, "end")
        self.ent_sec_from.insert(0, 0)
        self.ent_sec_from.configure(state="readonly")
        self.close()
