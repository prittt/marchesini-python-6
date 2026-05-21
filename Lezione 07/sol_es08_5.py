# Esercizio 5 - filter_palindromes
# La funzione accetta una lista di str e ritorna una nuova lista
# contenente solo gli elementi palindromi.

def filter_palindromes_v1(lst: list[str]) -> list[str]:
    result = []
    for word in lst:
        if word == word[::-1]:
            result.append(word)
    return result


def filter_palindromes_v2(lst: list[str]) -> list[str]:
    return [word for word in lst if word == word[::-1]]


def filter_palindromes_v3(lst: list[str]) -> list[str]:
    return list(filter(lambda word: word == word[::-1], lst))


def filter_palindromes_v4(lst: list[str]) -> list[str]:
    def is_palindrome(word: str) -> bool:
        normalized = word.lower()
        return normalized == normalized[::-1]
    return list(filter(is_palindrome, lst))


# --- Test ---
if __name__ == "__main__":
    data = ["radar", "hello", "level", "world", "madam", "Python",
            "racecar", "kayak", "Noon", "civic"]

    print("Input:", data)
    print("v1 (for):            ", filter_palindromes_v1(data))
    print("v2 (comprehension):  ", filter_palindromes_v2(data))
    print("v3 (filter+lambda):  ", filter_palindromes_v3(data))
    print("v4 (case-insensitive):", filter_palindromes_v4(data))
