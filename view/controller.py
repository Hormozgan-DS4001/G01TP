from model import Core
from view import Manager
from pickle import load, dump
from os.path import exists as file_exists

if file_exists("database.bin"):
    file = open("database.bin", "rb")
    database = load(file)
    file.close()
else:
    database = Core()


m = Manager(database.show_all_camera, database.show_all_car, database.add_car, database.add_camera, database.add_model,
            database.search_camera, database.check_violation, database.show_model, database.show_steal,
            database.add_steal, database.search_car)

m.mainloop()

file = open("database.bin", "wb")
dump(database, file)
file.close()
