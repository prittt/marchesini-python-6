import statistics
#import timer_wrapper as tw

# from timer_wrapper import timer as t, other_name
# from timer_wrapper import *
import timer_wrapper

def media_v01(lst: list) -> float:
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
        i += 1
    return total / len(lst)


def media_v02(lst: list) -> float:
    total = 0
    for x in lst:
        total += x
    return total / len(lst)


def media_v03(lst: list) -> float:
    return sum(lst) / len(lst)


def varianza_v01(lst: list) -> float:
    m = media_v03(lst)
    total = 0
    i = 0
    while i < len(lst):
        total += (lst[i] - m) ** 2
        i += 1
    return total / len(lst)


def varianza_v02(lst: list) -> float:
    m = media_v03(lst)
    total = 0
    for x in lst:
        total += (x - m) ** 2
    return total / len(lst)


def varianza_v03(lst: list) -> float:
    m = media_v03(lst)
    return sum([(x - m) ** 2 for x in lst]) / len(lst)


def varianza_v04(lst: list) -> float:
    return statistics.pvariance(lst)


def ribalta_v01(lst: list) -> list:
    result = []
    i = len(lst) - 1
    while i >= 0:
        result.append(lst[i]) # result += [lst[i]]
        i -= 1
    return result
    # if (isinstance(lst,tuple)):
    #     result = tuple(result)
    # return result


def ribalta_v02(lst: list) -> list:
    return lst[::-1]


def ribalta_v03(lst: list) -> list:
    return list(reversed(lst))


def potenze_v01(base: float, maxesp: int) -> list:
    result = []
    esp = 1
    while esp <= maxesp:
        result.append(base ** esp) # result += [base ** esp]
        esp += 1
    return result


def potenze_v02(base: float, maxesp: int) -> list:
    result = []
    for esp in range(1, maxesp + 1):
        result.append(base ** esp)
    return result


def potenze_v03(base: float, maxesp: int) -> list:
    return [base ** esp for esp in range(1, maxesp + 1)]


# O(n log n)
def nodup_v01(lst: list) -> list:
    if not lst:
        return []
    #sorted_lst = lst.copy()
    #sorted_lst.sort()
    sorted_lst = sorted(lst)
    result = [sorted_lst[0]]
    i = 1
    while i < len(sorted_lst):
        if sorted_lst[i] != sorted_lst[i - 1]:
            result.append(sorted_lst[i])
        i += 1
    return result


# O(n²)
def nodup_v02(lst: list) -> list:
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result


# O(n) average
def nodup_v03(lst: list) -> list:
    return list(set(lst))


def nodup_ord_v02(lst: list) -> list:
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


nums = [2, 4, 4, 4, 5, 5, 7, 9]
dup  = [4, 1, 1, 4, 7, 9, 7]

print("=== media ===")
print(f"v01: {media_v01(nums)}")   # 5.0
print(f"v02: {media_v02(nums)}")
print(f"v03: {media_v03(nums)}")

print("\n=== varianza ===")
print(f"v01: {varianza_v01(nums)}")  # 4.0
print(f"v02: {varianza_v02(nums)}")
print(f"v03: {varianza_v03(nums)}")
print(f"v04: {varianza_v04(nums)}")

print("\n=== ribalta ===")
print(f"v01: {ribalta_v01([1, 2, 3, 4, 5])}")
print(f"v02: {ribalta_v02([1, 2, 3, 4, 5])}")
print(f"v03: {ribalta_v03([1, 2, 3, 4, 5])}")

print("\n=== potenze ===")
print(f"v01: {potenze_v01(2, 5)}")  # [2, 4, 8, 16, 32]
print(f"v02: {potenze_v02(2, 5)}")
print(f"v03: {potenze_v03(2, 5)}")

print("\n=== nodup (ordine qualsiasi) ===")
print(f"v01: {nodup_v01(dup)}")  # [1, 4, 7, 9]
print(f"v02: {nodup_v02(dup)}")
print(f"v03: {nodup_v03(dup)}")

print("\n=== nodup_ord (ordine primo inserimento) ===")
print(f"v02: {nodup_ord_v02(dup)}")

# ── Stress test ───────────────────────────────────────────────────────────────
import random

random.seed(42)
stress = [random.randint(0, 500) for _ in range(100_000)]

print(f"\n=== stress test (n={len(stress)}, unique={len(set(stress))}) ===")

@timer
def _nodup_v01_stress(lst): return nodup_v01(lst)

@timer
def _nodup_v02_stress(lst): return nodup_v02(lst)

@timer
def _nodup_v03_stress(lst): return nodup_v03(lst)

r1 = _nodup_v01_stress(stress)
r2 = _nodup_v02_stress(stress)
r3 = _nodup_v03_stress(stress)

print(f"v01 unique count: {len(r1)}")
print(f"v02 unique count: {len(r2)}")
print(f"v03 unique count: {len(r3)}")