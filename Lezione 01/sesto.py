def saluta(nome, cognome = '', saluto = 'Ciao') -> None:
    print(saluto, nome, cognome)

saluta('Costantino')
saluta('Costantino', 'Grana')
saluta('Costantino', 'Grana', 'Buongiorno')

saluta('Costantino', saluto='Buongiorno')
saluta('Costantino', cognome='Test', saluto='Buongiorno')
saluta(nome = 'Grana', cognome = 'Costantino')


