# Healthcare Management System

## Overview

This project implements a Healthcare Management System using Python and PyQt5 for the frontend and SQLite for the backend database. It provides functionalities for managing patients, appointments, medical records, and staff within a university medical support setting.

## Features

- **Patient Management**: Add, view, and manage patient records.
- **Appointment Scheduling**: Schedule appointments for patients who want to do his treatment after some times.
- **Medical Record Management**: Maintain medical records including diagnoses and treatments.
- **Staff Management**: Add and manage staff members including doctors and administrative staff.

## Technologies Used

- **Python 3**: Language used for development.
- **PyQt5**: Python bindings for Qt, used for building the graphical user interface (GUI).
- **SQLite**: Embedded relational database management system used for storing patient and medical data.

## Design Patterns Applied

- **MVC (Model-View-Controller)**:
  - **Model**: Includes Python classes representing data entities such as Patient, MedicalRecord, and Staff.
  - **View**: Implemented using PyQt5 widgets for user interaction.
  - **Controller**: Manages user inputs and interactions, updating the model and view accordingly.

- **Singleton**: Implemented in the Database utility class to ensure a single database connection throughout the application's lifecycle.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/joha546/healthcare-management-system.git
   cd healthcare-management-system
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

- **Adding a Patient**: Enter patient details like Name, Age, Department, Level-Term, Address etc in the input fields and click "Submit".
- **Viewing Patients**: Click on "Patient" -> "View Patients" in the menu to display a list of patients.
- **Managing Appointments**: Use the "Appointment" menu to add or view appointments.
- **Recording Medical Data**: Use the "Medical Record" menu to add or view medical records.
- **Managing Staff**: Add or view staff members using the "Staff" menu.

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests for any improvements or additional features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- PyQt documentation: https://www.riverbankcomputing.com/static/Docs/PyQt5/
- SQLite documentation: https://www.sqlite.org/docs.html
