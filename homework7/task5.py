"""
Пример работы с библиотекой numpy.
Создание матрицы 3 на 3, заполненной случайными числами.
Транспонирование матрицы.
"""
import numpy
array = numpy.random.sample((3, 3))
print("Исходная матрица 3 * 3:")
print(array)
print()
print("Транспонировання матрица 3 * 3:")
print(array.transpose())
