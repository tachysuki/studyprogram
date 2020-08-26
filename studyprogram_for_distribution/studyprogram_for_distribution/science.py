import command
import sys
import random

if __name__ == '__main__':
    print('Please launch main.py')
    sys.exit()
command.scienceisrun = True
q = ['動物と植物の細胞のどちらにも見られる、染色液によく染まる丸い球','動物と植物の細胞のどちらにも見られる、細胞質を包む膜','１つの細胞だけでできている生物']
a1 = ['核','細胞壁','単細胞生物']
a2 = ['核細胞','細胞膜','一細胞生物']
a = ['1','2','1']

def question():
    nam = random.randint(0,len(q)-1)
    print('名称を答えよ')
    print('Q:' + q[nam])
    print('1.' + a1[nam])
    print('2.' + a2[nam])
    answer = input('>')
    if answer == a[nam]:
        print('正解!')
    else:
        print('不正解!')

    import main

question()
