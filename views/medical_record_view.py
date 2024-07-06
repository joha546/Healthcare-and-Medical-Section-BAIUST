from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MedicalRecordView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.patient_id_label = QLabel('Patient ID:')
        self.patient_id_input = QLineEdit()
        
        self.diagnosis_label = QLabel('Diagnosis:')
        self.diagnosis_input = QLineEdit()
        
        self.treatment_label = QLabel('Treatment:')
        self.treatment_input = QLineEdit()
        
        self.doctor_label = QLabel('Doctor:')
        self.doctor_input = QLineEdit()
        
        self.submit_button = QPushButton('Submit')
        
        self.layout.addWidget(self.patient_id_label)
        self.layout.addWidget(self.patient_id_input)
        self.layout.addWidget(self.diagnosis_label)
        self.layout.addWidget(self.diagnosis_input)
        self.layout.addWidget(self.treatment_label)
        self.layout.addWidget(self.treatment_input)
        self.layout.addWidget(self.doctor_label)
        self.layout.addWidget(self.doctor_input)
        self.layout.addWidget(self.submit_button)
        
        self.setLayout(self.layout)
