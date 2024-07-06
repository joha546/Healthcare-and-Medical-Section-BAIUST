from PyQt5.QtWidgets import QTableWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidgetItem

class PatientView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        # Input fields for adding patients
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        
        self.age_label = QLabel('Age:')
        self.age_input = QLineEdit()
        
        self.level_term_label = QLabel('Level/Term:')
        self.level_term_input = QLineEdit()
        
        self.department_label = QLabel('Department:')
        self.department_input = QLineEdit()
        
        self.address_label = QLabel('Address:')
        self.address_input = QLineEdit()
        
        self.phone_label = QLabel('Phone:')
        self.phone_input = QLineEdit()
        
        self.submit_button = QPushButton('Submit')
        
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(self.level_term_label)
        self.layout.addWidget(self.level_term_input)
        self.layout.addWidget(self.department_label)
        self.layout.addWidget(self.department_input)
        self.layout.addWidget(self.address_label)
        self.layout.addWidget(self.address_input)
        self.layout.addWidget(self.phone_label)
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(self.submit_button)
        
        # Table widget for displaying patients
        self.patient_table = QTableWidget()
        self.layout.addWidget(self.patient_table)
        
        self.setLayout(self.layout)

    def display_patients(self, patients):
        # Clear existing data in table widget
        self.clear_patient_table()
        
        # Display patients in the table widget
        self.patient_table.setRowCount(len(patients))
        self.patient_table.setColumnCount(7)  # Adjust columns based on your patient data fields
        
        headers = ['ID', 'Name', 'Age', 'Level/Term', 'Department', 'Address', 'Phone']
        self.patient_table.setHorizontalHeaderLabels(headers)
        
        for row, patient in enumerate(patients):
            for col, data in enumerate(patient):
                item = QTableWidgetItem(str(data))
                self.patient_table.setItem(row, col, item)
                
    def clear_patient_table(self):
        self.patient_table.clearContents()
        self.patient_table.setRowCount(0)
