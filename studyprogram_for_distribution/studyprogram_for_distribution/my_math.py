import command
import sys
import random

command.mathisrun = True
if __name__ == '__main__':
    print('Please launch main.py')
    sys.exit()

q = ['x+3=5','x+4=-8','y-6=9','y-2=-7']
q1 = ['x=2','x=-4','y=15','y=-9']
q2 = ['x=8','x=-12','y=3','y=-5']
a = ['1','2','1','2']


def question():
    nam = random.randint(0,len(q)-1)
    print(q[nam])
    if q[nam] in 'x':
        print('x=?')
    else:
        print('y=?')
    print('1:'+ q1[nam])
    print('2:'+ q2[nam])
    answer = input('>')
    if answer == a[nam]:
        print('正解!')
    else:
        print('不正解!')

    import main
isstart = True
divergence = False
question()
