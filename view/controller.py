from model import Core
from view import Manager


database = Core()


m = Manager(database.show_all_camera, database.show_all_car, database.add_car, database.add_camera, database.add_model,
            database.search_camera, database.check_violation, database.show_model, database.show_steal,
            database.add_steal)

m.mainloop()
