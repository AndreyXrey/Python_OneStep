'''
b = int(input())
rez = []



a = [.]*n
pole = [[0 for i in range(n)] for j in range(m)]
for x in range(m):
    for y in range(n):
        cell = pole[x][y]
        while True:
            if y <= n-k and x == k:
                print('*', end=' ')

print()


строки:                  столбцы:

1) [0] -> [n]            2) [0+1] -> [n]

3) [n-1] -> [0]          4) [n-1] -> [0+1]

5) и т.д                 6) и т.д

Моя подсказка алгоритма данной задачи, не пертендующая на оригинальность, но решаемая знаниями, полученными только по итогу данного шага курса.

Попробуйте нарисовать марицу, допустим, 5х5 на бумаге и прям с точки 0,0 по шагам проследовать как должна заполняться матрица. Для удобства я для себя сделал две таблички: для строк и для столбцов. И в этих табличках построчно написал последовательность того, как идет спираль:

строки:                  столбцы:

1) [0] -> [n]             2) [0+1] -> [n]

3) [n-1] -> [0]          4) [n-1] -> [0+1]

5) и т.д                   6) и т.д

Если продолжить заполнение, то можно отчетливо увидеть общее правило и то, что задачу заполнения можно выполнить в эти первые 4 шага. Итого будет 2 части в каждой по два цикла (по циклу на шаг):
1-я  часть  - заполняем в направлении N (с лева на право и сверху в низ, шаги 1 и 2 )
2-я  часть  - заполняем от N (а тут кругом минусы (с права на лево, с низу в верх), шаги 3 и 4 )
Повторяем, если это нужно (не забываем проверять, а не пора ли остановиться).
Код получается в строк 30.
5:
0 0    5х5
0 1
0 2
0 3
0 4 поворот
1 4
2 4
3 4
4 4 поворот
4 3
4 2
4 1
4 0 поворот - 4х4
3 0
2 0
1 0 поворот
1 1
1 2
1 3 поворот - 3х3
2 3
3 3 поворот
3 2
3 1 поворот - 2х2
2 1 поворот
2 2 СЕРЕДИНА - выход













'''

A = input()
a = int(A)
b = [i for i in range(1, a**2+1)]
lenb = len(b)
c = [[int(0) for j in range(a)] for i in range(a)]
k = 1
print(a, b, lenb)

 # 5 4 4 3 3 2 2 1 1
 # НЕ РЕШИЛ, НУЖНО РАЗОБРАТЬ В РЕШЕНИЯХ НА СТЕПИКЕ
for i in range(a):
    for j in range(a):
        while True:
            if i == k and j == a - k:
                c[i][j] = b[i]
                print(c[i][j])
                k += 1
            if k == 7:
                break



a = [i for i in range(1, int(input())+1)]
print(a)