#!/usr/bin/env python

from bs4 import BeautifulSoup
import sqlite3
import argparse
import json
from os.path import dirname, realpath



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
print(rankings)







