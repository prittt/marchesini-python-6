from collections import deque

def _predecessors(m: int):
    yield 2 * m                        # even rule: 2m / 2 = m
    k = m - 1
    if k > 0 and k % 3 == 0:
        pred = k // 3
        if pred > 1 and pred % 2 == 1:  # must be odd and > 1
            yield pred                  # odd rule: 3*pred + 1 = m


def inverse_collatz_tree():
    queue = deque([1])
    while queue:
        n = queue.popleft()
        yield n
        for pred in _predecessors(n):
            queue.append(pred)


from functools import partial, reduce

def foo(x, y):
    return x*y


if __name__ == "__main__":
    # for value in inverse_collatz_tree():
    #     print(value)

    foo_specialized = partial(foo, y=5)
    foo_specialized(4)
    
    val = reduce(lambda x, y: x * y, [1, 2, 3, 4])
    print(val)

    val = reduce(lambda x, y: x + y, [1, 2, 3, 4])
    print(val)

    pass



