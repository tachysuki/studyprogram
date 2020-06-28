#from main import runcoman
import sys
#import main
#from main import *

comlist = ['help','exit','Japanese','Math','Science','SocialStudies']
#print('started command.py')
#import main
#runcom = main.runcom
japaneseisrun = False
mathisrun = False
scienceisrun = False
socialstuisrun = False

#print('command.py')
def help():
    print('Help text')

def exit():
    sys.exit()

def start():
    main.start()

def comprocessing(runcom):
    #print('comprocessing')
    #print(runcom)
    #from main import *
    #import main
    #print('finish import')
    if runcom == 'exit':
        print('Finished StudyProgram')
        exit()
    elif runcom == 'help':
        print(comlist)
        i = 0
        print('--------------')
        for i in range(0,len(comlist)):
            print(comlist[i])
        print('--------------')
        isstart = True
        import main
    elif runcom == 'Japanese':
        print('mode: Japanese')
        if japaneseisrun == True:
            print('japaneseisrun == True')
            import japanese
            japanese.question()
        import japanese

    elif runcom == 'Math':
        print('mode: Math')
        if mathisrun == True:
            print('mathisrun == True')
            import my_math
            my_math.question()
        import my_math

    elif runcom == 'Science':
        print('mode: Science')
        if scienceisrun == True:
            print('scienceisrun == True')
            import science
            science.question()
        import science

    elif runcom == 'SocialStudies':
        print('mode: SocialStudies')
        if socialstuisrun == True:
            print('socialstuisrun == True')
            import socialstu
            socialstu.question()
        import socialstu
    #elif runcom = 'etc'

if __name__ == '__main__':
    print('Please launch main.py')
