x = 50
def func():
    global x
    # x меняется во всей системе
    print('x equal', x)
    x=2
    print('Change global meaning x to',x)

func()
print('x meaning',x)