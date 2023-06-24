import random

import CheckNumbers


def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def matrix_initialize(a, b):
    matrix = []
    for i in range(a):
        matrix.append([0] * b)
    return matrix


def matrix_fill(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(1, 9)
    return matrix


def matrix_reverse(matrixA):
    matrixB = matrix_initialize(len(matrixA[0]), len(matrixA))
    for i in range(len(matrixB)):
        for j in range(len(matrixB[i])):
           matrixB[i][j] = matrixA[j][i]
    return matrixB


a = CheckNumbers.more("Введите число строк матрицы:", 0)
b = CheckNumbers.more("Введите число столбцов матрицы:", 0)
matrixA = matrix_fill(matrix_initialize(a, b))
print("\nСгенерирована матрица:")
matrix_print(matrixA)
matrixB = matrix_reverse(matrixA)
print("\nТранспонированная матрица:")
matrix_print(matrixB)
