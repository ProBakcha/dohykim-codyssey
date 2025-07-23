def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error : Division by zero.")
    return a / b

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculate_with_priority(tokens):
    try:
        nums = [float(tokens[i]) for i in range(0, len(tokens), 2)]
        ops = tokens[1::2]

        if any(op not in operations for op in ops):
            raise ValueError()
        
        for priority_ops in ['*/', '+-']:
            i = 0
            while i < len(ops):
                if ops[i] in priority_ops:
                    result = operations[ops[i]](nums[i], nums[i+1])
                    nums[i:i+2] = [result]
                    ops.pop(i)
                else:
                    i += 1
        return nums[0]
    
    except ZeroDivisionError as e:
        return str(e)
    except:
        return "Invalid input."

def main():
    user_input = input("input : ").split()
    result = calculate_with_priority(user_input)
    print(result)
 
if __name__ == '__main__':
    main()