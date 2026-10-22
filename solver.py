def solve_linear_equation(a: float, b: float) -> str:
    """
    Giải phương trình bậc 1 dạng ax + b = 0
    """
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        # Làm tròn kết quả đến 2 chữ số thập phân
        return f"Nghiệm: X = {x:.2f}"