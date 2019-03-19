#!/usr/bin/env python

from bs4 import BeautifulSoup
import sqlite3
import argparse
import json
from os.path import dirname, realpath
import os

madness = {}
directory = os.fsencode("Data")

with open("rankings.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

table = soup.find('tbody')
rows = table.find_all('tr')
rankings = {}
for row in rows:
    col = row.find_all('td')
    if (len(col) > 3):
        ranking = col[0].text
        team = col[2].text
        rankings[team] = ranking


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".html"):
        file = "Data/" + filename
        with open(file) as fp:
            soup = BeautifulSoup(fp, "html.parser")

        title = soup.find("legend")

        valid = title.text.split(")")
        ranking = valid[1].split("-")[1].strip()
        valid = valid[0].split("(")
        name = valid[0].strip()
        record = valid[1]

        table = soup.find("table")
        tables = table.find_all("table")
        season = {}
        stats = {}

        for t in tables:
            table_body = t.find('tbody')
            rows = table_body.find_all('tr')
            td = rows[0].find("td")
            text = td.text.strip()
            if ("Schedule/Results" in text):
                for row in range(len(rows)):
                    data = rows[row].find_all("td")
                    if (len(data) == 0 or len(data) == 1):
                        continue
                    else :
                        date = ""
                        oppo = ""
                        win = ""
                        home = ""
                        score = ""
                        for d in range(len(data)):
                            stripped = data[d].text.strip()
                            if (d == 0):
                                date = stripped
                            if (d == 1):
                                if (stripped[0] == "@"):
                                    oppo = stripped[2:]
                                    home = False
                                elif ("@" in stripped):
                                    splits = stripped.split("@")
                                    oppo = splits[0].strip()
                                    home = False
                                else:
                                    oppo = stripped
                                    home = True
                            if (d == 2):
                                if ("OT" in stripped):
                                    splits = stripped.split("(")
                                    stripped = splits[0].strip()

                                if (stripped[0] == "L"):
                                    win = False
                                    score = stripped[2:]
                                else:
                                    win = True
                                    score = stripped[2:]

                        oppoRanking = 353
                        if (oppo in rankings.keys()):
                            oppoRanking = rankings[oppo]
                        season[date] = {"opponent":oppo,"rank":oppoRanking,"win":win,"home":home,"score":score}
                    # print("================================")
            elif ("Team Stats" in text):
                for row in range(len(rows)):
                    data = rows[row].find_all("td")
                    if (len(data) == 3 and row != 1):
                        stat = ""
                        rank = ""
                        value = ""
                        for d in range(len(data)):
                            stripped = data[d].text.strip()
                            if (d == 0):
                                stat = stripped
                            if (d == 1):
                                rank = stripped
                            if (d == 2):
                                value = stripped
                        stats[stat] = {"rank":rank, "value":value}
            else:
                continue
        madness[name] = {"ranking":ranking,"season": season, "record": record, "stats":stats}



with open(dirname(realpath(__file__)) + '/madness.json', 'w') as outfile:
    json.dump(madness, outfile, indent=4)



