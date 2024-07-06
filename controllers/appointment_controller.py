from views.appointment_view import AppointmentView
from utils.database import Database
from models.appointment import Appointment

class AppointmentController:
    def __init__(self):
        self.view = AppointmentView()
        self.database = Database()
        self.view.submit_button.clicked.connect(self.add_appointment)
        
    def show_add_appointment_view(self):
        self.view.show()
        
    def show_view_appointments_view(self):
        # Logics to show appointments
        
        pass
        
    def add_appointment(self):
        patient_id = self.view.patient_id_input.text()
        doctor_id = self.view.doctor_id_input.text()
        date = self.view.date_input.text()
        time = self.view.time_input.text()
        
        appointment = Appointment(None, patient_id, doctor_id, date, time)
        self.database.execute("INSERT INTO appointments (patient_id, doctor_id, date, time) VALUES (?, ?, ?, ?)",
                              (patient_id, doctor_id, date, time))
        self.view.close()
