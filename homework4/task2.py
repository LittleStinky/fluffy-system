colors = dict( red = (255, 0, 0), green = (0, 255, 0), blue = (0, 0, 255), yellow = (255, 255, 0))
print(colors)
command = input("Выберите, что хотите сделать со словарем (add, delete, print all, nothing): ")
while command != "nothing" :
    if command == "add":
        color_name = input("Введите название цвета: ")
        if colors.get(color_name) != None and input("Этот цвет найден в словаре, заменить код его цвета на новый? (да/нет): ") == 'да' or colors.get(color_name) == None :
            color_rgb = tuple(input("Введите значения цвета в соответствии с моделью rgb через пробел: ").split(" "))
            if len(color_rgb) == 3 and int(color_rgb[0]) <= 255 and int(color_rgb[1]) <= 255 and int(color_rgb[2]) <= 255 and int(color_rgb[0]) >= 0 and int(color_rgb[1]) >= 0 and int(color_rgb[2]) >= 0:
                colors.update({color_name: color_rgb})
    elif command == "delete":
        color_name = input("Введите название цвета: ")
        if colors.get(color_name) != None :
            colors.pop(color_name, tuple(input("Введите значения цвета в соответствии с моделью rgb через пробел: ").split(" ")))
    elif command == "print all" :
        print(colors)
    else:
        print("Такой команды не существует")
    command = input("Выберите, что хотите сделать со словарем (add, delete, print all, nothing): ")
colors.clear()
