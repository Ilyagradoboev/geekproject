with open('staff.txt', 'r', encoding='utf-8') as f:
    diction = {}
    for line in f:
        line = line.replace("\n", "")
        string = line.split(" ")
        diction.update({string[0]: string[1]})

print(diction)
all = 0
for v in diction.values():
    all = all + int(v)
print(f'Средняя заработная плата равна: {all / len(diction)}')

print('Сотрудники с зарплатой ниже 20000: ')
for k,v in diction.items():
    if int(v) < 20000:
        print(k)
