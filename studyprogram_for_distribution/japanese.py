import command
command.japaneseisrun = True
def question():
    print('Q:明日はアメだ')
    print('正しい方を入力しなさい')
    print('1:飴')
    print('2:雨')
    answer = input('>')
    if answer == '2':
        print('正解!')
    else:
        print('不正解!')

    import main
isrun = True
question()
if __name__ == '__main__':
    print('Please launch main.py')
