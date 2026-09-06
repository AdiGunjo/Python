def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def main():
    print("Fibonacci Series using Recursion")
    terms = int(input("Enter number of terms: "))
    series = [fibonacci(i) for i in range(terms)]
    print(f"Fibonacci Series: {series}")

    print("\nGCD and LCM using Recursion")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"GCD of {a} and {b} = {gcd(a, b)}")
    print(f"LCM of {a} and {b} = {lcm(a, b)}")

    print("\nSum of Digits using Recursion")
    num = int(input("Enter a number: "))
    print(f"Sum of digits of {num} = {sum_of_digits(num)}")

    print("\nPower using Recursion")
    base = int(input("Enter base: "))
    exp = int(input("Enter exponent: "))
    print(f"{base}^{exp} = {power(base, exp)}")


if __name__ == "__main__":
    main()