# 1. Use gmpy2 (GMP-backed) instead of decimal — orders of magnitude faster
# 2. pip install gmpy2 --break-system-packages

import gmpy2
from gmpy2 import mpz, mpfr

def compute_pi_gmpy(digits):
    gmpy2.get_context().precision = int(digits * 3.322) + 50  # digits -> bits
    C = 426880 * gmpy2.sqrt(mpfr(10005))
    K, M, X, L, S = mpz(6), mpz(1), mpz(1), mpz(13591409), mpfr(13591409)
    num_terms = digits // 14 + 2

    for i in range(1, num_terms):
        M = M * (K**3 - 16*K) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += mpfr(M * L) / mpfr(X)
        K += 12

    return C / S

# Example: 100,000 digits — still fast with gmpy2

pi_big = compute_pi_gmpy(100_000)
print(str(pi_big)[:50], "...")

# This module in itself is powerful to produce millions or even billions of digits of pi
# but for practical purposes, you might want to limit the output or write to a file instead of printing directly.
