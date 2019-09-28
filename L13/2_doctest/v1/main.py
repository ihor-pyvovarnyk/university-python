def intersection(a1, b1, c1, a2, b2, c2):
    """Finds the intersection point of two lines."""
    x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
    y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
    return x, y