# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        for line in self.matrix:
            return '\n'.join([' '.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            result = []
            row_len = len(self.matrix[0])
            for (line1, line2) in zip(self.matrix, other.matrix):
                if len(line1) == row_len and len(line2) == row_len:
                    curr_el = []
                    for el1, el2 in zip(line1, line2):
                        curr_el.append(el1 + el2)
                    result.append(curr_el)
                else:
                    return 'One of matrices is not rectangle'
            return Matrix(result)
        else:
            return 'Matrices are not same length'


matrix1 = [[1, 2], [-2, 4], [8, 5]]
matrix2 = [[7, 4], [5, 4], [-1, 7]]
mtr1 = Matrix(matrix1)
print(mtr1)
mtr2 = Matrix(matrix2)
mtr3 = mtr1 + mtr2
print(mtr3)
