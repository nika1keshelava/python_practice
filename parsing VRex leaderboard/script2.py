import requests
from bs4 import BeautifulSoup
import pandas as pd

data = requests.get("http://interest.vrexbox.com/amz/static/")

soup = BeautifulSoup(data.text, "html.parser")

results = []
for tr in soup.find_all("tr"):
    values = [td.text for td in tr.find_all("td")]
    results.append(values)

# create lists of names,scores and games_played
names = []
scores = []
games_played = []
i = 1
while i < len(results):
    names.append(results[i][0])
    scores.append(int(results[i][1]))  # don't forget to convert type str to int.
    games_played.append(results[i][2])  # you will have to sort them later :
    i += 1

print("names: ", names)
print("scores:", scores)
print("games played: ", games_played)

lists_of_names_and_scores = []
i = 0
while i < len(results) - 1:
    lists_of_names_and_scores.append((names[i], scores[i]))
    i += 1
print("double list: ", lists_of_names_and_scores)


def sort_by_ascending_order():
    sorted_list = sorted(scores)
    return sorted_list


print("ascending order sorted list: ", sort_by_ascending_order())


def sort_by_descending_order():
    sorted_list = sorted(scores, reverse=True)
    return sorted_list


print("descending order sorted list: ", sort_by_descending_order())


def sort_double_list_by_ascending_order():
    lists_of_names_and_scores.sort(key=lambda x: x[1])
    return lists_of_names_and_scores
print("double list sorted: ", sort_double_list_by_ascending_order())


#create list of players and games

player_games_list = []
i = 0
while i < len(results)-1:
    player_games_list.append((names[i],games_played[i]))
    i+=1
print("player and games list: ", player_games_list)

people_who_play_minesweeper_list = []
for el in player_games_list:
    if "Minesweeper" in el[1]:
        people_who_play_minesweeper_list.append(player_games_list[0])
print("people who play minesweeper list: ", people_who_play_minesweeper_list)

df = pd.DataFrame(results, columns=["name", "score", "games played"])
df.to_csv("leaderboard.csv", index=False, encoding="utf-8")