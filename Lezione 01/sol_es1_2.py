testo = input('Dammi un numero intero: ')
numero = int(testo)

somma = 0

# i = 1
# while i <= numero:
#     somma += somma + i
#     i = i + 1

for i in range(1, numero + 1):
    somma += somma + i

# somma = sum(range(1, numero + 1))

print('La somma dei numeri da 1 a ', numero, 'è', somma)