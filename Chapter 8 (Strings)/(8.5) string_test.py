# Эта программа демонстрирует несколько строковых методов проверки.


def main():

    # Получить от пользователя строковое значение.
    user_string = input('Введите строковое значение: ')

    print('Boт, что обнаружено в отношении введенного значения:')
    # Проанализировать строковое значение.
    if user_string.isalnum():
        print('Эта строка содержит буквы или цифры.')
    if user_string.isdigit():
        print('Эта строка содержит только цифры.')
    if user_string.isalpha():
        print('Эта строка содержит только буквы алфавита.')
    if user_string.isspace():
        print('Эта строка содержит только пробельные символы.')
    if user_string.islower():
        print('Bce буквы в строке находятся в нижнем регистре.')
    if user_string.isupper():
        print('Bce буквы в строке находятся в верхнем регистре.')


# Вызвать главную функцию.
main()
