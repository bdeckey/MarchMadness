import json
from os.path import dirname, realpath
from dateutil.parser import parse
from Team import Team
from Game import Game
from Division import Division

with open('madness.json') as f:
    data = json.load(f)


def getTeam(name):
    if (name not in data.keys()):
        return None
    info = data[name]
    season = info["season"]
    stats = info['stats']
    record = info['record']
    ranking = info['ranking']
    return Team(name, season, stats, record, ranking)

def makeDivision(division):
    final = []
    for game in division:
        team1 = getTeam(game[0])
        team2 = getTeam(game[1])
        final += [Game(team1, team2)]
    return final


east = [("Duke", None),
            ("VCU","UCF"),
            ("Mississippi St.", "Liberty"),
            ("Virginia Tech", "Saint Louis"),
            ("Maryland", None),
            ("LSU", "Yale"),
            ("Louisville","Minnesota"),
            ("Michigan St.", "Bradley")]

west = [("Gonzaga", None),
        ("Syracuse", "Baylor"),
        ("Marquette", "Murray St."),
        ("Florida St.", "Vermont"),
        ("Buffalo", "Arizona St."),
        ("Texas Tech", "Northern Ky."),
        ("Nevada", "Florida"),
        ("Michigan","Montana")]

south = [("Virginia",None),
        ("Mississippi","Oklahoma"),
        ("Wisconsin","Oregon"),
        ("Kansas St.", "UC Irvine"),
        ("Villanova","Saint Mary's"),
        ("Purdue","Old Dominion"),
        ("Cincinnati","Iowa"),
        ("Tennessee", "Colgate")]

midwest = [("North Carolina", None),
        ("Utah St.","Washington"),
        ("Auburn","New Mexico St."),
        ("Kansas","Northeastern"),
        ("Iowa St.","Ohio St."),
        ("Houston","Georgia St."),
        ("Wofford", "Seton Hall"),
        ("Kentucky", "Abilene Christian")]

print("=================================================")

eastDiv = makeDivision(east)
westDiv = makeDivision(west)
southDiv = makeDivision(south)
midDiv = makeDivision(midwest)

West = Division(westDiv)
East = Division(eastDiv)
South = Division(southDiv)
Midwest = Division(midDiv)

westWinner = West.play()
eastWinner = East.play()
southWinner = South.play()
midwestWinner = Midwest.play()

print("Winner of the West Division:", westWinner.name)
print("Winner of the East Division:", eastWinner.name)
print("Winner of the South Division:", southWinner.name)
print("Winner of the Midwest Division:", midwestWinner.name)

fin1 = Game(eastWinner, westWinner, True).play()
fin2 = Game(southWinner, midwestWinner, True).play()
Game(fin1,fin2, True).play()




