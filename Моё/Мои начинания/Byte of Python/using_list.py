# Составляю список покупок
shopList = [' чай', ' кофе', ' сок', ' жопа проститутки', ' гандоны с ментолом']

print('Я должен сделать', len(shopList), 'покупки')

print('Покупки', end="")
for item in shopList:
    print(item, end="")

print("\nТакже нужно купить красный педжак.")
shopList.append("красный педжак")
print("Теперь мой список покупок таков:", shopList)

print("Отсортирую ка я список")
shopList.sort()
print("отсортированный список выглядит так:", shopList)

print("Первое, что мне нужно купить, это", shopList[0])
oldItem = shopList[0]
del shopList[0]
print("Я купил", oldItem)
print("Теперь мой список покупок:", shopList)

# print("\n")
# print(shopList.contains)
