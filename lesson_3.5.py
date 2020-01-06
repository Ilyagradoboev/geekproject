result = 0
while (True):
    numbers = input("Введите числа, разделенные пробелом: ")
    if numbers == "stop":
        print(result)
        break
    else:
        list = numbers.split(" ")
        for i in list:
            result = result + int(i)
    print(result)
