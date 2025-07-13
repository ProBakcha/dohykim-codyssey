def power(base, exponent):
    result = 1.0
    is_negative = exponent < 0
    exponent = abs(exponent)

    for _ in range(exponent):
        result *= base

    if is_negative:
        if base == 0:
            return "Undefined (division by zero)"
        return 1 / result
    return result

def main():
    try:
        number_input = input("Enter number: ")
        number = float(number_input)
    except ValueError:
        print("Invalid number input.")
        return

    try:
        exponent_input = input("Enter exponent: ")
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    result = power(number, exponent)
    
    if isinstance(result, float) and result.is_integer():
        print("Result:", int(result))
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
