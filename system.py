class System:
    def __ismatch(self, ar):
        if ar[0] == ar[1] and ar[1] == ar[2]:
            return True
        else:
            return False

    def sys_gameOver(self, pos):
        if pos[0] == '-' and pos[4] == '-' and pos[8] == '-':
            return False

        elif pos[2] == '-' and pos[4] == '-' and pos[6] == '-':
            return False

        elif self.__ismatch([pos[0], pos[1], pos[2]]) and pos[0] != '-':
            return True

        elif self.__ismatch([pos[3], pos[4], pos[5]]) and pos[3] != '-':
            return True

        elif self.__ismatch([pos[6], pos[7], pos[8]]) and pos[6] != '-':
            return True

        elif self.__ismatch([pos[0], pos[3], pos[6]]) and pos[0] != '-':
            return True

        elif self.__ismatch([pos[1], pos[4], pos[7]]) and pos[1] != '-':
            return True

        elif self.__ismatch([pos[2], pos[5], pos[8]]) and pos[2] != '-':
            return True

        elif self.__ismatch([pos[0], pos[4], pos[8]]) and pos[0] != '-':
            return True

        elif self.__ismatch([pos[2], pos[4], pos[6]]) and pos[2] != '-':
            return True

        else:
            return False