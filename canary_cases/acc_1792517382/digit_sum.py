def digit_sum(n):
    """Return the sum of the decimal digits of abs(n)."""
    n = abs(n)
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total
