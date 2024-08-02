import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
URL_TEMPLATE = "https://www.flashscore.com.ua/team/arsenal/hA1Zm19f/"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
all_matches = soup.find_all('p', class_='event__participant event__participant--home')
match_names = []
for name in all_matches:
    a = name.text
    match_names.append(a)
print(match_names)
