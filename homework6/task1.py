def list_encode(list_str):
    list_byte = []
    for i in range(len(list_str)):
        list_byte.append(list_str[i].encode())
    return list_byte

def list_decode(list_byte):
    list_str = []
    for i in range(len(list_byte)):
        list_str.append(list_byte[i].decode())
    return list_str

print("Преобразование списка строк в список байт-кодов:", list_encode(list_str = list(input("\nВведите список строк, разделенных запятыми:").split(','))), '\n')

new_list_str = (input("Введите список байт кодов, разделенных запятыми:").split(','))
list_byte = []
for i in range(len(new_list_str)):
    list_byte.append(bytearray(new_list_str[i], encoding='utf-8'))
print("Преобразование списка байт-кодов в список строк", list_decode(list_byte), '\n')

print("Проверка применения обратных функций друг к другу:", list_decode(list_encode(list_str = list(input("Введите список строк, разделенных запятыми:").split(',')))))
