"""
Бесконечный скрипт для движения персонажа влево, вправо,
вверх и вниз по координатам x и y.
Остановка программы - слово "стоп".
"""
x = y = 0
while 1:
    direction = input("Введите направление: ")
    if direction.lower() == "влево":
        x -= int(input("Введите число шагов: "))
    elif direction.lower() == "вправо":
        x += int(input("Введите число шагов: "))
    elif direction.lower() == "вверх":
        y += int(input("Введите число шагов: "))
    elif direction.lower() == "вниз":
        y -= int(input("Введите число шагов: "))
    elif direction.lower() == "стоп":
        break;
    print(f"({x}, {y})")
