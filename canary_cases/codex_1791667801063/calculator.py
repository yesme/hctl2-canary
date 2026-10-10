def ceil_div(numerator: int, denominator: int) -> int:
    """Return the ceiling of numerator / denominator using integer arithmetic."""
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    return -(-numerator // denominator)
