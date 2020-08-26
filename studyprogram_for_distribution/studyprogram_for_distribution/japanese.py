#Update at 8/2

import command
import sys
import random
command.japaneseisrun = True
if __name__ == '__main__':
    print('Please launch main.py')
    sys.exit()

q = ['明日はアメだ','物語はイガイな結末をむかえた','会議で人の意見にイギを唱えた','最後まで自分のイシを貫いた','イッパツの銃声が鳴り響いた','ゲルマン民族の大イドウ','河川の堤防をカイシュウする','聴衆の質問にカイトウする','校庭を一般にカイホウする','キセイ事実として認める','住民のヒナンをあびる']
q1 = ['飴','意外','意義','意志','一発','移動','回収','回答','解放','既成','避難']
q2 = ['雨','以外','異議','意思','一髪','異動','改修','解答','開放','規制','非難']
a = ['2','1','2','1','1','1','2','1','2','1','2']


def question():
    nam = random.randint(0,len(q)-1)
    n_question = q[nam]
    n_q1 = q1[nam]
    n_q2 = q2[nam]
    n_a = a[nam]
    print('Q:'+ n_question)
    print('正しい方を半角数字で入力しなさい')
    print('1:'+ n_q1)
    print('2:'+ n_q2)
    answer = input('>')
    if answer == n_a:
        print('正解!')
    else:
        print('不正解!')



    import main
isrun = True
question()
