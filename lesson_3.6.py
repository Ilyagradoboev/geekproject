def int_func(text):
    return text.title()

print(int_func("привет"))

string = input("Введите строку в нижнем регистре, разделитель - пробелы: ")
list = []
list = string.split(" ")
string = ""
for i in list:
    string = string + int_func(i) + " "

print(string)
