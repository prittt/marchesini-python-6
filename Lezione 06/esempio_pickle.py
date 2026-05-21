import pickle

class Prova:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return str(self.x)
    def __repr__(self):
        return str(self)

# dati = {
#     'valore': 5,
#     'prova': Prova(7)
# }
# print(dati)
# pickle.dump(dati, open('prova.pkl', 'wb'))

dati_letti = pickle.load(open('prova.pkl', 'rb'))
print(dati_letti)