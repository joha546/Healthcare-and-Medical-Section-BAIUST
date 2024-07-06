from views.staff_view import StaffView
from utils.database import Database
from models.staff import Staff

class StaffController:
    def __init__(self):
        self.view = StaffView()
        self.database = Database()
        self.view.submit_button.clicked.connect(self.add_staff)
        
    def show_add_staff_view(self):
        self.view.show()
        
    def show_view_staff_view(self):
        # Logics to show staff
        pass
        
    def add_staff(self):
        name = self.view.name_input.text()
        position = self.view.position_input.text()
        address = self.view.address_input.text()
        
        staff = Staff(None, name, position, address)
        self.database.execute("INSERT INTO staff (name, position, address) VALUES (?, ?, ?)",
                              (name, position, address))
        self.view.close()
