import sys

comlist = ['help','exit','Japanese','Math','Science','SocialStudies','English','etc']
japaneseisrun = False #各教科のプログラムを実行したかどうか
mathisrun = False
scienceisrun = False
socialstuisrun = False
englishisrun = False


def help():
    print('Help text')

def exit():
    sys.exit()

def start():
    main.start()

def comprocessing(runcom):#コマンド実行の関数
    if runcom == 'exit':
        print('Finished StudyProgram')
        exit()
    elif runcom == 'help':
        i = 0
        print('--------------')
        for i in range(0,len(comlist)):
            print(comlist[i])
        print('--------------')
        isstart = True
        import main
        main.start()
    elif runcom == 'Japanese':
        print('mode: Japanese')
        if japaneseisrun == True:
            import japanese
            japanese.question()
        import japanese

    elif runcom == 'Math':
        print('mode: Math')
        if mathisrun == True:
            import my_math
            my_math.question()
        import my_math

    elif runcom == 'Science':
        print('mode: Science')
        if scienceisrun == True:
            import science
            science.question()
        import science

    elif runcom == 'SocialStudies':
        print('mode: SocialStudies')
        if socialstuisrun == True:
            import socialstu
            socialstu.question()
        import socialstu

    elif runcom == 'English':
        print('mode: English')
        if englishisrun == True:
            import english
            english.question()
        import english
    elif runcom == 'etc':
        print('Sorry, we are preparing...')

if __name__ == '__main__':
    print('Please launch main.py')
