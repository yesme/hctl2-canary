def sign_abs(x: int) -> int:
    """Return the absolute value of x multiplied by its sign."""
    return (1 if x >= 0 else -1) * abs(x)
