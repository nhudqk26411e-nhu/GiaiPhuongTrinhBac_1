# Bài Tập Nhóm: Phần Mềm Giải Phương Trình Bậc 1

## Mục lục
* [1. Giới thiệu dự án](#1-gioi-thieu-du-an)
* [2. Phân công nhiệm vụ thành viên](#2-phan-cong-nhiem-vu-thanh-vien)
* [3. Cấu trúc dự án](#3-cau-truc-du-an)
* [4. Hướng dẫn cài đặt và chạy ứng dụng](#4-huong-dan-cai-dat-va-chay-ung-dung)

---

## 1. Giới thiệu dự án
Ứng dụng giải phương trình bậc nhất dạng $ax + b = 0$ xây dựng bằng ngôn ngữ **Python** và thư viện **PyQt6**. Dự án áp dụng mô hình phân chia chức năng rõ ràng cho từng thành viên trong nhóm.

> [!NOTE]
> Mã nguồn được quản lý qua Git/GitHub và theo dõi tiến độ công việc trên Jira Software.

## 2. Phân công nhiệm vụ thành viên

| Thành viên             | Vai trò phụ trách        | File / Module | Chi tiết công việc thực hiện |
|:-----------------------|:-------------------------| :--- | :--- |
| **Phạm Thị Quỳnh Như** | Thiết kế giao diện (GUI) | `main_window.ui` | Thiết kế cửa sổ Qt Designer, tạo các ô nhập $a$, $b$, nút Giải, Làm mới, vùng kết quả và chụp ảnh báo cáo. |
| **Trần Huỳnh Gia Hy**  | Xử lý thuật toán (Logic) | `solver.py` | Lập trình giải các trường hợp $a \ne 0$, $a=0, b=0$, $a=0, b \ne 0$ và kiểm tra dữ liệu nhập không hợp lệ. |
| **Đoàn Quỳnh Như**     | Kết nối giao diện PyQt6  | `main.py` | Nạp file `.ui`, kết nối sự kiện nút Giải/Làm mới và định dạng hiển thị kết quả/thông báo lỗi. |
| **Lục Bảo Linh**       | Kiểm thử & Hoàn thiện    | `history.py` | Kiểm thử bộ giá trị (số âm, số thập phân, chữ, bỏ trống), kiểm tra bố cục giao diện và lưu log test. |
| **Võ Hoàng Linh**          | Tích hợp, GitHub         | `README.md` | Tạo Repository, tổng hợp mã nguồn, biên soạn `README.md`, quản lý Pull Request và cập nhật Jira Board. |

## 3. Cấu trúc dự án
* `main_window.ui`: File thiết kế giao diện bằng Qt Designer.
* `solver.py`: Module chứa thuật toán giải phương trình và hàm kiểm định dữ liệu.
* `main.py`: File khởi chạy chính kết nối GUI và xử lý sự kiện.
* `history.py`: Module hỗ trợ lưu vết và ghi log kiểm thử.
* `test_history.txt`: File nhật ký lưu trữ kết quả test cases.

## 4. Hướng dẫn cài đặt và chạy ứng dụng

### Cài đặt thư viện
```bash
pip install PyQt6