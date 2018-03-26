from Board import Board
from Team import Team


import  re
import sys

Team_list=[]

WHITE = True
BLACK = False


def askForPlayerSide():
    playerChoiceInput = raw_input("What side would you like to play as [white],[black]? ").lower()
    if playerChoiceInput=="white":
        print("You will play as white")
        return WHITE

    elif playerChoiceInput=="black":
        print("You will play as black")
        return BLACK

    else:
        print("your enter invalid color ,, choose white or black")
        sys.exit()

def startGame(board, playerSide):

    if board.WhiteSide == playerSide:
        print("now white side turn")
        pMove = raw_input("Enter piece to move it >>> ")
        go_pMove = raw_input("Enter Next step to move it >>> ")
        # makeMove(pMove,go_pMove)

        board.changeBoard(playerSide,pMove, go_pMove)

    elif board.BlackSide==playerSide:
        print("now black side turn")
        pMove = raw_input("Enter piece to move it >>> ")
        go_pMove = raw_input("Enter Next step to move it >>> ")
        board.changeBoard(playerSide, pMove, go_pMove)


def RegestTeam(team):
    T_name=raw_input("Enter Team name>>> ")
    T_color = askForPlayerSide()
    team = Team(T_name,T_color)
    Team_list.append(team)
    RegestPlayer(team)

def RegestPlayer(team):
    m=raw_input("How many players you want to add >>> ")
    for i in xrange(int(m)):
        P_name=raw_input("Enter player name>> ")
        team.addPlayer(P_name)



if __name__ == '__main__':
    team = Team(0,0)
    board = Board()

    while True:
        print("____________________________________")
        print("Enter 1 to Regist Team ")
        # print("Enter 2 to join Player ")
        print("Enter 3 to  Print all teams ")
        print("Enter 4 to print team information  ")
        print("Enter 5 to start play Game ")
        print("---------------------------------------")
        char=raw_input("choose number >> ")

        if char=="1":
            RegestTeam(team)
        elif char=="3":
            for i in Team_list:
                print(i)
        elif char=="4":
            t = raw_input("choose team to get information >>> ")
            for i in Team_list:
                if i.getName()==t:
                    print(i.getInformation())
        elif char=="5":
            print(board.initialize())
            while True:
                playerSide = askForPlayerSide()
                try:
                    startGame(board, playerSide)
                except KeyboardInterrupt:
                    print("SHIIIIT")
                    sys.exit()
        else:
            sys.exit()


