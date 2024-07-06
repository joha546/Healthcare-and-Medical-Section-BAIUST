from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AppointmentView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.patient_id_label = QLabel('Patient ID:')
        self.patient_id_input = QLineEdit()
        
        self.doctor_id_label = QLabel('Doctor ID:')
        self.doctor_id_input = QLineEdit()
        
        self.date_label = QLabel('Date:')
        self.date_input = QLineEdit()
        
        self.time_label = QLabel('Time:')
        self.time_input = QLineEdit()
        
        self.submit_button = QPushButton('Submit')
        
        self.layout.addWidget(self.patient_id_label)
        self.layout.addWidget(self.patient_id_input)
        self.layout.addWidget(self.doctor_id_label)
        self.layout.addWidget(self.doctor_id_input)
        self.layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.time_input)
        self.layout.addWidget(self.submit_button)
        
        self.setLayout(self.layout)
