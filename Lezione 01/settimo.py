def modifica1(x):
    x = x + 1

def modifica2(x):
    x.append(4)


a = 6
modifica1(a)
print(a)

b = [1,2,3]
modifica2(b)
print(b)
