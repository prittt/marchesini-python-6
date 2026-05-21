# Esercizio 6 - sum
# La funzione accetta una lista di int e ritorna la somma degli elementi.
# Nota: la funzione è chiamata 'sum', ma Python ha già un built-in con lo
# stesso nome; le versioni v3 e v4 lo usano esplicitamente.

from functools import reduce

def sum_v1(lst: list[int]) -> int:
    total = 0
    for x in lst:
        total += x
    return total


def sum_v2(lst: list[int]) -> int:
    total = 0
    [total := total + x for x in lst] 
    return total

import collections
def sum_v6(lst: list[int]) -> int:
    total = 0
    collections.deque((total := total + x for x in lst), maxlen=0)
    # for _ in (total := total + x for x in lst):
    #     pass
    return total

import builtins
builtins_sum = builtins.sum

def sum_v3(lst: list[int]) -> int:
    return builtins_sum(lst)


def sum_v4(lst: list[int]) -> int:
    if not lst:
        return 0
    return reduce(lambda a, b: a + b, lst)


import operator

def sum_v5(lst: list[int]) -> int:
    if not lst:
        return 0
    return reduce(operator.add, lst)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Input:", data)
    print("v1 (for):            ", sum_v1(data))
    print("v2 (walrus):         ", sum_v2(data))
    print("v3 (built-in sum):   ", sum_v3(data))
    print("v4 (reduce+lambda):  ", sum_v4(data))
    print("v5 (reduce+operator):", sum_v5(data))
    print("v6 (walrus+generator):", sum_v6(data))
