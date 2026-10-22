i  import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from solver import solve_linear_equation, validate_number
from history import TestHistoryManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "main_window.ui")
        uic.loadUi(ui_path, self)

        self.history = TestHistoryManager()

        self.btn_solve.clicked.connect(self.handle_solve)
        self.btn_reset.clicked.connect(self.handle_reset)

    def _get_text(self, widget) -> str:
        if hasattr(widget, 'text'):
            return widget.text()
        elif hasattr(widget, 'cleanText'):
            return widget.cleanText()
        return str(widget.value()) if hasattr(widget, 'value') else ""

    def handle_solve(self):
        try:
            raw_a = self._get_text(self.input_a)
            raw_b = self._get_text(self.input_b)

            a = validate_number(raw_a, "Hệ số a")
            b = validate_number(raw_b, "Hệ số b")

            result = solve_linear_equation(a, b)

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            self.lbl_result.setText(f"PHƯƠNG TRÌNH: {a}X {b_str} = 0\n{result.upper()}")

            self.history.save_test_case(a, b, result)

        except ValueError as err:
            QMessageBox.critical(self, "Lỗi dữ liệu", str(err))

    def handle_reset(self):
        if hasattr(self.input_a, 'clear'):
            self.input_a.clear()
            self.input_b.clear()
        elif hasattr(self.input_a, 'setValue'):
            self.input_a.setValue(0)
            self.input_b.setValue(0)
        self.lbl_result.setText("Vui lòng nhập hệ số a, b và bấm Giải")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())