class Team:
    def __init__(self, name, season, stats, record, ranking):
        self.name = name
        self.season = season
        self.stats = stats
        self.record = record
        self.ranking = ranking
        temp = record.split("-")
        self.wins = int(temp[0])
        self.losses = int(temp[1])
        self.totGames = self.wins + self.losses
        self.opponents, self.HOS, self.pointsFor, self.pointsAgainst = self.setUp(season)

    def getStats(self):
        print(self.name)
        print("HOS", self.HOS)
        print("record", self.record)
        print("Points for", self.pointsFor)
        print("Points against", self.pointsAgainst)

    def setUp(self, season):
        keys = season.keys()
        teams = []
        hardness = 0
        pointsFor = 0
        pointsAgainst = 0
        for key in keys:
            hardness += int(season[key]["rank"])
            if (season[key]["score"] != ""):
                teams += [season[key]["opponent"]]
                # print(key)
                # print(self.season[key]['score'])
                score = self.parseScore(self.season[key]['score'])
                pointsFor += score[0]
                pointsAgainst += score[1]
        return teams, hardness, pointsFor, pointsAgainst

    def getResult(self, team):
        opponents = self.opponents
        if team not in opponents:
            return None
        keys = self.season.keys()
        diff = 0
        for key in keys:
            if (team == self.season[key]["opponent"]):
                a, b = self.parseScore(self.season[key]['score'])
                diff += (a - b)
        return diff

    def parseScore(self, string):
        scores = string.split("-")
        ourScore = int(scores[0].strip())
        oppoScore = int(scores[1].strip())
        return ourScore, oppoScore




