def is_password(password):
    """
    Функция принимает в качестве аргумента строку-пароль.
    Функция проверяет, подходит ли пароль под условия.
    Функция возвращает True - если подходит, False не подходит
    """
    if len(password) < 6:
        print("Пароль должен быть не менее 6 символов")
        return False
    if password.isdigit():
        print("Пароль не должен состоять только из цифр")
        return False
    if password.lower().find("password") != -1:
        print("Пароль не должен содержать слово 'password' в любом регистре")
        return False
    for i in range(len(password)):
        if password[i].isdigit():
            return True
    print("Пароль должен содержать хотя бы одну цифру")
    return False

if is_password(input("Введите пароль:")):
    print("Пароль принят")
else:
    print("Пароль не принят")
