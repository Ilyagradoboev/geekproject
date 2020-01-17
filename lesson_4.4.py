import itertools

list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [el for n, el in enumerate(list) if el not in list[:n]]

print(new_list)
