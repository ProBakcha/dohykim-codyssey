def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero.")
    return a / b

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculate_with_priority(expression):
    try:
        tokens = expression.split()
        if len(tokens) % 2 == 0 or not tokens:
            raise ValueError()
        
        nums = [float(tokens[i]) for i in range(0, len(tokens), 2)]
        ops = tokens[1::2]
        
        # 우선순위 처리: */ 먼저, +- 나중에
        for priority_ops in ['*/', '+-']:
            i = 0
            while i < len(ops):
                if ops[i] in priority_ops:
                    result = operations[ops[i]](nums[i], nums[i+1])
                    nums[i:i+2] = [result]  # 두 요소를 결과로 대체
                    ops.pop(i)
                else:
                    i += 1
        
        return nums[0]
    
    except ZeroDivisionError as e:
        return str(e)
    except:
        return "Invalid input."

def main():
    user_input = input("Enter expression: ").strip()
    result = calculate_with_priority(user_input)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()