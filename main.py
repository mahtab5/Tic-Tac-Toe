from random import randint
from board import Board
from TicTac_bot import Bot

x = Board()
y = Bot()
computer_point = 0
user_point = 0
x_point = 0
o_point = 0
istarted = True
name = None
mode = None

# separte


def multiplayer():
    print('MultiPlayer Mode ')
    # play
    turn = 0
    while not x.isFinished() and not x.gameOver():
        if turn % 2 == 0:
            print()
            print(x)
            print()
            print("O's Turn...")
            user = 'a'
            while not x.isAvl(user):
                user = input('Enter Your Position From 1-9: ')
                if not x.isAvl(user):
                    print('Invalid Position!')
                    print()

            x.chnge(int(user), 'O')
            turn += 1
        else:
            print()
            print(x)
            print()
            print("X's Turn...")
            user = 'a'
            while not x.isAvl(user):
                user = input('Enter Your Position From 1-9: ')
                if not x.isAvl(user):
                    print('Invalid Position!')
                    print()

            x.chnge(int(user), 'X')
            turn += 1

    print()
    print(x)
    if not x.gameOver():
        print()
        print('Match Has Been Tied')
    elif turn % 2 == 0:
        print()
        print('X Has Won The Match')
        global x_point
        x_point = x_point+1
    else:
        print()
        print('O Has Won The Match')
        global o_point
        o_point = o_point + 1

    print()
    print(f'X : {x_point}      O : {o_point}')
    x.reset()
    l = input('Enter 1 If You Want To Start Again: ')
    print()


def computer():
    print('Computer Mode ')
    print()
    global istarted
    if istarted:
        global mode
        print('1)Normal\n2)Hard\n')
        mode = input('Enter The Mode: ')
        if mode == '2':
            mode = 'Hard'
        else:
            mode = 'Normal'
        global name
        name = input('Enter Your Name Here: ')
        if name.split() == '' or name == '\n' or not name:
            name = 'User'

    turn = randint(0, 1)
    counter = 0
    computer = True
    print(f'{mode} Mode: ', end='')
    while not x.gameOver() and not x.isFinished():
        if turn % 2 == 0:
            print()
            print(x)
            print()
            print(f"{name}'s Turn...")
            user = 'a'
            while not x.isAvl(user):
                user = input('Enter Your Position From 1-9: ')
                if not x.isAvl(user):
                    print('Invalid Position!')
                    print()

            if counter % 2 == 0:
                x.chnge(int(user), 'O')
                turn += 1
                counter += 1
                computer = False
            else:
                x.chnge(int(user), 'X')
                turn += 1
                counter += 1
                computer = False
        else:
            print()
            print(x)
            print()
            print("Computer's Turn...")

            if counter % 2 == 0:
                y.bot_move(x.pos, 'O',mode)
                turn += 1
                counter += 1
                computer = True
            else:
                y.bot_move(x.pos, 'X',mode)
                turn += 1
                counter += 1
                computer = True

    print()
    print(x)
    if not x.gameOver():
        print()
        print('Match Has Been Tied')
    elif computer:
        print()
        print('Computer Has Won')
        global computer_point
        computer_point = computer_point + 1
    else:
        print()
        print('You Have Won')
        global user_point
        user_point = user_point + 1

    istarted = False
    print(f"Your Point: {user_point}        Computer's Point: {computer_point}")



# sprte

print('Tic Tac Toe Game'+'              '+'Author: Mahtab')

start = '1'
opt = True
cmp = True


while start == '1':
    if opt:
        computer_point = 0
        user_point = 0
        x_point = 0
        o_point = 0
        istarted = True

        print('You Have 3 Options Available: \n1)Play With Computer\n2)Play Multiplayer\n3)See The Positions\n4)Exit\n')

        options = input('Enter Your Choice Here: ')

        if options == '2':
            cmp = False
            multiplayer()
            opt = False
        elif options == '3':
            x.showpos()
            print(x)
            x.reset()
            print()

        elif options == '4':
            break

        else:
            cmp = True
            computer()
            opt = False
    else:
        j = input('Press Enter To Play Again, 1 To See The Options :')

        if j == '1':
            x.reset()
            opt = True
            continue

        else:
            if cmp:
                x.reset()
                computer()
            else:
                x.reset()
                multiplayer()
