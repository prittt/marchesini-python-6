# Esercizio 2 - list_round
# La funzione accetta una lista di float e ritorna una nuova lista con
# gli stessi numeri arrotondati ad un numero di cifre pari alla loro
# posizione (il primo elemento a 0 cifre, il secondo a 1, ecc.).

def list_round_v1(lst: list[float]) -> list[float]:
    result = []
    for i, val in enumerate(lst):
        result.append(round(val, i))
    return result


def list_round_v2(lst: list[float]) -> list[float]:
    return [round(val, i) for i, val in enumerate(lst)]


def list_round_v3(lst: list[float]) -> list[float]:
    return list(map(lambda pair: round(pair[1], pair[0]), enumerate(lst)))


def list_round_v5(lst: list[float]) -> list[float]:
    return list(map(lambda pair: round(pair[0], pair[1]), zip(lst, range(len(lst)))))


# Buuu
def list_round_v6(lst: list[float]) -> list[float]:
    return list(map(lambda x: round(x, lst.index(x)), lst))


from itertools import count
def list_round_v7(lst: list[float]) -> list[float]:
    c = count()
    return list(map(lambda x: round(x, next(c)), lst))


def list_round_v9(lst: list[float]) -> list[float]:
    i = [0]
    return list(map(lambda x: round(x, i[0]) if not i.__setitem__(0, i[0] + 1) else None, lst))

# def list_round_v9(lst: list[float]) -> list[float]:
#     i = 0
#     return list(map(lambda x: round(x, i:= i + 1), lst))


from itertools import starmap

def list_round_v4(lst: list[float]) -> list[float]:
    return list(starmap(round, zip(lst, range(len(lst)))))


def list_round_v8(lst: list[float]) -> list[float]:
    return list(map(round, lst, range(len(lst))))


if __name__ == "__main__":
    data = [3.14159, 2.71828, 1.41421, 1.73205, 1.73205, 1.73205, 0.57721]

    print("Input:                  ", data)
    print("v1 (for+enumerate):     ", list_round_v1(data))
    print("v2 (comprehension):     ", list_round_v2(data))
    print("v3 (map+zip):           ", list_round_v3(data))
    print("v4 (starmap):           ", list_round_v4(data))
    print("v5 (map+enumerate):     ", list_round_v5(data))
    print("v6 (porcata):           ", list_round_v6(data))
    print("v7 (count):             ", list_round_v7(data))
    print("v8 (map with multi its):", list_round_v8(data))
    print("v9 (porcata**porcata):  ", list_round_v9(data))


# i = 5.8
# print(i.__trunc__())
# pass