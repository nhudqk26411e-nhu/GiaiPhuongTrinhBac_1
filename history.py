from datetime import datetime

class TestHistoryManager:
    def __init__(self, filename="test_history.txt"):
        self.filename = filename

    def save_test_case(self, a: float, b: float, result: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"[{now}] Test case: a={a}, b={b} => {result}\n"
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(record)