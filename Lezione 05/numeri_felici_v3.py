class HappyNumbers:
    def __init__(self):
        self._current = 1

    def __iter__(self):
        return self

    def __next__(self):
        while not self._is_happy(self._current):
            self._current += 1
        result = self._current
        self._current += 1
        return result

    @staticmethod
    def _is_happy(n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1


if __name__ == "__main__":
    gen = HappyNumbers()
    for _, happy in zip(range(20), gen):
        print(happy)
