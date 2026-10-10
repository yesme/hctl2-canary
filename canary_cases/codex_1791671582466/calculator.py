"""Integer arithmetic helpers."""


def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of a signed integer quotient."""
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    return -(-numerator // denominator)
