print('Простое присваивание')
shopList = ['Яблоки', "Mango", "Carrot", 'Bananas']
myList = shopList # myList это ещё одно имя указывающее на объект

del shopList[0] #Первая покупка сделана

print('shopList:', shopList)
print('myList', myList)
# оба принта указывают на одно и то же

print("Копирование при помощи полной вырезки")
myList= shopList[:] # Создаётся копия путём полной вырезки
del myList[0]

print('shopList:', shopList)
print('myList', myList)