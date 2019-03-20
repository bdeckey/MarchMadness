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

def getCleanList(list):
    result = []
    longest = 0
    for pair in list:
        if (pair[0] == None):
            newFirst = ""
        else:
            newFirst = pair[0]

        if (pair[1] == None):
            newSecond = ""
        else:
            newSecond = pair[1]

        if (len(newFirst) > longest):
            longest = len(newFirst)
        if (len(newSecond) > longest):
            longest = len(newSecond)

    for pair in list:
        if (pair[0] == None):
            newFirst = ""
        else:
            newFirst = pair[0]

        if (pair[1] == None):
            newSecond = ""
        else:
            newSecond = pair[1]
        newPair = (newFirst.ljust(longest), newSecond.ljust(longest))
        result += [newPair]
    space = " "
    space = space.ljust(longest+2)
    return result, space

def printDivision(starting, divisionName, division, divisionWinner):
    f = open("schedule2.txt", 'r')
    filedata = f.read()
    f.close()
    cleanStart, spacing1 = getCleanList(starting)
    finalPrint = filedata.replace("Division", divisionName)
    finalPrint = finalPrint.replace("spacing1", spacing1)
    count = 0
    for pair in cleanStart:
        finalPrint = finalPrint.replace("[" + str(count) + "]", pair[0])
        count += 1
        finalPrint = finalPrint.replace("[" + str(count) + "]", pair[1])
        count += 1
    cleanR2, spacing2 = getCleanList(division.round2)
    finalPrint = finalPrint.replace("spacing2", spacing1+spacing2)
    for pair in cleanR2:
        finalPrint = finalPrint.replace("[" + str(count) + "]", pair[0])
        count += 1
        finalPrint = finalPrint.replace("[" + str(count) + "]", pair[1])
        count += 1
    cleanR3, spacing3 = getCleanList(division.round3)
    finalPrint = finalPrint.replace("spacing3", spacing1+spacing2+spacing3)
    for pair in cleanR3:
        finalPrint = finalPrint.replace("[" + str(count) + "]", pair[0])
        count += 1
        finalPrint = finalPrint.replace("[" + str(count) + "]", pair[1])
        count += 1

    cleanWinner, spacing4 = getCleanList([division.finalRound])
    finalPrint = finalPrint.replace("spacing4", spacing1+spacing2+spacing3+spacing4)
    finalPrint = finalPrint.replace("[" + str(count) + "]", cleanWinner[0][0])
    count += 1
    finalPrint = finalPrint.replace("[" + str(count) + "]", cleanWinner[0][1])
    count += 1

    finalPrint = finalPrint.replace("[" + str(count) + "]", divisionWinner.name)
    f = open(divisionName + "Results.txt", 'w')
    f.write(finalPrint)
    f.close()

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
print("================ WEST ===========")
westWinner = West.play()
printDivision(west, "West", West, westWinner)
print("================ EAST ===========")
eastWinner = East.play()
printDivision(east, "East", East, eastWinner)
print("================ SOUTH ===========")
southWinner = South.play()
printDivision(south, "South", South, southWinner)
print("================ MIDWEST =========")
midwestWinner = Midwest.play()
printDivision(midwest, "Midwest", Midwest, midwestWinner)
print("==================================")

print("Winner of the West Division:", westWinner.name)
print("Winner of the East Division:", eastWinner.name)
print("Winner of the South Division:", southWinner.name)
print("Winner of the Midwest Division:", midwestWinner.name)

fin1 = Game(eastWinner, westWinner).play()
fin2 = Game(southWinner, midwestWinner).play()
Game(fin1,fin2).play()




