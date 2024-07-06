from PyQt5.QtWidgets import QApplication
from controllers.main_controller import MainController

def main():
    app = QApplication([])
    main_controller = MainController()
    main_controller.run()
    app.exec_()

if __name__ == '__main__':
    main()
