text = input("Введите текст: ")

list = text.split(' ')
print(list)

with open('lesson.txt', "w") as f:
    for el in list:
        f.write(el)
        f.write("\n")

