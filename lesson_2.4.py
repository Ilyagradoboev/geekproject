phrase = input("Введите слова через пробел: ")
list = phrase.split(" ")
for i, el in enumerate(list, start=1):
    print(i, el[:10])
