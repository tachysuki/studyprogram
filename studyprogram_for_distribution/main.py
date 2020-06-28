#This program is test edition for distribution 20/6/14
#import sys
from command import *
import command


global runcom
global isstart
isstart = None
#print(__name__)


def start():
    inputcommand = input('>')
    splitcom(inputcommand)

def splitcom(inputcommand):
    #print('splitcom')
    if inputcommand in ' ':
        inputcommand = com
        comsp = com.split()
        inputcommand = comsp[0]
        inputoption = comsp[1]
        #print(inputcommand)
        #print(inputoption)
        checkcom(inputcommand)
    else:
        checkcom(inputcommand)

def checkcom(inputcommand):
    #print('checkcom')
    i = 0
    for i in range(0,len(comlist)):
        i + 1
        #print(i)
        if inputcommand == comlist[i]:
            #print('a')
            runcom = comlist[i]
            #print(runcom)
            #import command
            comprocessing(runcom)
            #print('finishcheckcom')
            start()
    else:
        print(inputcommand + ': Command not found')
        helpok = input('Do you want help? Y/n')
        if helpok == '' or helpok == 'Y':
            runcom = 'help'
            comprocessing(runcom)
        else:
            start()

if __name__ != '__main__':
    print('finish command.py')

if __name__ == '__main__' or isstart == False:
    print('Started main.py....')
    print('StudyProgram Ver.1.0β')
    print('Copyright ©︎2020 Hirotoshi Yoshida. All Rights Reserved.')
    ismathrun = False
    isstart = True

start()
