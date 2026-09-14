from decimal import Decimal, getcontext

def compute_pi(digits):
    """
    Computes pi to the given number of decimal digits using the
    Chudnovsky algorithm.
    """
    getcontext().prec = digits + 15  
    C = 426880 * Decimal(10005).sqrt()
    K = Decimal(6)
    M = Decimal(1)
    X = Decimal(1)
    L = Decimal(13591409)
    S = L

    # Each term adds ~14 correct digits, so this many terms
    # comfortably covers the requested precision.

    num_terms = digits // 14 + 2

    for i in range(1, num_terms):
        M = M * (K**3 - 16*K) / (i**3)
        L += 545140134
        X *= -262537412640768000
        S += (M * L) / X
        K += 12

    pi = C / S
    getcontext().prec = digits  
    return +pi  


# Example: compute pi to 1,000 digits

digits_wanted = 1000
pi_value = compute_pi(digits_wanted)
pi_str = str(pi_value)

print(f"Pi to {digits_wanted} digits:")
print(pi_str)
print(f"\nTotal characters generated: {len(pi_str)}")