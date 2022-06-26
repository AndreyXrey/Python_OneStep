number = 23
guess=int(input('введите число:'))

if guess==number:
    print('Поздравляю! Угадал!')
    print('(хотя и не получишь приза)')
elif guess<number:
    print('Гадай ещё, число больше')
else:
    print('Гадай меньшее')

print("Завершено")