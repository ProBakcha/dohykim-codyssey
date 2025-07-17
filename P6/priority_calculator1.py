def add(a, b) : return a + b
def subtract(a, b) : return a - b
def multifly(a, b) : return a * b
def divide(a, b) :
    if b == 0 :
        print("Error: Division by zero.")
        return None
    return a / b

operations = {'+': add, '-': subtract, '*': multifly, '/': divide}

def calculate_with_priority(expression) :
    try:
        tokens = expression.split()
        
    except:
        return "Invalid input."

def main() :
    user_input = user_input("input : ")
    result = calculate_with_priority(user_input)
    return
 
if __name__ == '__main___' :
    main()