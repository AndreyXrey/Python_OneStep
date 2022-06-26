print('-----------------------------------------------')

print('nonlocal в подфункции:')
x = 3
def func_outer():
    x = 2
    print('x equal', x)

    def func_inner():
        nonlocal x
        # global x
        x = 5
        print(x)

    func_inner()
    print('Local x changed to', x)

func_outer()
print(x)

print('-----------------------------------------------')

print('global в подфункции:')
x = 3
def func_outer():
    x = 2
    print('x equal', x)

    def func_inner():
        # nonlocal x
        global x
        x = 5
        print(x)

    func_inner()
    print('Local x changed to', x)

func_outer()
print(x)

print('-----------------------------------------------')
