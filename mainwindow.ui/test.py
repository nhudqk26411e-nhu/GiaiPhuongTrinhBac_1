import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from giaiphuongtrinhbac1ex import giaiphuongtrinhbac1ex

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_win = QMainWindow()

    mygui = giaiphuongtrinhbac1ex()
    mygui.setupUi(main_win)
    mygui.showWindow()

    sys.exit(app.exec())