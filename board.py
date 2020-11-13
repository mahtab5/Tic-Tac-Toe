from system import System
z = System()

class Board:
    def __init__(self):
        self.pos = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.rest = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def chnge(self, n, x):
        self.pos[n-1]=x

    def reset(self):
        self.pos = self.rest.copy()

    def isFinished(self):
        for i in self.pos:
            if i == '-':
                return False
        return True

    def showpos(self):
        for i in range(9):
            self.pos[i] = i+1

    def isAvl(self, pos:str):
        if not pos.isdigit():
            return False
        if 1 <= int(pos) <= 9:
            if self.pos[int(pos)-1] != '-':
                return False
            else:
                return True
        else:
            return False

    def gameOver(self):
        return z.sys_gameOver(self.pos)

    def __str__(self):
        return  f' {self.pos[0]} | {self.pos[1]} | {self.pos[2]} \n' \
                f' {self.pos[3]} | {self.pos[4]} | {self.pos[5]} \n' \
                f' {self.pos[6]} | {self.pos[7]} | {self.pos[8]} '