def intersection(a1, b1, c1, a2, b2, c2):
    """
    Finds an intersection point of two lines.
    >>> intersection(1, 2, 5, -1, 2, 3)
    (1.0, 2.0)
    >>> intersection(1, 1, 2, 1, 1, 3)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "/Users/myuser/Workspace/university-python/doctests/main.py", line 2, in intersection
        x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
    ZeroDivisionError: division by zero
    """
    x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
    y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
    return x, y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
