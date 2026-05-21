from itertools import groupby

def comprimi_runs_v01(iterable):
    it = iter(iterable)
    try:
        current = next(it)
        count = 1
    except StopIteration:
        return
    for item in it:
        if item == current:
            count += 1
        else:
            yield (current, count)
            current = item
            count = 1
    yield (current, count)


def comprimi_runs_v02(iterable):
    for key, group in groupby(iterable):
        yield (key, sum(1 for _ in group))


def comprimi_runs_v03(iterable):
    for key, group in groupby(iterable):
         yield (key, len(list(group)))


if __name__ == "__main__":
    for comprimi_runs in (comprimi_runs_v01, comprimi_runs_v02, comprimi_runs_v03):
        print(f"\n--- {comprimi_runs.__name__} ---")
        print(list(comprimi_runs([1, 1, 1, 2, 2, 3, 1, 1])))
        # [(1, 3), (2, 2), (3, 1), (1, 2)]
        
        for item in comprimi_runs([1, 1, 1, 2, 2, 3, 1, 1]):
            print(item, end=", ")
            # (1, 3), (2, 2), (3, 1), (1, 2),

        print(list(comprimi_runs("aaabbcaaa")))
        # [('a', 3), ('b', 2), ('c', 1), ('a', 3)]
        print(list(comprimi_runs([])))
        # []
