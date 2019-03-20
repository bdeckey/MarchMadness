import random

class Game:
    def __init__(self, teamA, teamB, extra=True):
        self.teamA = teamA
        self.teamB = teamB
        self.extra = extra
        if (teamA != None and teamB != None):
            self.teamAHOS, self.teamBHOS = self.getNormalHardness()

    def play(self):
        if (self.teamA == None):
            # print(self.teamB.name + " won the Game.")
            return self.teamB
        if (self.teamB == None):
            # print(self.teamA.name + " won the Game.")
            return self.teamA

        scores = self.getScores()
        # print(self.teamA.name, scores[0], self.teamB.name, scores[1])
        if scores[0] > scores[1]:
            print(self.teamA.name + " won the Game.")
            return self.teamA
        else:
            print(self.teamB.name + " won the Game.")
            return self.teamB

    def getScores(self):
        bOpponents = self.teamB.opponents
        aOpponents = self.teamA.opponents
        similar = []
        for i in bOpponents:
            if i in aOpponents:
                if i not in similar:
                    similar += [i]
        aSimPoints = 0
        bSimPoints = 0
        for i in similar:
            aSimPoints += self.teamA.getResult(i)
            bSimPoints += self.teamB.getResult(i)
        if (self.teamA.name in bOpponents):
            aSimPoints += self.teamA.getResult(self.teamB.name)
            bSimPoints += self.teamB.getResult(self.teamA.name)
        aStats = 0
        bStats = 0

        for key in self.teamA.stats.keys():
            if (key == "Scoring Offense"):
                aStats += (((float(self.teamA.stats[key]["value"]) - 88.8) * -1) + 100) * 1.8
                bStats += (((float(self.teamB.stats[key]["value"]) - 88.8) * -1) + 100) * 1.8
            if (key == "Scoring Defense"):
                aStats += (((float(self.teamA.stats[key]["value"]) - 55.1) * -1) + 100) * 1.7
                bStats += (((float(self.teamB.stats[key]["value"]) - 55.1) * -1) + 100) * 1.7
            if (key == "Turnover Margin"):
                aStats += (((float(self.teamA.stats[key]["value"]) - 5.8) * -1) + 100) * 1.5
                bStats += (((float(self.teamB.stats[key]["value"]) - 5.8) * -1) + 100) * 1.5
            if (key == "Assist Turnover Ratio"):
                aStats += (((float(self.teamA.stats[key]["value"]) - 1.76) * -1) + 100) * 2
                bStats += ((float(self.teamB.stats[key]["value"]) - 1.76) * -1) + 100 * 2
            if (key == "Field-Goal Percentage"):
                aStats += (((float(self.teamA.stats[key]["value"]) - 53.2)*-1) + 100) * 2
                bStats += (((float(self.teamB.stats[key]["value"]) - 53.2)*-1) + 100) * 2
            if (key == "Field-Goal Percentage Defense"):
                aStats += (((float(self.teamA.stats[key]["value"]) - 36.7) * -1) + 100) * 2
                bStats += (((float(self.teamB.stats[key]["value"]) - 36.7) * -1) + 100) * 2
            if (key == "Three-Point Field-Goal Percentage"):
                aStats += float(self.teamA.stats[key]["value"]) * (float(self.teamA.stats["Three-Point Field Goals Per Game"]["value"])/4) * 1.5
                bStats += float(self.teamB.stats[key]["value"]) * (float(self.teamB.stats["Three-Point Field Goals Per Game"]["value"])/4) * 1.5

        aNormHard = aStats * (1/(self.teamAHOS * 2.5)) * 1000
        bNormHard = bStats * (1/(self.teamBHOS * 2.5)) * 1000
        if (self.extra):
            print(self.teamA.name, aStats, self.teamAHOS)
            print(self.teamB.name, bStats, self.teamBHOS)
        if (self.extra):
            print(self.teamA.name)
        aFinal = self.linearCombo(aSimPoints,aNormHard)
        if (self.extra):
            print(self.teamB.name)
        bFinal = self.linearCombo(bSimPoints,bNormHard)
        return aFinal, bFinal


    def getNormalHardness(self):
        teamAHardness = self.teamA.HOS
        teamBHardness = self.teamB.HOS
        totA = self.teamA.totGames
        totB = self.teamB.totGames
        avgA = teamAHardness/totA
        avgB = teamBHardness/totB
        if totA>totB:
            while(totA>totB):
                teamAHardness = teamAHardness - avgA
                totA = totA - 1
        if totB>totA:
            while(totB>totA):
                teamBHardness = teamBHardness - avgB
                totB = totB - 1
        return teamAHardness, teamBHardness

    def linearCombo(self, sim, stat):
        varChangeStat = (random.randint(-10,10)/100) + 1
        varChangeSim = (random.randint(-5,5)/100) + 1
        result = varChangeSim*sim + varChangeStat*stat
        if (self.extra):
            print(sim, "*", varChangeSim, "+", stat, "*", varChangeStat, "=", result)
        return result
