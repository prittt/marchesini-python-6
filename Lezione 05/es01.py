# La funzione accetta una lista di stringhe e ritorna una nuova lista
# con le stesse stringhe convertite in maiuscolo.

def list_upper_v1(lst: list[str]) -> list[str]:
    result = []
    for s in lst:
        result.append(s.upper())
    return result


def list_upper_v2(lst: list[str]) -> list[str]:
    return [s.upper() for s in lst]


def list_upper_v3(lst: list[str]) -> list[str]:
    return list(map(str.upper, lst))


def list_upper_v4(lst: list[str]) -> list[str]:
    return list(map(lambda s: s.upper(), lst))


if __name__ == "__main__":
    data = ["hello", "world", "python", "exercises"]

    print("Input:       ", data)
    print("v1 (for):    ", list_upper_v1(data))
    print("v2 (comprehension):", list_upper_v2(data))
    print("v3 (map+str.upper):", list_upper_v3(data))
    print("v4 (map+lambda):", list_upper_v4(data))
