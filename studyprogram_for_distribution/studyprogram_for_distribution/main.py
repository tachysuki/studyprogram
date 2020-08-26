#This program is finished edition 20/8/26
from command import *
import command

global runcom
global isstart
isstart = None

def start():#コマンド入力関数
    inputcommand = input('>')
    checkcom(inputcommand)

def checkcom(inputcommand):#入力されたコマンドが不正なものじゃないか否かの処理
    i = 0
    for i in range(0,len(comlist)):
        i + 1
        if inputcommand == comlist[i]:
            runcom = comlist[i]
            comprocessing(runcom)
            start()
    else:
        print(inputcommand + ': Command not found')
        helpok = input('Do you want help? Y/n')
        if helpok == '' or helpok == 'Y':
            runcom = 'help'
            comprocessing(runcom)
        else:
            start()

if __name__ == '__main__' or isstart == False:#実行が初回か否かの処理
    print('Started main.py....')
    print('StudyProgram Ver.1.5')
    print('Copyright ©︎2020 Hirotoshi Yoshida. All Rights Reserved.')
    ismathrun = False
    isstart = True

start()
