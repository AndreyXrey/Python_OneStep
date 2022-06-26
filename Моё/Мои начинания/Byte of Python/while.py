number = 15
run = True
while run:
    guess = int(input('Число:'))
    if guess == number:
        print('Угадаааал!')
        run = False
    elif guess < number:
        print('Ищи большее')
    else:
        print('Ищи меньшее')
else:
    print("Цикл while закончен")
print('Завершение')
