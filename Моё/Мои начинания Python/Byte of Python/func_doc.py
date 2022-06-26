def printMax(x, y):
    """ Выводит максимальое из двух чисел.

        Оба значения должны быть целыми"""
    x = int(x)  # конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


printMax(3.6, 5)
print(printMax.__doc__)
help(printMax)

