from datetime import datetime

class HistoryManager:
    def __init__(self, filename="history.txt"):
        self.filename = filename

    def save_record(self, a: float, b: float, result: str):
        """Lưu lịch sử tính toán vào file txt kèm thời gian"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"[{now}] Phương trình: {a}x + ({b}) = 0  =>  {result}\n")