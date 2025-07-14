def main():
    user_input = input("Input numbers: ")

    try:
        numbers = [float(num) for num in user_input.split()]
    except ValueError:
        print("Invalid input.")
        return

    if not numbers:
        print("Invalid input.")
        return

    minimum = maximum = numbers[0]

    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    print(f"Min: {minimum}, Max: {maximum}")

if __name__ == "__main__":
    main()
