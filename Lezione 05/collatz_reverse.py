def collatz_reverse(n: int):
    if n != 1:
        next_n = n // 2 if n % 2 == 0 else 3 * n + 1
        yield from collatz_reverse(next_n)
    yield n


# def collatz_reverse_infinite():
#     n = 1
#     while True:
#         yield from collatz_reverse(n)
#         n += 1


if __name__ == "__main__":
    for value in collatz_reverse(6):
        print(value)
