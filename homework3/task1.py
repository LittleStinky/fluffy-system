    direction = input("Введите направление: ")
    if (direction.lower() == "влево"):
        print("(" -int(input("Введите число шагов: ")), ", 0 )")
    elif (direction.lower() == "вправо"):
        print("(", int(input("Введите число шагов: ")), ", 0 )")
    elif (direction.lower() == "вверх"):
        print("( 0 , ", int(input("Введите число шагов: ")), ")")    
    elif (direction.lower() == "вниз"):
        print("( 0 , ", -int(input("Введите число шагов: ")), ")") 
