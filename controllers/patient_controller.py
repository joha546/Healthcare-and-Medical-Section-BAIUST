# controllers/patient_controller.py

from models.patient import Patient
from views.patient_view import PatientView
from utils.database import Database

class PatientController:
    def __init__(self):
        self.view = PatientView()
        self.database = Database()
        self.view.submit_button.clicked.connect(self.add_patient)
        
    def show_add_patient_view(self):
        self.view.show()
    
    def show_view_patients_view(self):
        patients = self.database.fetchall("SELECT * FROM patients")
        self.view.display_patients(patients)
        self.view.show()
    
    def add_patient(self):
        name = self.view.name_input.text()
        age = self.view.age_input.text()
        level_term = self.view.level_term_input.text()
        department = self.view.department_input.text()
        address = self.view.address_input.text()
        phone = self.view.phone_input.text()
        
        patient = Patient(None, name, age, level_term, department, address, phone)
        self.database.execute("INSERT INTO patients (name, age, level_term, department, address, phone) VALUES (?, ?, ?, ?, ?, ?)",
                              (name, age, level_term, department, address, phone))
        self.show_view_patients_view()
        self.view.close()
