class digitsOnly(Exception):
    def __str__(self):
        return 'Строка содержит не только числа!'


list = []
while True:
    number = input("Введите число: ")
    if number == 'stop':
        break
    try:
        for i in number:
            if i.isdigit():
                pass
            else:
                raise digitsOnly(0)
    except digitsOnly as e:
        print(e)
    else:
        number = int(number)
        list.append(number)

print(list)
