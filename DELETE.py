class InfinityIterator:
    """
    The class returns an infinite sequence of even numbers
    """
    def __init__(self, n_max=10000000):
        self.n_max = n_max

    def __iter__(self):
        self.n = -2
        return self

    def __next__(self):
        if self.n < self.n_max:
            self.n += 2
            return self.n
        else:
            raise StopIteration


ex = InfinityIterator()
for idx, value in enumerate(ex):
    print(idx, value)

