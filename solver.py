def validate_number(val_str: str, name: str) -> float:
    if not val_str or val_str.strip() == "":
        raise ValueError(f"Vui lòng nhập giá trị cho {name}!")
    try:
        return float(val_str.strip())
    except ValueError:
        raise ValueError(f"{name} phải là một số thực hợp lệ!")


def solve_linear_equation(a: float, b: float) -> str:
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        return "Phương trình vô nghiệm"

    x = -b / a
    return f"Phương trình có nghiệm duy nhất: X = {x:.2f}"