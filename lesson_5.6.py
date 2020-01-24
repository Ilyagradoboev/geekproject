with open('edu.txt', 'r', encoding='utf-8') as f:
    data = []
    for line in f:
        line = line.replace("\n", "")
        line = line.replace(":", "")
        string = line.split(" ")
        data.append(string)

diction = {}
for el in data:
    summary = 0
    for v in el[1:]:
        number = ''
        for i in v:
            if i.isdigit():
                number = number + i
        if number.isnumeric():
            number = int(number)
            summary = summary + number
    diction.update({el[0]: summary})

print(diction)
