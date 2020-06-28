import command

command.scienceisrun = True
#print('This is science.py')
def question():
    print('100gにかかる力は何Nか?')
    print('1:100N')
    print('2:10N')
    print('3:1N')
    answer = input('>')
    if answer == '3':
        print('正解!')
    else:
        print('不正解!')

    import main

question()
if __name__ == '__main__':
    print('Please launch main.py')
