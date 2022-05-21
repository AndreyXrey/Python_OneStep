with open('out.txt', 'a+') as ouf:
    ouf.write('Какой-то текст\n') # or \r
    ouf.write(str(25))
    ouf.write('\n')
import os
# os.remove('out.txt')

