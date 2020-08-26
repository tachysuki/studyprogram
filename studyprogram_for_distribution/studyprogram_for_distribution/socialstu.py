import command
import sys
import random

if __name__ == '__main__':
    print('Please launch main.py')
    sys.exit()

command.socialstuisrun = True
q = ['645','794','1192','1575','1582']
a1 = ['大化の改新','平城京への遷都','鎌倉幕府成立','桶狭間の戦い','本能寺の変']
a2 = ['十七条の憲法の制定','平安京への遷都','平治の乱','長篠の戦い','安土城築城']
a = ['1','2','1','2','1']
def question():
    nam = random.randint(0,len(q)-1)
    print('Q:'+ q[nam] +'年に起きたことは?')
    print('1:'+ a1[nam])
    print('2:'+ a2[nam])
    answer = input('>')
    if answer == a[nam]:
        print('正解!')
    else:
        print('不正解!')

    import main
question()
