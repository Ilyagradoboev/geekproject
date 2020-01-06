def div(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("На ноль делить нельзя, введите другое число")


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

print(div(number1, number2))
