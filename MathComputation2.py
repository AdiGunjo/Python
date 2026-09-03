def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num


def factorial(num):
    if num < 0:
        return None
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def main():
    num = int(input("Enter a number: "))

    print(f"\nIs {num} a prime number? {'Yes' if is_prime(num) else 'No'}")
    print(f"Is {num} an Armstrong number? {'Yes' if is_armstrong(num) else 'No'}")

    fact = factorial(num)
    if fact is not None:
        print(f"Factorial of {num} = {fact}")
    else:
        print("Factorial is not defined for negative numbers")

    print(f"Square of {num} = {square(num)}")
    print(f"Cube of {num} = {cube(num)}")


if __name__ == "__main__":
    main()