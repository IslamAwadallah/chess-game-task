from Player import Player

WHITE=True
BLACK=False

class Team:
    name='0'
    players_member=[]
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def __str__(self):
        return self.name

    def addPlayer(self,player_name):
        player=Player(player_name,self)
        self.players_member.append(player)
        player.getName()
        player.getTeam()


    def getInformation(self,a):
        print("Team name is --> ",self.getName())
        # print("Team color is --> ",self.getColor())
        if self.getColor() == False:
            print(" Team color is ===> 'Black' ")
        else:
            print(" Team color is ===> 'White' ")
        if self.players_member:
            for i in self.players_member:
                # print(type(i.getTeam().getName()))
                if i.getTeam().getName()==a:
                    print i
        else:
            print("No members up to now ")
