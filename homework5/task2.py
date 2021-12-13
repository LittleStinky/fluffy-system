def sum(*args):
    """
    Функция принимает сколько угодно аргументов.
    Функция возвращает их сумму.
    """
    print(args)
    if len(args) == 0:
        rez = 0
    else:
        rez = args[0]
        for i in range(1, len(args)):
            rez += args[i]
    return rez


try:
    print("Сумма равна", sum())
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum(1, 2, 3))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum("ab", "cd"))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum((1, 2), (3, 4)))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print(1, 2, "cd")
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum( (1, 2), 3, 4))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum((1, 2), {3, 4}))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum((1, 2), [3, 4]))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum((1, 2), "cd"))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum( {1, 2}, 3, 4))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum({1, 2}, [3, 4]))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum({1, 2}, "cd"))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum( [1, 2], 3, 4))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")

try:
    print("Сумма равна", sum([1, 2], "cd"))
except TypeError:
    print("Операция применена к объекту несоответствующего типа")
