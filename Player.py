

class Player:
    def __init__(self,name,team):
        self.team=team
        self.name=name

    def getName(self):
        print(self.name)

    def getTeam(self):
        print(self.team)

    def __str__(self):
        return self.name