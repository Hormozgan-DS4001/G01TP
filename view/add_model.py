from configure.configure import Button, Entry, Label, Frame
from tkinter import messagebox


class AddModel(Frame):
    def __init__(self, add_model, close):
        super(AddModel, self).__init__()
        self.callback_add_model = add_model
        self.close = close
        Label(self, text="Name Model: ").grid(row=0, column=0)
        self.ent_name = Entry(self)
        self.ent_name.grid(row=0, column=1)
        Button(self, text="Add Name", command=self.add_model).grid(row=1, column=0, columnspan=2)

    def add_model(self):
        name = self.ent_name.get()
        if not name:
            messagebox.showerror("Error", "Please enter name")
            return
        self.callback_add_model(name)
        self.ent_name.delete(0, "end")
        self.close()












