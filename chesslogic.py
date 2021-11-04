from dataclasses import dataclass
import math 


board_starting_state = [['BR', 'BN', 'BB', 'BK', 'BQ', 'BB', 'BN', 'BR'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['WR1', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR2']]

class Chesslogic:
    def __init__(self):
        self.pastList = []
        self.castling = False

    def setBoard(self, board_list):
        self.board = board_list
    
    #def extractDifference(self):
    #    init_diff = []
    #    final_diff = []
    #    for i in range (8):
    #        for j in range (8):
    #            if self.initial_board != self.board:
    #                init_diff.append((self.initial_board, i, j))
    #                final_diff.append((self.board, i, j))
    #    if len(init_diff > 2): self.castling = True
    #    if init_diff[0][0] != 'EE':
    #        self.pieceName = init_diff[1][0]
    #        self.fromPos = (init_diff[1][1], init_diff[1][2])
    #        self.toPos = (init_diff[0][1], init_diff[0][2])
    #    else:
    #        self.pieceName = init_diff[]

    
    def validKnightMove(self, fromPos, toPos):
        from_x = fromPos[1]
        from_y = fromPos[0]
        to_x = toPos[1]
        to_y = toPos[0]
        if abs(to_x - from_x) == 2 and abs(to_y - from_y) == 1:
            return True
        elif abs(to_x - from_x) == 1 and abs(to_y - from_y) == 2:
            return True
        else: 
            return False
    
    def validateRookMove(self, fromPos, toPos):
        from_x = fromPos[1]
        from_y = fromPos[0]
        to_x = toPos[1]
        to_y = toPos[0]

        if (from_x == to_x):
            if (to_y > from_y):
                for i in range (from_y, to_y):
                    if self.board[from_x][i][0] != 'E':
                        return False
            else:
                for i in range(to_y, from_y):
                    if self.board[from_x][i][0] != 'E':
                        return False
            return True
        elif (from_y == to_y):
            if (to_x > from_x):
                for i in range (from_x, to_x):
                    if self.board[i][from_y][0] !=  'E':
                        return False
            else:
                for i in range (to_x, from_x):
                    if self.board[i][from_y][0] != 'E':
                        return False
            return True
        else:
            return False

    def validateQueenMove(self, fromPos, toPos):
        from_x = fromPos[1]
        from_y = fromPos[0]
        to_x = toPos[1]
        to_y = toPos[0]
        
        if (abs(to_x - from_x) == abs(to_y - from_y)):
            if (from_x > to_x) and (from_y > to_y):
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x - i][from_y - i][0] != 'E':
                        return False
            elif (from_x < to_x) and (from_y > to_y):
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x + i][from_y - i][0] != 'E':
                        return False
            elif (from_x > to_x) and (from_y < to_y):
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x - i][from_y + i][0] != 'E':
                        return False
            else:
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x + i][from_y + i][0] != 'E':
                        return False
            return True


        elif (from_x == to_x):
            if (to_y > from_y):
                for i in range (from_y, to_y):
                    if self.board[from_x][i][0] != 'E':
                        return False
            else:
                for i in range(to_y, from_y):
                    if self.board[from_x][i][0] != 'E':
                        return False
            return True
        elif (from_y == to_y):
            if (to_x > from_x):
                for i in range (from_x, to_x):
                    if self.board[i][from_y][0] != 'E':
                        return False
            else:
                for i in range (to_x, from_x):
                    if self.board[i][from_y][0] != 'E':
                        return False
            return True
        else:
            return False
    
    def validPawnMove(self, fromPos, toPos):
        from_x = fromPos[1]
        from_y = fromPos[0]
        to_x = toPos[1]
        to_y = toPos[0]
        print("from_x", from_x)
        print("from_y", from_y)
        print("to_x", to_x)
        print("to_y", to_y)
        if (from_x != to_x):
            if (abs(to_x - from_x) == 1) and (to_y - from_y == 1):
                if self.board[to_x][to_y][0] == 'B':
                    return True
        else:
            if (to_y == 3) and (from_y == 1):
                print("A")
                return True
            elif(to_y - from_y== 1):
                return True
        return False

    def validBishopMove(self, fromPos, toPos):
        from_x = fromPos[1]
        from_y = fromPos[0]
        to_x = toPos[1]
        to_y = toPos[0]
        
        if (abs(to_x - from_x) == abs(to_y - from_y)):
            if (from_x > to_x) and (from_y > to_y):
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x - i][from_y - i][0] != 'E':
                        return False
            elif (from_x < to_x) and (from_y > to_y):
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x + i][from_y - i][0] != 'E':
                        return False
            elif (from_x > to_x) and (from_y < to_y):
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x - i][from_y + i][0] != 'E':
                        return False
            else:
                for i in range (abs(to_x - from_x)):
                    if self.board[from_x + i][from_y + i][0] != 'E':
                        return False
            return True
        return False

    def validKingMove(self, fromPos, toPos):
        from_x = fromPos[1]
        from_y = fromPos[0]
        to_x = toPos[1]
        to_y = toPos[0]

        if(abs(to_x - from_x)<= 1) and (abs(to_y - from_y) <= 1):
            return True
        else:
            return False
        



    def validGeneral(self, fromPos, toPos):
        from_x = fromPos[0]
        from_y = fromPos[1]
        to_x = toPos[0]
        to_y = toPos[1]

        if(from_x == to_x) and (from_y == to_y):
            print("caseA ")
            return False
        if self.board[to_x][to_y][0] == 'W':
            print("case B: cannot move to your occupied place with your current piece ")
            return False
        if self.board[from_x][from_y][0] == 'E':
            print("case C")
            return False
        if (to_x > 7 or to_x < 0 or to_y > 7 or to_y < 0):
            print("out of range")
            return False
        
        return True
    

    
    def validate(self, fromPos, toPos):
        from_x = fromPos[0]
        from_y = fromPos[1]
        to_x = toPos[0]
        to_y = toPos[1]
        print("curr cell: ", self.board[from_x][from_y])
        pieceName = self.board[from_x][from_y][1]
        pieceValid = False
    
        print("Piece type: ", pieceName)
        print("fromPos", fromPos)
        if pieceName == 'Q':
            pieceValid = self.validateQueenMove( fromPos, toPos)
        elif pieceName == 'R':
            pieceValid = self.validateRookMove( fromPos, toPos)
        elif pieceName == 'N':
            pieceValid = self.validKnightMove( fromPos, toPos)
        elif pieceName == 'K':
            pieceValid = self.validKingMove( fromPos, toPos)
        elif pieceName == 'P':
            pieceValid = self.validPawnMove(fromPos, toPos)
        elif pieceName == 'B':
            pieceValid = self.validBishopMove(fromPos, toPos)
        print("piece valid", pieceValid)
        if (pieceValid and self.validGeneral(fromPos, toPos)):
            self.pastList.append(self.board[from_x][from_y])
            print("output: T")

            return True
        return False
    
    def printCurrentBoard(self):
        print("---------------------------------------")
        for i in range (8):
            print("\n")
            for j in range (8):
                print (self.board[i][j] + " ")
    
    #function for testing purposes so i dont have to create list everytime
    def updateBoardState(self, fromp, top):
        from_x = fromp[1]
        from_y = fromp[0]
        to_x = top[1]
        to_y = top[0]
        if self.board[from_y][from_x] == 'EE':
            print("error")
        final_board = self.board.deepcopy()
        final_board[from_y][from_x] = 'EE'
        final_board[to_y][to_x] = self.board[from_y][from_x]
        self.board = final_board

    
#initialize the past actions list after game is over
    def resetPastList(self):
        self.pastList = []


