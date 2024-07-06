from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PatientView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
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
        
        self.setLayout(self.layout)
