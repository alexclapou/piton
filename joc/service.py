from domain import Board
class Service(object):
    def __init__(self, board):
        self.board = board

    def minimax(self, depth, max_player):
        score = self.table_value()
        if score != 0:
            return score
        if depth == 2:
            return 0
        if max_player == True:
            best = -10
            j = 0
            while j < 7:
                i = 5
                breaK = False
                while self.board[i, j] != " ":
                    i = i - 1
                    if i < 0:
                        breaK = True
                        break
                if breaK == True:
                    j = j + 1
                    continue
                self.board[i, j] = "O"
                score = self.minimax(depth + 1, False)
                self.board[i, j] = " "
                best = max(score, best)
                j = j + 1
            return best
        else:
            best = 10
            j = 0
            while j < 7:
                i = 5
                breaK = False
                while self.board[i, j] != " ":
                    i = i - 1
                    if i < 0:
                        breaK = True
                        break
                if breaK == True:
                    j = j + 1
                    continue
                self.board[i, j] = "X"
                score = self.minimax(depth + 1, True)
                self.board[i, j] = " "
                best = min(score, best)
                j = j + 1
            return best

    def best_move(self):
        j = 0
        best_score = -1
        move = [0, 0]
        while j < 7:
            i = 5
            breaK = False
            while self.board[i, j] != " ":
                i = i - 1
                if i < 0:
                    breaK = True
                    break
            if breaK == True:
                j = j + 1
                continue
            self.board[i, j] = "X"
            score = self.minimax(0, False)
            self.board[i, j] = " "
            if score > best_score:
                best_score = score
                move = [i, j]
            j = j + 1
        return move

    def valid_move(self, line):
        ind = 0
        count = 0
        found = 0
        while ind < 6:
            count = count + 1
            if self.board[ind, line] == " ":
                found = ind
                ind = ind + 1
            else:
                break
        if count != 1:
            return [True, ind - 1] 
        return [False, None]

    def make_user_move(self, column, line):
        self.board[line, column] = "X"

    def make_computer_move(self, column, line):
        self.board[line, column] = "O"

    def table_value(self):
        linx, lino= ([0] * 6 for i in range(2))
        j = 0
        while j < 7:
            i = 5
            who = ""
            count_col = 0
            empty = False
            while i >= 0 and empty == False:
                if self.board[i, j] == " ":
                    empty = True
                    Y = i
                    while Y >= 0:
                        linx[Y] = 0
                        lino[Y] = 0
                        Y = Y - 1
                elif self.board[i, j] == "X":
                    if who == "X":
                        count_col = count_col + 1
                    else:
                        who = "X"
                        count_col = 1
                    lino[i] = 0
                    linx[i] = linx[i] + 1
                elif self.board[i, j] == "O":
                    if who == "O":
                        count_col = count_col + 1
                    else:
                        who = "O"
                        count_col = 1
                    linx[i] = 0
                    lino[i] = lino[i] + 1
                if count_col == 4:
                    if who == "X":
                        return 1
                    else:

                        return -1
                if linx[i] == 4:
                    return 1
                if lino[i] == 4:
                    return -1
                i = i - 1
            j = j + 1
        for i in range(3):
            I = i
            Jp = 6
            for j in range(4):
                J = j
                if self.board[I, J] == self.board[I + 1, J + 1] == self.board[I + 2, J + 2] == self.board[I + 3, J + 3] == "X":
                    return 1
                elif self.board[I, J] == self.board[I + 1, J + 1] == self.board[I + 2, J + 2] == self.board[I + 3, J + 3] == "O":
                    return -1
                elif self.board[I, Jp] == self.board[I + 1, Jp - 1] == self.board[I + 2, Jp - 2] == self.board[I + 3, Jp - 3] == "X":
                    return 1
                elif self.board[I, Jp] == self.board[I + 1, Jp - 1] == self.board[I + 2, Jp - 2] == self.board[I + 3, Jp - 3] == "O":
                    return -1
                Jp = Jp - 1
        return 0
