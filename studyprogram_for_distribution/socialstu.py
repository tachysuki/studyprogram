import command

#print('This is socialstu.py')
command.socialstuisrun = True
def question():
    print('イギリスが午前0時の時、日本は何時か?')
    print('1:午前9時')
    print('2:午後3時')
    answer = input('>')
    if answer == '1':
        print('正解!')
    else:
        print('不正解!')

    import main
question()

if __name__ == '__main__':
    print('Please launch main.py')
