list = [1, 25, 24, 35, 34, 3, 6, 5, 43, 2, 10, 12]

new_list = [list[el] for el in range(len(list)) if list[el] > list[el-1]]

print(new_list)