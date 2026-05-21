import csv
from collections import namedtuple

Persona = namedtuple('Persona', 'nome,età,altezza')
persone = [
    Persona('Giovanni', 18, 1.89),
    Persona('Marco', 27, 1.81),
    Persona('Luca', 56, 1.76),
]
for x in persone:
    #print(x[0], x[1], x[2])
    print(x.nome, x.età, x.altezza)


with open('pp-monthly-update-new-version.csv') as f:
    reader = csv.reader(f)
    Row = namedtuple('Row', next(reader))
    Stat = namedtuple('Stat', 'sum,count')
    stats = {}
    for row in reader:
        row = Row(*row)
        data = stats.get(row.county, Stat(0, 0))
        stats[row.county] = Stat(data.sum + int(row.price), data.count + 1)
        
    for county, data in sorted(stats.items()):
        print(f'{county}, {data.sum/data.count:.0f}')

# with open('pp-monthly-update-new-version.csv') as f:
#     reader = csv.DictReader(f)
#     stat = {}
#     for row in reader:
#         county = row['county']
#         price = int(row['price'])
#         data = stat.get(county, (0, 0))
#         stat[county] = (data[0] + price, data[1] + 1)
        
#     for county, data in sorted(stat.items()):
#         print(f'{county}, {data[0]/data[1]:.0f}')

# with open('pp-monthly-update-new-version.csv') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     stat = {}
#     for row in reader:
#         county = row[13]
#         price = int(row[1])
#         data = stat.get(county, (0, 0))
#         stat[county] = (data[0] + price, data[1] + 1)
        
#     for county, data in sorted(stat.items()):
#         print(f'{county}, {data[0]/data[1]:.0f}')
