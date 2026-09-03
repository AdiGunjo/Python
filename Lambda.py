from functools import reduce


def get_numbers():
    n = int(input("Enter number of elements: "))
    numbers = []
    for i in range(n):
        value = int(input(f"Enter number {i + 1}: "))
        numbers.append(value)
    return numbers


def demonstrate_lambda(numbers):
    square = lambda x: x ** 2
    squared_numbers = [square(x) for x in numbers]
    print(f"Squares using lambda: {squared_numbers}")


def demonstrate_map(numbers):
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"Doubled using map: {doubled}")


def demonstrate_filter(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers using filter: {even_numbers}")


def demonstrate_reduce(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Sum using reduce: {total}")
    print(f"Product using reduce: {product}")


def demonstrate_combined(numbers):
    result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
    print(f"Sum of squares of even numbers (map+filter+reduce): {result}")


def main():
    numbers = get_numbers()
    print(f"\nOriginal numbers: {numbers}")
    demonstrate_lambda(numbers)
    demonstrate_map(numbers)
    demonstrate_filter(numbers)
    demonstrate_reduce(numbers)
    demonstrate_combined(numbers)


if __name__ == "__main__":
    main()