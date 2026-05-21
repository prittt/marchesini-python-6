from itertools import islice


def blocchi_v01(iterable, n: int, strict: bool = False):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    it = iter(iterable)
    while True:
        chunk = []
        for _ in range(n):
            try:
                chunk.append(next(it))
            except StopIteration:
                if chunk:
                    if strict:
                        raise ValueError(
                            f"L'ultimo blocco ha lunghezza {len(chunk)}, attesa {n}"
                        )
                    yield tuple(chunk)
                return
        yield tuple(chunk)


def blocchi_v02(iterable, n: int, strict: bool = False):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        if strict and len(chunk) < n:
            raise ValueError(
                f"L'ultimo blocco ha lunghezza {len(chunk)}, attesa {n}"
            )
        yield chunk


def blocchi_v03(iterable, n, *, strict=False):
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while chunk := tuple(islice(iterator, n)):
        if strict and len(chunk) != n:
            raise ValueError(
                f"L'ultimo blocco ha lunghezza {len(chunk)}, attesa {n}"
            )
        yield chunk

if __name__ == "__main__":
    for blocchi in (blocchi_v01, blocchi_v02, blocchi_v03):
        print(f"\n--- {blocchi.__name__} ---")
        print(list(blocchi(range(7), 3)))
        # [(0, 1, 2), (3, 4, 5), (6,)]
        print(list(blocchi("abcdef", 2)))
        # [('a', 'b'), ('c', 'd'), ('e', 'f')]
        print(list(blocchi([], 3)))
        # []
        print(list(blocchi([1, 2, 3, 4], 2, strict=True)))
        # [(1, 2), (3, 4)]
        try:
            print(list(blocchi([1, 2, 3], 2, strict=True)))
        except ValueError as e:
            print(e)
