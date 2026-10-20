def clamp_abs(x, lo, hi):
    """Clamp the signed integer x to the inclusive interval [lo, hi]."""
    return max(lo, min(x, hi))
