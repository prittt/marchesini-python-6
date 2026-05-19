def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


def happy_numbers():
    n = 1
    while True:
        if is_happy(n):
            yield n
        n += 1


if __name__ == "__main__":
    gen = happy_numbers()
    for _ in range(20):
        print(next(gen))
