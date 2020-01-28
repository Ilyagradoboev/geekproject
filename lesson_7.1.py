matrix_list = [[1, 15, 18], [34, 36, 83], [2, 6, 93]]
matrix_list2 = [[1, 1, 1], [2, 2, 2], [1, 1, 1]]

class Matrix:
    def __init__(self, list):
        self.matrix = list

    def __str__(self):
        string = ''
        for el in self.matrix:
            for i in el:
                string = string + str(i) + '  '
            string = string + '\n'
        return string

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            y = []
            for a in range(len(self.matrix[i])):
                x = self.matrix[i][a] + other[i][a]
                y.append(x)
            result.append(y)
        self.matrix = result




matr = Matrix(matrix_list)
matr.__add__(matrix_list2)
print(matr)