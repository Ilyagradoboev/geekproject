goods = []
properties = ("название", "цена", "количество", "ед.")

for i in range(3):
    item = {}
    for element in properties:
        value = (input(f'Введите значение поля {element}:'))
        item[element] = value
    string = []
    string.append(i + 1)
    string.append(item)
    string = tuple(string)
    goods.append(string)

print(goods)

analys = []
for i in range(len(goods)):
    item = goods[i][1]
    analys.append(item)
result = {}
for d in analys:
    for k, v in d.items():
        if result.get(k) is None:
            result[k] = []
        if v not in result.get(k):
            result[k].append(v)
print(result)
