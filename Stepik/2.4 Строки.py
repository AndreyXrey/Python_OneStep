# genome = input() + ' '
# s = 0
# n = genome[0]
# for i in genome:
#     if n != i:
#         print(n + str(s), end='')
#         s = 0
#         n = i
#     s += 1
# решение выше ШИКАРНО
a = input()
len = len(a)
a = ' '
n = int(0)
k = int(1)
result = ''
while n < len:
    result = a[n]
    if n == -1:
        break
    while a[n] == a[n + 1]:
        k += 1
        n += 1
    print(str(result) + str(k), end='')
    k = 1
    n += 1

