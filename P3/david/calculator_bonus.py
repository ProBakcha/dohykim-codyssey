def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def auto_mode_calculator(user_input):
    try:
        op = next((o for o in operations if o in user_input), None)

        if op:  # expression 모드
            left, right = user_input.split(op)
            a, b = int(float(left.strip())), int(float(right.strip()))
        else:  # basic 모드
            a = int(float(user_input))
            b = int(float(input("input2: ")))
            op = input("input operator(+, -, *, /): ").strip()

        func = operations.get(op)
        if not func:
            print("Invalid operator.")
            return

        result = func(a, b)
        if result is not None:
            print(f"Result: {result}")

    except ValueError:
        print("Invalid number input.")
    except Exception:
        print("An error occurred.")

if __name__ == "__main__":
    user_input = input("input1: ").strip()
    auto_mode_calculator(user_input)
