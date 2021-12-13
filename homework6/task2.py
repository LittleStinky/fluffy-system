try:
    with open('Input.txt', 'r') as input:
        try:
            c = int(input.readline())
            h = int(input.readline())
            o = int(input.readline())
            if c <= 0 or h <= 0 or o <= 0:
                raise ValueError
        except ValueError:
            with open('Output.txt', 'w') as output:
                output.write('Входные данные должны быть натуральными числами')
except FileNotFoundError:
    print("Файл 'Input.txt' не найден")
    exit()

div_c = c // 2
div_h = h // 6
div_o = o

count_c2h5oh = min(div_c, div_h, div_o)

with open('Output.txt', 'w') as output:
    output.write('Максимально возможное число молекул спирта равно ')
    output.write(str(count_c2h5oh))
