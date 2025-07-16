##
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    user_input = input("Input numbers: ")

    try:
        numbers = [float(num) for num in user_input.strip().split()]
    except ValueError:
        print("Invalid input.")
        return

    if not numbers:
        print("Invalid input.")
        return

    sorted_numbers = bubble_sort(numbers)
    print("Sorted:", *sorted_numbers)

if __name__ == "__main__":
    main()
