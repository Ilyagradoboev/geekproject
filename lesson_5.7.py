import json

with open('firm.txt', 'r', encoding='utf-8') as f:
    data = []
    for line in f:
        line = line.replace("\n", "")
        string = line.split(" ")
        data.append(string)

average = 0
avg_firms = 0
diction = {}
for el in data:
    profit = int(el[2]) - int(el[3])
    diction.update({el[0]:profit})
    if profit > 0:
        average = average + profit
        avg_firms += 1

average = average / avg_firms
avg_dict = {"Average profit": average}
summary = [diction, avg_dict]

with open('firm.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f)
