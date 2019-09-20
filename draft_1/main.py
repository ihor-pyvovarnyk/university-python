def is_balanced(text):
    """
    >>> is_balanced('(())()')
    True
    >>> is_balanced('(()()')
    False
    """
    level = 0
    for character in text:
        if character == '(':
            level += 1
        elif character == ')':
            level -= 1
    return level == 0


def intersection(a1, b1, c1, a2, b2, c2):
    """
    Finds an intersection point of two lines.
    >>> intersection(1, 2, 5, -1, 2, 3)
    (1.0, 2.0)
    """
    x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
    y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
    return x, y




class Stack:
    """
    >>> s = Stack(3)
    >>> s.push(1)
    >>> s.push(2)
    >>> s.pop()
    2
    >>> s.push(3)
    >>> s.push(4)
    >>> s.push(5)
    Traceback (most recent call last):
      ...
    Exception: Stack overflow
    """

    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, value):
        if len(self.stack) >= self.max_size:
            raise Exception('Stack overflow')
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()


def file_to_matrix(file, row_separator='\n', column_separator=' '):
    """
    >>> from io import StringIO
    >>> f1 = StringIO('1 2 3\\n4 5 6')
    >>> file_to_matrix(f1)
    [[1, 2, 3], [4, 5, 6]]
    >>> f2 = StringIO('1 2 3\\n4 5 6')
    >>> file_to_matrix(f2, ' ', '\\n')
    Traceback (most recent call last):
      ...
    Exception: Inconsistent matrix width
    """
    matrix = []
    content = file.read()
    rows = content.split(row_separator)
    width = len(rows[0].split(column_separator))
    for line in rows:
        row = [int(val) for val in line.split(column_separator)]
        if len(row) != width:
            raise Exception('Inconsistent matrix width')
        matrix.append(row)
    return matrix


def read_properties(file):
    """
    >>> from io import StringIO
    >>> f1 = StringIO('key1=value\\nkey2')
    >>> read_properties(f1)
    {'key1': 'value', 'key2': True}
    """
    properties = {}
    for line in file:
        equal_index = line.find('=')
        if equal_index == -1:
            key, value = line, True
        else:
            key = line[:equal_index]
            value = line[equal_index + 1:].rstrip('\n')
        properties[key] = value
    return properties


def read_properties_2(file):
    """
    >>> from io import StringIO
    >>> f1 = StringIO('key1=value\\nkey2=part1\\\\\\n\\tpart2')
    >>> read_properties_2(f1)
    {'key1': 'value', 'key2': 'part1part2'}
    """
    properties = {}
    line = next(file, '')
    while line:
        equal_index = line.find('=')
        if equal_index == -1:
            key, value = line, True
        else:
            key = line[:equal_index]
            value = line[equal_index + 1:].rstrip('\n')
            while value.endswith('\\'):
                value = value.rstrip('\\') + next(file, '').lstrip('\t')
        properties[key] = value
        line = next(file, '')
    return properties

