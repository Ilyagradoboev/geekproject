import itertools


def int_numbers(start):
    for el in itertools.count(start):
        if el > 50:
            break
        else:
            print(el)

list = ["Привет", "Пока", "Давай до свидания"]
def repeat_list(list):
    c = 0
    for el in itertools.cycle(list):
        if c > 20:
            break
        print(el)
        c += 1

repeat_list(list)
int_numbers(7)


