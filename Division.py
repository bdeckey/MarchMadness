from Team import Team
from Game import Game


class Division:
    def __init__(self, gamePairs):
        self.games = gamePairs
        self.round2 = []
        self.round3 = []
        self.finalRound = None

    def play(self):
        round2 = []
        round2 += [Game(self.games[0].play(), self.games[1].play())]
        round2 += [Game(self.games[2].play(), self.games[3].play())]
        round2 += [Game(self.games[4].play(), self.games[5].play())]
        round2 += [Game(self.games[6].play(), self.games[7].play())]
        for game in round2:
            self.round2 += [(game.teamA.name, game.teamB.name)]
        round3 = []
        round3 += [Game(round2[0].play(), round2[1].play())]
        round3 += [Game(round2[2].play(), round2[3].play())]
        for game in round3:
            self.round3 += [(game.teamA.name, game.teamB.name)]
        finalRound = Game(round3[0].play(), round3[1].play())
        self.finalRound = (finalRound.teamA.name, finalRound.teamB.name)
        return finalRound.play()