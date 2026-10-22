from giaiphuongtrinhbac1 import Ui_MainWindow


class giaiphuongtrinhbac1ex(Ui_MainWindow):
    def __init__(self, parent=None):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        # Kết nối sự kiện click của nút bấm
        self.pushButton.clicked.connect(self.process_giai)
        self.pushButton_2.clicked.connect(self.process_lam_moi)

    def process_giai(self):
        try:
            # Lấy dữ liệu từ QLineEdit
            a_str = self.lineEdithesoa.text().strip()
            b_str = self.lineEdithesob.text().strip()

            if not a_str or not b_str:
                self.lineEditphuongtrinh.setText("Vui lòng nhập đủ a và b!")
                self.lineEditnghiem.setText("")
                return

            a = float(a_str)
            b = float(b_str)

            # Định dạng chuỗi hiển thị phương trình giống ảnh mẫu (dùng chữ X hoa)
            if b >= 0:
                pt_str = f"{a:g}X + {b:g} = 0"
            else:
                pt_str = f"{a:g}X - {abs(b):g} = 0"

            self.lineEditphuongtrinh.setText(pt_str)

            # Giải phương trình bậc 1 và hiển thị nghiệm
            if a == 0:
                if b == 0:
                    self.lineEditnghiem.setText("Vô số nghiệm")
                else:
                    self.lineEditnghiem.setText("Vô nghiệm")
            else:
                x = -b / a
                self.lineEditnghiem.setText(f"X = {x}")

        except ValueError:
            self.lineEditphuongtrinh.setText("Lỗi dữ liệu!")
            self.lineEditnghiem.setText("Hệ số phải là số!")

    def process_lam_moi(self):
        # Xóa trắng tất cả dữ liệu khi bấm nút Làm mới
        self.lineEdithesoa.setText("")
        self.lineEdithesob.setText("")
        self.lineEditphuongtrinh.setText("")
        self.lineEditnghiem.setText("")
        self.lineEdithesoa.setFocus()