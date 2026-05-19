class Collatz:
    def __init__(self, n: int):
        self._current = n
        self._done = False

    def __iter__(self):
        return self

    def __next__(self):
        if self._done:
            raise StopIteration
        value = self._current
        if self._current == 1:
            self._done = True
        elif self._current % 2 == 0:
            self._current = self._current // 2
        else:
            self._current = 3 * self._current + 1
        return value


class CollatzReversed:
    def __init__(self, n: int):
        self._values = reversed([val for val in Collatz(n)])
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # value = self._values[self._index]
        # if self._index < len(self._values):
        #     self._index += 1
        #     return value
        # else:
        #     raise StopIteration
        for e in self._values:
            return e
        raise StopIteration


# def foo_gen_2():
#     yield from [1, 2, 3, 4]

# def foo_gen():
#     yield from foo_gen_2()


if __name__ == "__main__":
    for value in Collatz(6):
        print(value)

    # for e in foo_gen():
    #     print(e)
