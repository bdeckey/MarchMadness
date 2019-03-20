import json
from os.path import dirname, realpath
from dateutil.parser import parse
from Team import Team
from Game import Game
from Division import Division
import sys, networkx as nx, matplotlib.pyplot as plt

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

teams = data.keys()

nodes = []
edges = []
node_sizes = []
labels = {}
i = 0

for team in teams:
    nodes += [team]
    labels[i] = team
    node_sizes += [int(data[team]["record"].split("-")[0]) * 10]
    for game in data[team]["season"].keys():
        if ((data[team]["season"][game]["opponent"], team) not in edges):
            edges += [(team, data[team]["season"][game]["opponent"])]



# Create the graph and draw it with the node labels
g = nx.Graph()
g.add_nodes_from(nodes)
g.add_edges_from(edges)
nx.draw_random(g, node_size = node_sizes, labels=labels)

# nx.draw_random(g, node_size = node_sizes, labels=labels, with_labels=True)
plt.show()
