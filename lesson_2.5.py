my_list = [7, 5, 5, 3, 3, 2]
while True:
    my_list.append(int(input("Введите новый результат для рейтинга: ")))
    my_list.sort(reverse=1)
    my_list = my_list[:6]
    print(my_list)
