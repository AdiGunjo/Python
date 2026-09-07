def calculate_commission(sales, rate):
    return (sales * rate) / 100


def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def calculate_compound_interest(principal, rate, time, n=1):
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    interest = amount - principal
    return amount, interest


def main():
    print("Commission Calculator")
    sales = float(input("Enter total sales amount: "))
    rate = float(input("Enter commission rate (%): "))
    commission = calculate_commission(sales, rate)
    print(f"Commission = {commission:.2f}\n")

    print("Simple Interest Calculator")
    principal = float(input("Enter principal amount: "))
    si_rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter time period (years): "))
    si = calculate_simple_interest(principal, si_rate, time)
    print(f"Simple Interest = {si:.2f}\n")

    print("Compound Interest Calculator")
    ci_principal = float(input("Enter principal amount: "))
    ci_rate = float(input("Enter rate of interest (%): "))
    ci_time = float(input("Enter time period (years): "))
    n = int(input("Enter compounding frequency per year: "))
    amount, ci = calculate_compound_interest(ci_principal, ci_rate, ci_time, n)
    print(f"Amount = {amount:.2f}")
    print(f"Compound Interest = {ci:.2f}")


if __name__ == "__main__":
    main()