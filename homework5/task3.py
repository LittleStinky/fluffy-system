def f(n):
    if n == 1 or n == 2:
        return 1;
    if n <= 0:
        return f(n+2) - f(n+1)
    return f(n-1) + f(n-2)
    

try:
    print(f(int(input("Введите номер числа Фибоначчи:"))))
except ValueError:
    print("Необходимо ввести целое число")
