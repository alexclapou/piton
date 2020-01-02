class Board(object):
    def __init__(self):
        self._b = [[]]
        self.initialize_board(self._b)

    def initialize_board(self, board):
        self._b = [[" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "]]
 
    def display(self):
        print(" -----------------------------")
        print(" | " + str(self._b[0][0]) + " | " + str(self._b[0][1]) + " | " + str(self._b[0][2]) + " | " + str(self._b[0][3]) + " | " + str(self._b[0][4]) + " | " + str(self._b[0][5]) + " | " + str(self._b[0][6]) + " |")
        print(" -----------------------------")
        print(" | " + str(self._b[1][0]) + " | " + str(self._b[1][1]) + " | " + str(self._b[1][2]) + " | " + str(self._b[1][3]) + " | " + str(self._b[1][4]) + " | " + str(self._b[1][5]) + " | " + str(self._b[1][6]) + " |")
        print(" -----------------------------")
        print(" | " + str(self._b[2][0]) + " | " + str(self._b[2][1]) + " | " + str(self._b[2][2]) + " | " + str(self._b[2][3]) + " | " + str(self._b[2][4]) + " | " + str(self._b[2][5]) + " | " + str(self._b[2][6]) + " |")
        print(" -----------------------------")
        print(" | " + str(self._b[3][0]) + " | " + str(self._b[3][1]) + " | " + str(self._b[3][2]) + " | " + str(self._b[3][3]) + " | " + str(self._b[3][4]) + " | " + str(self._b[3][5]) + " | " + str(self._b[3][6]) + " |")
        print(" -----------------------------")
        print(" | " + str(self._b[4][0]) + " | " + str(self._b[4][1]) + " | " + str(self._b[4][2]) + " | " + str(self._b[4][3]) + " | " + str(self._b[4][4]) + " | " + str(self._b[4][5]) + " | " + str(self._b[4][6]) + " |")
        print(" -----------------------------")
        print(" | " + str(self._b[5][0]) + " | " + str(self._b[5][1]) + " | " + str(self._b[5][2]) + " | " + str(self._b[5][3]) + " | " + str(self._b[5][4]) + " | " + str(self._b[5][5]) + " | " + str(self._b[5][6]) + " |")
        print(" -----------------------------")
        return "   " + str(0) + "   " +str(1) + "   " + str(2) + "   " + str(3) + "   " + str(4) + "   " + str(5) + "   " + str(6)
    
    def __getitem__(self, ind):
        l, c = ind
        return self._b[l][c]
    
    def __setitem__(self, ind, value):
        l, c = ind
        self._b[l][c] = value

    def __str__(self):
        return str(self.display()) 
    
