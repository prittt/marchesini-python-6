from functools import cache

def _sum_sq_digits(n: int) -> int:
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d * d
    return total


@cache
def is_happy(n: int) -> bool:
    if n == 1:
        return True
    if n == 4:
        return False
    return is_happy(_sum_sq_digits(n))


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

    for e in happy_numbers():
        print(e)