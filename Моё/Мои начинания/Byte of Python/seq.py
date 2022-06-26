shopList = ['Яблоки', "Mango", "Carrot", 'Bananas']
name = 'swaroop'

# Операция индексирования
print('Элемен 0 -', shopList[0])
print('Элемен 1 -', shopList[1])
print('Элемен 2 -', shopList[2])
print('Элемен 3 -', shopList[3])
print('Элемен -1 -', shopList[-1])
print('Элемен -2 -', shopList[-2])
print('Символ 0 -', name[0])

print('\n')
# Вырезка из списка
print('Элемен c 1 по 3:', shopList[1:3])
print('Элемен с 2ого до конца', shopList[2:])
print('Элемен с 1 по -1', shopList[1:-1])
print('Элемен от начала до конца', shopList[:])

print('\n')
# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца :', name[:])

print('\n')
# print(shopList[-5]) это не работает
print(shopList[::2])
print(shopList[::3])
print(shopList[::-1])
print(shopList[::-2])