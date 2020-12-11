# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(number_1, number_2, number_3):
    numbers = []
    numbers.append(number_1)
    numbers.append(number_2)
    numbers.append(number_3)


    numbers.sort()
    print(numbers)
    res = numbers[1] + numbers[2]
    return res


print(my_func(2, 8, 1))
