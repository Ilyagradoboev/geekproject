diction = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open('eng_numbers.txt', 'r', encoding='utf-8') as f:
    string = []
    for line in f:
        for k, v in diction.items():
            line = line.replace(k, v)
        string.append(line)

print(string)

with open('rus_numbers.txt', 'w', encoding='utf-8') as f:
    f.writelines(string)