"""Integer arithmetic helpers."""


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of the quotient of two signed integers."""
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    return -(-numerator // denominator)
