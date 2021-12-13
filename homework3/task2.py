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
