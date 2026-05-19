# Esercizio 3 - filter_scores
# La funzione accetta una lista di int (punteggi) e ritorna una nuova
# lista contenente solo quelli maggiori della soglia thr.

def filter_scores_v1(lst: list[int], thr: int) -> list[int]:
    result = []
    for score in lst:
        if score > thr:
            result.append(score)
    return result


def filter_scores_v2(lst: list[int], thr: int) -> list[int]:
    return [score for score in lst if score > thr]


def filter_scores_v3(lst: list[int], thr: int) -> list[int]:
    return list(filter(lambda score: score > thr, lst))


def filter_scores_v4(lst: list[int], thr: int) -> list[int]:
    def above_threshold(score: int) -> bool:
        return score > thr
    return list(filter(above_threshold, lst))


if __name__ == "__main__":
    scores = [45, 80, 33, 92, 60, 71, 20, 88]
    threshold = 60

    print("Punteggi:            ", scores)
    print(f"Soglia: {threshold}")
    print("v1 (for):            ", filter_scores_v1(scores, threshold))
    print("v2 (comprehension):  ", filter_scores_v2(scores, threshold))
    print("v3 (filter+lambda):  ", filter_scores_v3(scores, threshold))
    print("v4 (filter+helper):  ", filter_scores_v4(scores, threshold))
