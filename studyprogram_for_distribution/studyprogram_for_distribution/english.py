import command
import sys
import random

if __name__ == '__main__':
    print('Please launch main.py')
    sys.exit()
command.englishisrun = True

q = ['go','have','start','visit']
a1 = ['went','haved','started','visitd']
a2 = ['god','had','startd','visited']
a = ['1','2','1','2']

def question():
    nam = random.randint(0,len(q)-1)
    print(q[nam] + 'の過去形は?')
    print('1.' + a1[nam])
    print('2.' + a2[nam])
    answer = input('>')
    if answer == a[nam]:
        print('正解!')
    else:
        print('不正解!')

    import main

isrun = True
question()
