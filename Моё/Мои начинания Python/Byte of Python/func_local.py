# Мой вариант
x=50
def func(x):
   print('x равен', x, 'хотите изменить локальный х?')
   l=input()
   if l=='да':
       print('впишите его далее:')
       x=input()
       print('Замена локального х на', x)
   elif l=='нет':
       print('х по прежнему',x)
   else:
       print('Некорректный ответ')
func(x)
# -------------------------------------------------------
# Вариант из книжки
print('---------------------------------------------------------')

x = 50
def func(x):
    print('x равен', x)
    # х меняется в подсистеме
    x = 2
    print('Замена локального x на', x)
func(x)
print('x по прежнему', x)

