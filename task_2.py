# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию:')
year = input('Введите Ваш возраст:')
city = input('Город в котором вы проживате? ')
email = input('Введите ваш емейл: ')
telephone = input('Введите свой номер телефона: ')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name=name, surname=surname, year=year, city=city, email=email, telephone=telephone))