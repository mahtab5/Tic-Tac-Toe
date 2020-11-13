from random import randint
from system import System

x = System()
# 0,1,2
# 3,4,5
# 6,7,8

corners = [0, 2, 6, 8]
middle = 4
rest = [1, 3, 5, 7]
line1 = [0,3,6]
line2 = [1,4,7]
line3 = [2,5,8]
line4 = [0,1,2]
line5 = [3,4,5]
line6 = [6,7,8]
line7 = [0,4,8]
line8 = [2,4,6]

class Bot:
    def isEmpty(self, pos):
        for i in pos:
            if i != '-':
                return False
        return True

    def __empty(self, pos:list):
        keeper = []
        for i in range(len(pos)):
            if pos[i] == '-':
                keeper.append(i)

        return keeper

    def __match_move(self, pos, n):
        keeper = []
        append = True
        if n in line1:
            for i in line1:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        append = True

        if n in line2:
            for i in line2:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        append = True

        if n in line3:
            for i in line3:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        append = True

        if n in line4:
            for i in line4:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        append = True

        if n in line5:
            for i in line5:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        append = True

        if n in line6:
            for i in line6:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        append = True

        if n in line7:
            for i in line7:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        append = True

        if n in line8:
            for i in line8:
                if pos[i] == n:
                    continue
                elif pos[i] != '-':
                    append = False
                else:
                    if append:
                        keeper.append(i)
        return keeper

    def willWin(self, pos: list, n):
        for i in range(len(pos)):
            if pos[i] == '-':
                pos[i] = 'X' if n == 'O' else 'O'
                if x.sys_gameOver(pos):
                    pos[i] = '-'
                    return i
                else:
                    pos[i] = '-'

        return False

    def __wilbotwin(self,pos, n):
        if n == 'O':
            return self.willWin(pos, 'X')
        else:
            return self.willWin(pos, 'O')

    def bot_move(self, pos, n, mode):
        if self.isEmpty(pos):
            pos[corners[randint(0,3)]] = n
            return pos

        elif self.__wilbotwin(pos, n):
            c = self.__wilbotwin(pos, n)
            pos[c] = n
            return pos

        elif self.willWin(pos, n):
            c = self.willWin(pos, n)
            pos[c] = n
            return pos

        elif pos[middle] == '-' and mode != 'Normal':
            pos[middle] = n
            return pos

        elif self.__match_move(pos, n) and mode != 'Normal':
            c = self.__match_move(pos, n)
            pos[c[randint(0, len(c)-1)]] = n
            return pos

        else:
            c = self.__empty(pos)
            pos[self.__empty(pos)[randint(0,len(c)-1)]] = n
            return pos