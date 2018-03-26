from Piece import Piece
import ast

WHITE = True
BLACK = False

steps={
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7
}


class Board:
    w, h = 8, 8
    Matrix =[[]]


    def __init__(self):
        self.WhiteSide = WHITE
        self.BlackSide = BLACK
        self.Matrix=[[' 0 ' for i in xrange(8)] for i in xrange(8)]

        self.Matrix[0][0]=' R '
        self.Matrix[0][1] = ' N '
        self.Matrix[0][2] = ' B '
        self.Matrix[0][3] = ' K '
        self.Matrix[0][4] = ' Q '
        self.Matrix[0][5] = ' B '
        self.Matrix[0][6] = ' N '
        self.Matrix[0][7] = ' R '

        self.Matrix[1][0] = ' P '
        self.Matrix[1][1] = ' P '
        self.Matrix[1][2] = ' P '
        self.Matrix[1][3] = ' P '
        self.Matrix[1][4] = ' P '
        self.Matrix[1][5] = ' P '
        self.Matrix[1][6] = ' P '
        self.Matrix[1][7] = ' P '

        self.Matrix[7][7] = ' r '
        self.Matrix[7][6] = ' n '
        self.Matrix[7][5] = ' b '
        self.Matrix[7][4] = ' k '
        self.Matrix[7][3] = ' q '
        self.Matrix[7][2] = ' b '
        self.Matrix[7][1] = ' n '
        self.Matrix[7][0] = ' r '

        self.Matrix[6][0] = ' p '
        self.Matrix[6][1] = ' p '
        self.Matrix[6][2] = ' p '
        self.Matrix[6][3] = ' p '
        self.Matrix[6][4] = ' p '
        self.Matrix[6][5] = ' p '
        self.Matrix[6][6] = ' p '
        self.Matrix[6][7] = ' p '

    def initialize(self):
        print("     A      B      C      D      E      F      G      H ")
        j=0
        while j<8:
            print("%d %s" %(j,self.Matrix[j]))

            j+=1

    def changeBoard(self,turn,currStep,nextStep):
        a=currStep[0]
        b=currStep[1]


        a1=nextStep[0]
        b1=nextStep[1]

        # print("[%d][%d]" %(int(b),steps[a]))
        print(self.Matrix[int(b)][steps[a]])
        print(self.Matrix[int(b1)][steps[a1]])

        temp=self.Matrix[int(b)][steps[a]]
        self.Matrix[int(b)][steps[a]]=self.Matrix[int(b1)][steps[a1]]
        self.Matrix[int(b1)][steps[a1]]=temp

        print("     A      B      C      D      E      F      G      H ")
        j = 0
        while j < 8:
            print("%d %s" % (j, self.Matrix[j]))

            j += 1




