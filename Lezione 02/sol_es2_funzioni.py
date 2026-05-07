def double(n: float) -> float:
    return n * 2


def add_n(n: int) -> int:
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def gcd(n: int, m: int) -> int:
    while m != 0:
        n, m = m, n % m
    return n


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    # i = 2
    # while i * i <= n:
    #     if n % i == 0:
    #         return False
    #     i += 1
    # return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# double
doppio = float(input("Inserire il numero di cui calcolare il doppio: "))
print(f"The user input is {doppio=}") 
print("double(", doppio, ") = ", double(doppio), sep="")



# add_n
print("add_n(5) = ", add_n(5), sep="")

# gcd
print("gcd(594437, 588253) = ", gcd(594437, 588253), sep="")

# is_prime
print("is_prime(5) = ", is_prime(5), sep="")
print("is_prime(121) =", is_prime(121), sep="")

n = 6
prime = is_prime(n)
print(f"the number {n=} is ", "prime" if prime else "not prime", sep="")