import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('span', attrs={'class': 'short-desc'})

first_result = results[0]
print(first_result)

records = []
for result in results:
    date = result.find('strong').text[0:-2] + ". 2017"
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')["href"]
    records.append((date, lie, explanation, url))
print(records[0])

#create a tabular data structure

df = pd.DataFrame(records, columns=["date", "lie", "explanation", "url"])
df["date"] = pd.to_datetime(df["date"])
print(df.head())
df.to_csv("trump_lies.csv", index=False, encoding="utf-8")