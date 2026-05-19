# Esercizio 4 - filter_scores con nomi
# La funzione accetta una lista di punteggi (int) e una lista di nomi (str).
# Ritorna due nuove liste contenenti solo i punteggi e i nomi dei personaggi
# il cui punteggio è maggiore della soglia thr.

def filter_scores_v1(
    lst_scores: list[int], lst_names: list[str], thr: int
) -> tuple[list[int], list[str]]:
    scores_out = []
    names_out = []
    for score, name in zip(lst_scores, lst_names):
        if score > thr:
            scores_out.append(score)
            names_out.append(name)
    return scores_out, names_out


def filter_scores_v2(
    lst_scores: list[int], lst_names: list[str], thr: int
) -> tuple[list[int], list[str]]:
    pairs = [(s, n) for s, n in zip(lst_scores, lst_names) if s > thr]
    if not pairs:
        return [], []
    # pairs = [(1, "a"), (2, "b"), (3, "c"))]
    scores_out, names_out = zip(*pairs)
    # print(type(scores_out), type(names_out))
    return list(scores_out), list(names_out)


def filter_scores_v5(
    lst_scores: list[int], lst_names: list[str], thr: int
) -> tuple[list[int], list[str]]:
    return [s for s, _ in zip(lst_scores, lst_names) if s > thr], [n for s, n in zip(lst_scores, lst_names) if s > thr]


def filter_scores_v3(
    lst_scores: list[int], lst_names: list[str], thr: int
) -> tuple[list[int], list[str]]:
    pairs = list(filter(lambda sn: sn[0] > thr, zip(lst_scores, lst_names)))
    if not pairs:
        return [], []
    scores_out, names_out = zip(*pairs)
    return list(scores_out), list(names_out)


def filter_scores_v4(
    lst_scores: list[int], lst_names: list[str], thr: int
) -> tuple[list[int], list[str]]:
    mask = list(map(lambda s: s > thr, lst_scores))
    scores_out = [s for s, keep in zip(lst_scores, mask) if keep]
    names_out  = [n for n, keep in zip(lst_names, mask) if keep]
    return scores_out, names_out


if __name__ == "__main__":
    scores = [45, 80, 33, 92, 60, 71, 20, 88]
    names  = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Heidi"]
    threshold = 60

    print("Punteggi:", scores)
    print("Nomi:    ", names)
    print(f"Soglia: {threshold}\n")

    for i, fn in enumerate([filter_scores_v1, filter_scores_v2,
                             filter_scores_v3, filter_scores_v4], 1):
        s, n = fn(scores, names, threshold)
        print(f"v{i}: punteggi={s}, nomi={n}")