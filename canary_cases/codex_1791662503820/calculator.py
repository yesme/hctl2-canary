def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a signed integer quotient using integer arithmetic."""
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    return -(-numerator // denominator)
