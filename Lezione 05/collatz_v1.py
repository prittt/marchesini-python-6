def collatz(n: int):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1
    # return # raise StopIteration



if __name__ == "__main__":
    for value in collatz(27):
        print(value)
