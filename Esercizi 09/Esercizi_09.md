## Esercizio 1 - Finestre scorrevoli

Nel file `finestre.py` implementare la funzione:

```python
def finestre(iterable, n):
    ...
```

La funzione deve produrre, in modo lazy, tutte le finestre consecutive di lunghezza `n`.
Ogni finestra deve essere restituita come tupla.

Esempi:

```python
list(finestre([1, 2, 3, 4], 2))
# [(1, 2), (2, 3), (3, 4)]

list(finestre("python", 3))
# [('p', 'y', 't'), ('y', 't', 'h'), ('t', 'h', 'o'), ('h', 'o', 'n')]

list(finestre([1, 2], 3))
# []
```

Vincoli:

- Se `n <= 0`, lanciare `ValueError`.
- Non usare indicizzazione sull'iterabile ricevuto: deve funzionare anche con generatori.
- Consumare al massimo `n` elementi di anticipo.
- Non modificare l'input se l'input è una lista.


## Esercizio 2 - Compressione di sequenze consecutive

Nel file `runs.py` implementare la funzione:

```python
def comprimi_runs(iterable):
    ...
```

La funzione deve raggruppare gli elementi consecutivi uguali e produrre coppie `(valore, numero_occorrenze_consecutive)`.
Ogni coppia deve essere una tupla.

Esempi:

```python
list(comprimi_runs([1, 1, 1, 2, 2, 3, 1, 1]))
# [(1, 3), (2, 2), (3, 1), (1, 2)]

list(comprimi_runs("aaabbcaaa"))
# [('a', 3), ('b', 2), ('c', 1), ('a', 3)]

list(comprimi_runs([]))
# []
```

Vincoli:

- La funzione deve essere lazy.
- Non usare `itertools.groupby` nella prima versione.
- Dopo avere completato la prima versione, scrivere anche `comprimi_runs_groupby()` usando `itertools.groupby`.


## Esercizio 3 - Blocchi lazy

Nel file `blocchi.py` implementare la funzione:

```python
def blocchi(iterable, n, strict=False):
    ...
```

La funzione deve leggere un iterabile e produrre tuple di lunghezza `n`.
L'ultimo blocco può essere più corto, salvo quando `strict=True`.

Esempi:

```python
list(blocchi(range(7), 3))
# [(0, 1, 2), (3, 4, 5), (6,)]

list(blocchi("abcdef", 2))
# [('a', 'b'), ('c', 'd'), ('è, 'f')]

list(blocchi([], 3))
# []
```

Caso con `strict=True`:

```python
list(blocchi([1, 2, 3, 4], 2, strict=True))
# [(1, 2), (3, 4)]

list(blocchi([1, 2, 3], 2, strict=True))
# ValueError, perchè l'ultimo blocco avrebbe lunghezza 1
```

Vincoli:

- Se `n <= 0`, lanciare `ValueError`.
- Non convertire l'intero iterabile in lista.
- La funzione deve funzionare anche con iteratori infiniti, almeno finché il chiamante consuma un numero finito di blocchi.
- Non usare `itertools.batched`.


## Esercizio 4 - Top-k in streaming

Nel file `topk.py` implementare:

```python
def top_k(iterable, k, key=None):
    ...
```

La funzione deve restituire i `k` elementi più grandi dell'iterabile, ordinati dal più grande al più piccolo.
Il parametro opzionale `key` funziona come in `sorted()`.

Esempi:

```python
top_k([5, 1, 9, 2, 7], 3)
# [9, 7, 5]

top_k([5, 1, 9], 10)
# [9, 5, 1]

top_k(["casa", "a", "python", "io"], 2, key=len)
# ["python", "casa"]
```

Vincoli:

- Se `k < 0`, lanciare `ValueError`.
- Se `k == 0`, restituire `[]`.
- Non ordinare tutto l'iterabile quando non è necessario.
- Usare al massimo memoria proporzionale a `k`, oltre all'input già ricevuto.
- Suggerimento: si può usare `heapq`.


## Esercizio 5 - Pipeline di log

Nel file `log_pipeline.py` implementare una piccola pipeline lazy per file di log testuali.

Il formato di ogni riga è:

```text
YYYY-MM-DD HH:MM:SS | LEVEL | user | message
```

Esempio:

```text
2026-05-20 09:15:02 | INFO | anna | login completato
2026-05-20 09:16:10 | ERROR | luca | file non trovato
2026-05-20 09:17:33 | WARNING | anna | spazio disco quasi pieno
```

Implementare:

```python
from datetime import datetime

def parse_log_line(line):
    ...

def read_logs(filename):
    ...

def filter_logs(records, level=None, user=None, start=None, end=None):
    ...

def count_by_level(records):
    ...

def last_messages(records, n):
    ...
```

`parse_log_line()` deve restituire un dizionario con queste chiavi:

```python
{
    "timestamp": datetime(...),
    "level": "INFO",
    "user": "anna",
    "message": "login completato",
}
```

Richieste:

- `parse_log_line()` deve lanciare `ValueError` se la riga non rispetta il formato.
- `read_logs()` deve aprire il file e produrre i record uno alla volta.
- `filter_logs()` deve essere lazy.
- `count_by_level()` deve consumare l'iterabile e produrre un dizionario, ad esempio `{"INFO": 10, "ERROR": 2}`.
- `last_messages()` deve restituire solo gli ultimi `n` messaggi senza tenere in memoria tutti i record se non necessario.
- Se `n < 0`, `last_messages()` deve lanciare `ValueError`.

Esempio di uso atteso:

```python
records = read_logs("app.log")
errors = filter_logs(records, level="ERROR")
print(count_by_level(errors))
```

## Esercizio 6 Merge ordinato

Nel file `merge_sorted.py` implementare:

```python
def merge_sorted(*iterables, key=None):
    ...
```

La funzione riceve più iterabili già ordinati e produce un unico iteratore ordinato.
Il parametro opzionale `key` funziona come in `sorted()`.

Esempi:

```python
list(merge_sorted([1, 4, 7], [2, 3, 9], [0, 8]))
# [0, 1, 2, 3, 4, 7, 8, 9]

list(merge_sorted(["a", "bbb"], ["cc", "dddd"], key=len))
# ["a", "cc", "bbb", "dddd"]
```

Vincoli:

- La funzione deve essere lazy.
- Non concatenare tutto e poi ordinare.
- Deve gestire anche iterabili vuoti.
