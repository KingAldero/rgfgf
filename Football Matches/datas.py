import requests
import sqlite3
from bs4 import BeautifulSoup as bs
import pandas as pd
URL_TEMPLATE = "https://www.readfootball.com/football-england/teams/arsenal/calendar.html"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
match_day = soup.find_all('td', class_='epl')
matches_days = []
for name in match_day:
    a = name.text
    matches_days.append(a)
##for i in range(75):
##    a = matches_days[i]
match_time = []
match_league = []
for i in range(76):
    if i % 2 != 0:
        a = matches_days[i][8:]
        match_time.append(a)
    else:
        a = matches_days[i]
        match_league.append(a)
matches_r = soup.find_all('td', class_='comm tright chooseteam')
match_names_r = []
for i in matches_r:
    d = i.text
    match_names_r.append(d)

matches_l = soup.find_all('td', class_='comm tleft chooseteam')
match_names_l = []
for i in matches_l:
    d = i.text
    match_names_l.append(d)

matches = []
for i in range(38):
    top = str(match_league[i]) + " " + str(match_time[i]) + " " + str(match_names_r[i]) + " - " + str(match_names_l[i])

    matches.append(top)

#year
year = []
for i in range(76):
    if i % 2 != 0:
        a = "20" + matches_days[i][6:8]
        year.append(a)

#month
month = []
for i in range(76):
    if i % 2 != 0:
        a = matches_days[i][3:5]
        month.append(a)

#day
day = []
for i in range(76):
    if i % 2 != 0:
        a = matches_days[i][0:2]
        day.append(a)
print(matches)

