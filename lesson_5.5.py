string = input("Введите числа, разделенные пробелом: ")

with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write(string)

with open('numbers.txt', 'r', encoding='utf-8') as f:
    new_string = f.read()
new_string = new_string.split(' ')
summary = 0
for el in new_string:
    summary = summary + int(el)
print(summary)