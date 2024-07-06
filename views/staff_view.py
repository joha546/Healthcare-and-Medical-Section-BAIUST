from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class StaffView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        
        self.position_label = QLabel('Position:')
        self.position_input = QLineEdit()
        
        self.address_label = QLabel('Address:')
        self.address_input = QLineEdit()
        
        self.submit_button = QPushButton('Submit')
        
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.position_label)
        self.layout.addWidget(self.position_input)
        self.layout.addWidget(self.address_label)
        self.layout.addWidget(self.address_input)
        self.layout.addWidget(self.submit_button)
        
        self.setLayout(self.layout)
