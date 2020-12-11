# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(*user_input):
    try:
        user_inp_a = int(input('Введите делимое: '))
        user_inp_b = int(input('Введите делитель: '))
        result = user_inp_a / user_inp_b

    except ZeroDivisionError:
        return 'Делить на 0 нельзя!'
    except ValueError:
        return 'Вы ввели недопустимые символы'

    return result


print(f'Результат: {division()}')