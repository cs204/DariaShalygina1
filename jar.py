class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit negative cookies")
        if self._size + n > self._capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw negative cookies")
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
       return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not (type(capacity) is int and capacity > 0):
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not (type(size) is int and size >= 0 and size <= self.capacity):
            raise ValueError("size.proclees")
        self._size = size




