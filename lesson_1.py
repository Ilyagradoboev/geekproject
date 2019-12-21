command = int(input("Введите номер задания для проверки(1-6): "))

if command == 1:
    a = 6
    b = 15
    print(a)
    print(b)
    number = int(input("Введите число: "))
    print(number)
    string = input("Введите строку: ")
    print(string)
elif command == 2:
    time = int(input("Введите время в секундах: "))
    hours = time // 3600
    minutes = time % 3600 // 60
    seconds = time % 3600 % 60
    print(f'Время в формате чч:мм:сс {hours}:{minutes}:{seconds}')
elif command == 3:
    number = int(input("Введите число: "))
    print("Выводим сумму чисел n + nn + nnn")
    print(int(str(number) + str(number) + str(number)) + int(str(number) + str(number)) + number)
elif command == 4:
    number = input("Введите число для поиска наибольшей цифры: ")
    max_number = 0
    i = 0
    while i < len(number):
        if int(number[i]) > max_number:
            max_number = int(number[i])
        i += 1
    print(max_number)

elif command == 5:
    income = int(input("Введите данные о выручке фирмы: "))
    cost = int(input("Введите данные о издержках фирмы: "))
    if income > cost:
        print("Ваша фирма приносит прибыль!")
        rent = income / cost
        print("Показатель рентабельности: ", rent)
        staff = int(input("Введите данные о количестве сотрудников: "))
        staff_income = (income - cost) / staff
        print(f'Прибыль на одного сотрудника составляет {staff_income}')

    elif income < cost:
        print("Ваша фирма работает в убыток!")
    else:
        print("Ваша фирма работает в ноль!")
elif command == 6:
    a = int(input("Введите количество километров, которые пробежал спортсмен в первый день: "))
    b = int(input("Введите результат в километрах, который он хочет достичь: "))
    day = 1
    while a < b:
        a = a * 1.1
        day += 1
    print(f'Он достигент желаемого результата за {day} дней.')
else:
    print("Такого номера не существует. Задания имеют нумерацию с 1 по 6")
