s = input("Введите коэффициенты квадратного уравнения через пробел: ").split(" ")
num_coeff = list(float(i) for i in s)
a = num_coeff[0]
b = num_coeff[1]
c = num_coeff[2]
d = b**2 - 4*a*c
if a == 0:
    print("Это не является квадратным уравнением")
elif d > 0:
    x = [(- b + d**(0.5)) / (2*a), (- b - d**(0.5)) / (2*a)]
    print(f"Корни квадратного уравнения {x[0]}, {x[1]}")
elif d == 0:
    x = - b / (2*a)
    print(f"Корень квадратного уравнения {x}")
elif d < 0:
    print("Корней нет")
