def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    try:
        a = int(float(input("첫 번째 실수 입력: ")))
        b = int(float(input("두 번째 실수 입력: ")))
        op = input("연산자 (+, -, *, /)를 입력하세요: ")

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            if b == 0:
                print("Error: Division by zero.")
                exit()
            result = divide(a, b)
        else:
            print("Invalid operator.")
            exit()

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter integers only.")
