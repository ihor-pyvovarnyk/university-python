from contextlib import contextmanager

def gen():
    for val in range(2):
        yield val
    raise Exception('my error')


# @contextmanager
# def man():
#     try:
#         yield
#     except Exception:
#         pass

class Context():
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

def main():
    with Context():
        for val in gen():
            print(val)

main()