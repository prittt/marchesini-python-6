def numbers(max):
    i = 0
    while i <= max:
        yield i
        i += 1


a = numbers(5)
print(next(a))
print(next(a))
print(next(a))
