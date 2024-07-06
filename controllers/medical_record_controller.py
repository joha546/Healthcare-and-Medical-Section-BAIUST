from views.medical_record_view import MedicalRecordView
from utils.database import Database
from models.medical_record import MedicalRecord

class MedicalRecordController:
    def __init__(self):
        self.view = MedicalRecordView()
        self.database = Database()
        self.view.submit_button.clicked.connect(self.add_record)
        
    def show_add_record_view(self):
        self.view.show()
        
    def show_view_records_view(self):
        # Logics to show medical records
        pass
        
    def add_record(self):
        patient_id = self.view.patient_id_input.text()
        diagnosis = self.view.diagnosis_input.text()
        treatment = self.view.treatment_input.text()
        doctor = self.view.doctor_input.text()
        
        record = MedicalRecord(None, patient_id, diagnosis, treatment, doctor)
        self.database.execute("INSERT INTO medical_records (patient_id, diagnosis, treatment, doctor) VALUES (?, ?, ?, ?)",
                              (patient_id, diagnosis, treatment, doctor))
        self.view.close()
