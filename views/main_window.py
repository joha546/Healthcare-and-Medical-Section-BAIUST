from PyQt5.QtWidgets import QMainWindow, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Healthcare Management System')
        self.setGeometry(100, 100, 800, 600)
        
        mainMenu = self.menuBar()
        
        patientMenu = mainMenu.addMenu('Patient')
        self.add_patient_action = QAction('Add Patient', self)
        patientMenu.addAction(self.add_patient_action)
        self.view_patients_action = QAction('View Patients', self)
        patientMenu.addAction(self.view_patients_action)
        
        appointmentMenu = mainMenu.addMenu('Appointment')
        self.add_appointment_action = QAction('Add Appointment', self)
        appointmentMenu.addAction(self.add_appointment_action)
        self.view_appointments_action = QAction('View Appointments', self)
        appointmentMenu.addAction(self.view_appointments_action)
        
        recordMenu = mainMenu.addMenu('Medical Record')
        self.add_record_action = QAction('Add Medical Record', self)
        recordMenu.addAction(self.add_record_action)
        self.view_records_action = QAction('View Medical Records', self)
        recordMenu.addAction(self.view_records_action)
        
        staffMenu = mainMenu.addMenu('Staff')
        self.add_staff_action = QAction('Add Staff', self)
        staffMenu.addAction(self.add_staff_action)
        self.view_staff_action = QAction('View Staff', self)
        staffMenu.addAction(self.view_staff_action)
        
        self.show()
