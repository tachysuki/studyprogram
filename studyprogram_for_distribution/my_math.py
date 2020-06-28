import command

command.mathisrun = True
#print('This is my_math.py')
def question():
    print('3x=3')
    print('x=?')
    print('1:x=1')
    print('2:x=2')
    answer = input('>')
    if answer == '1':
        print('正解!')
    else:
        print('不正解!')

    import main
isstart = True
divergence = False
question()
if __name__ == '__main__':
    print('Please launch main.py')
