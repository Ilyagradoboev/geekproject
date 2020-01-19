with open('lesson.txt', "r") as f:
    text = f.readlines()
print(text)
print(f"Количество строк в файле: {len(text)}")
n = 0
for el in text:
    n += 1
    print(f"Количество печатаемых символов в строке {n}: {len(el) - 1}")
