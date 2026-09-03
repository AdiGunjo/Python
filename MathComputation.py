def get_numbers():
    n = int(input("Enter how many numbers you want to input: "))
    numbers = []
    for i in range(n):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)
    return numbers


def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def find_average(numbers):
    return find_sum(numbers) / len(numbers)


def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def main():
    numbers = get_numbers()
    print(f"\nNumbers entered: {numbers}")
    print(f"Sum = {find_sum(numbers):.2f}")
    print(f"Average = {find_average(numbers):.2f}")
    print(f"Minimum = {find_min(numbers)}")
    print(f"Maximum = {find_max(numbers)}")


if __name__ == "__main__":
    main()