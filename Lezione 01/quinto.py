def area_triangolo(b, h):
    return b * h / 2

print("Calcolatore dell'area del triangolo")
print("-----------------------------------")
base = float(input('Base: '))
altezza = float(input('Altezza: '))

area = area_triangolo(base, altezza)

print("L'area è", area)
print("Se la base fosse 17 l'area sarebbe", area_triangolo(17, altezza))
print("Se l'altezza fosse 17 l'area sarebbe", area_triangolo(base, 17))
