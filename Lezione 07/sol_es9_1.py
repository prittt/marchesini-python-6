from collections import deque
from itertools import tee, islice


def finestre_v06(iterable, n: int):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    out = []
    for e in iterable:
        out.append(e)
        if len(out) == n:
            yield tuple(out)
            out.pop(0)
    return


def finestre_v07(iterable, n: int):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    out = deque()
    for e in iterable:
        out.append(e)
        if len(out) == n:
            yield tuple(out)
            out.popleft()
    return


# --- Soluzione 1: deque manuale ---
def finestre_v01(iterable, n: int):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    it = iter(iterable)
    window = deque()
    for _ in range(n):
        try:
            window.append(next(it))
        except StopIteration:
            return
    yield tuple(window)
    for item in it:
        window.popleft()
        window.append(item)
        yield tuple(window)


# --- Soluzione 2: itertools.tee ---
def finestre_v02(iterable, n: int):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    iterators = tee(iterable, n)
    for i, it in enumerate(iterators):
        for _ in range(i):
            next(it, None)
    return zip(*iterators)

    # iterators = (it1, it2, it3)
    # it1 =  1, 2, 3, 4
    # it2 =     2, 3, 4
    # it2 =        3, 4



# --- Soluzione 3: lista invece di deque ---
# Identica a v01 ma usa list.pop(0) invece di deque.popleft().
# pop(0) è O(n) perché sposta tutti gli elementi, popleft() è O(1).

def finestre_v03(iterable, n: int):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    it = iter(iterable)
    window = []
    for _ in range(n):
        try:
            window.append(next(it))
        except StopIteration:
            return
    yield tuple(window)
    for item in it:
        window.pop(0)
        window.append(item)
        yield tuple(window)


# --- Soluzione 4: islice su buffer (viola un vincolo e "consuma prima") ---
def finestre_v04(iterable, n: int):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    buf = list(iterable)
    for i in range(len(buf) - n + 1):
        yield tuple(islice(buf, i, i + n)) # islice funziona su qualunque iterabile


# --- Soluzione 5: zip su slices sfalsati (viola un vincolo e "consuma prima") ---
def finestre_v05(iterable, n: int):
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    seq = list(iterable)
    return zip(*(seq[i:] for i in range(n)))


if __name__ == "__main__":
    for finestre in (finestre_v01, finestre_v02, finestre_v03, finestre_v04, finestre_v05, finestre_v06, finestre_v07):
        print(f"\n--- {finestre.__name__} ---")
        
        for finestra in finestre([1, 2, 3, 4], 2):
            print(finestra, end=", ")
        print() 
        # (1, 2), (2, 3), (3, 4),
        # print(", ".join(str(f) for f in finestre([1, 2, 3, 4], 2)))

        print(list(finestre([1, 2, 3, 4], 2)))
        # [(1, 2), (2, 3), (3, 4)]
        print(list(finestre("python", 3)))
        # [('p', 'y', 't'), ('y', 't', 'h'), ('t', 'h', 'o'), ('h', 'o', 'n')]
        print(list(finestre([1, 2], 3)))
        # []
        print(list(finestre(range(-5,6), 2)))
        # [(-5, -4), (-4, -3), (-3, -2), (-2, -1), (-1, 0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
        print(list(finestre((a for a in [1, 2, 3, 4]), 2)))
        try:
            list(finestre([1, 2, 3], 0))
        except ValueError as e:
            print(e)
