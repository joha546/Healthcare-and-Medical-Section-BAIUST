from PyQt5.QtWidgets import QMainWindow, QApplication
from views.main_window import MainWindow
from controllers.patient_controller import PatientController
from controllers.appointment_controller import AppointmentController
from controllers.medical_record_controller import MedicalRecordController
from controllers.staff_controller import StaffController

class MainController:
    def __init__(self):
        self.main_window = MainWindow()
        
        self.patient_controller = PatientController()
        self.appointment_controller = AppointmentController()
        self.medical_record_controller = MedicalRecordController()
        self.staff_controller = StaffController()
        
        self.connect_actions()

    def connect_actions(self):
        self.main_window.add_patient_action.triggered.connect(self.patient_controller.show_add_patient_view)
        self.main_window.view_patients_action.triggered.connect(self.patient_controller.show_view_patients_view)
        
        self.main_window.add_appointment_action.triggered.connect(self.appointment_controller.show_add_appointment_view)
        self.main_window.view_appointments_action.triggered.connect(self.appointment_controller.show_view_appointments_view)
        
        self.main_window.add_record_action.triggered.connect(self.medical_record_controller.show_add_record_view)
        self.main_window.view_records_action.triggered.connect(self.medical_record_controller.show_view_records_view)
        
        self.main_window.add_staff_action.triggered.connect(self.staff_controller.show_add_staff_view)
        self.main_window.view_staff_action.triggered.connect(self.staff_controller.show_view_staff_view)

    def run(self):
        self.main_window.show()
