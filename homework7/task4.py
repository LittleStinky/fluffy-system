"""
Пример работы с модулем os.
"""
import os
print("Имя операционной сисетмы:", os.name)
print("Имя пользователя, вошедшего в терминал:", os.getlogin())
print("Список папок и файлов, лежащих в текущем рабочем каталоге:", os.listdir())
