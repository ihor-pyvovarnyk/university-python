def intersection(a1, b1, c1, a2, b2, c2):
    """Finds an intersection point of two lines."""
    try:
        x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
        y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
        return x, y
    except ZeroDivisionError:
        return 0, 0

if __name__ == "__main__":
    import doctest
    doctest.testfile('./test_v7.txt')
