list = []
length = int(input("Введите длину списка: "))
while length > 0:
    list.append(input("Введите элемент списка: "))
    length -= 1

for i in range(len(list)):
    if (i % 2 != 0):
        list[i], list[i - 1] = list[i - 1], list[i]

print(list)
