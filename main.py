import tkinter as tk
from tkinter import messagebox
from solver import solve_linear_equation
from validator import validate_input
from history import HistoryManager


class LinearSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Giải Phương Trình Bậc 1")
        self.root.geometry("440x380")
        self.root.resizable(False, False)
        self.root.configure(bg="#ECEFF1")

        # Khởi tạo bộ quản lý lịch sử
        self.history = HistoryManager()

        # Tiêu đề chính
        lbl_title = tk.Label(
            root,
            text="GIẢI PHƯƠNG TRÌNH BẬC 1: aX + b = 0",
            font=("Arial", 11, "bold"),
            fg="#0D47A1",
            bg="#ECEFF1"
        )
        lbl_title.pack(pady=12)

        # Khung nhập liệu (Inputs)
        frame_input = tk.LabelFrame(
            root, text=" Nhập hệ số (Inputs) ", font=("Arial", 9, "bold"),
            padx=15, pady=10, bg="#ECEFF1"
        )
        frame_input.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_input, text="Hệ số a", font=("Arial", 9), bg="#ECEFF1").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_a = tk.Entry(frame_input, font=("Arial", 10), width=28)
        self.entry_a.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(frame_input, text="Hệ số b", font=("Arial", 9), bg="#ECEFF1").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_b = tk.Entry(frame_input, font=("Arial", 10), width=28)
        self.entry_b.grid(row=1, column=1, pady=5, padx=10)

        # Khung chứa nút bấm
        frame_btn = tk.Frame(root, bg="#ECEFF1")
        frame_btn.pack(pady=10)

        btn_solve = tk.Button(
            frame_btn, text="GIẢI PHƯƠNG TRÌNH", font=("Arial", 9, "bold"),
            bg="#1E88E5", fg="white", px=12, py=4, relief="flat",
            command=self.handle_solve
        )
        btn_solve.pack(side="left", padx=5)

        btn_reset = tk.Button(
            frame_btn, text="Làm mới", font=("Arial", 9),
            bg="#CFD8DC", px=10, py=4, relief="flat",
            command=self.handle_reset
        )
        btn_reset.pack(side="left", padx=5)

        # Khung hiển thị kết quả (Results)
        frame_result = tk.LabelFrame(
            root, text=" Kết quả (Results) ", font=("Arial", 9, "bold"),
            padx=15, pady=10, bg="#ECEFF1"
        )
        frame_result.pack(fill="x", padx=20, pady=5)

        self.lbl_result = tk.Label(
            frame_result,
            text="Vui lòng nhập hệ số a, b và bấm Giải",
            font=("Arial", 10, "bold"),
            fg="#2E7D32",
            bg="#E8F5E9",
            pady=10
        )
        self.lbl_result.pack(fill="x")

        # Chân trang
        lbl_footer = tk.Label(
            root, text="Thiết kế bởi Đội Ngũ Phát Triển",
            font=("Arial", 8, "italic"), fg="#78909C", bg="#ECEFF1"
        )
        lbl_footer.pack(side="bottom", pady=8)

    def handle_solve(self):
        try:
            # 1. Kiểm tra dữ liệu qua validator.py
            a = validate_input(self.entry_a.get(), "a")
            b = validate_input(self.entry_b.get(), "b")

            # 2. Tính toán nghiệm qua solver.py
            result = solve_linear_equation(a, b)

            # 3. Định dạng phương trình hiển thị
            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            equation_str = f"PHƯƠNG TRÌNH: {a}X {b_str} = 0"

            self.lbl_result.config(
                text=f"{equation_str}\n{result.upper()}",
                fg="#1B5E20",
                bg="#C8E6C9"
            )

            # 4. Ghi lịch sử tính toán qua history.py
            self.history.save_record(a, b, result)

        except ValueError as err:
            messagebox.showerror("Lỗi dữ liệu", str(err))

    def handle_reset(self):
        self.entry_a.delete(0, tk.END)
        self.entry_b.delete(0, tk.END)
        self.lbl_result.config(
            text="Vui lòng nhập hệ số a, b và bấm Giải",
            fg="#2E7D32",
            bg="#E8F5E9"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = LinearSolverApp(root)
    root.mainloop()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
