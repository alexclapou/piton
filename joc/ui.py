from service import Service
from domain import Board
from random import randint

class UI(object):
    def __init__(self, service):
        self.service = service

    def display_board(self):
        print(self.service.board)
        print('\n')

    def computer_move(self):
        line, move = self.service.best_move()
        self.service.make_computer_move(move, line)
        print("computer move:\n" + "column: " + str(move) + " line: " + str(line))
        return 1

    def check_for_winner(self, winner):
        end = self.service.table_value()
        if end == 1:
            print("X won")
            return 1
        elif end == -1:
            print("O won")
            return 1
        return 0

    def user_move(self):
        c = int(input("column: "))
        if c > 7 or c < 0:
            return 0
        move_info = self.service.valid_move(c)
        valid_move, line = move_info 
        if valid_move == True:
            self.service.make_user_move(c, line)
            return 1
        return 0
    
    def start(self):
        inp = 0
        moves = 0
        winner_found = False
        #if inp % 2 == 0 user have to add a new value, if inp % 2 != 0 the computer will play
        while winner_found == False and moves != 42:
            try:
                self.display_board()
                if inp % 2 == 0:
                    q = self.user_move()
                    while q == 0:
                        q = self.user_move()
                    moves = moves + 1
                else:
                    q = self.computer_move()
                    while q == 0:
                        q = self.computer_move()
                    moves = moves + 1
                if self.check_for_winner(winner_found) == 1:
                    print(self.service.table_value())
                    return
            except IndexError as m:
                print(m)
            except ValueError as m:
                print(m)
            inp = inp + 1
b = Board()
s = Service(b)
u = UI(s)
u.start()
