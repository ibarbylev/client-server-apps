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


import csv

ll = [[1, 2, 3, 'abc'], [1, 2, 3, 'abc']]
with open('ttt.csv', 'w', newline='') as f:
    csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=';').writerows(ll)

with open('ttt.csv') as f:
    data = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    print(list(data))
