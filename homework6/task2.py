try:
    with open('Input.txt', 'r') as input:
        try:
            C = int(input.readline())
            H = int(input.readline())
            O = int(input.readline())
            if C <= 0 or H <= 0 or O <= 0:
                raise ValueError
        except ValueError:
            with open('Output.txt', 'w') as output:
                output.write('Входные данные должны быть натуральными числами')
except FileNotFoundError:
    print("Файл 'Input.txt' не найден")
    exit()

div_C = C // 2
div_H = H // 6
div_O = O

count_C2H5OH = min(div_C, div_H, div_O)

with open('Output.txt', 'w') as output:
    output.write('Максимально возможное число молекул спирта равно ')
    output.write(str(count_C2H5OH))
