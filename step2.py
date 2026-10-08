import numpy as np
import pandas as pd

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()
print()
print(chat.size)
print()
print("Chat total: ", chat.sum())
print("Video total: ", video.sum())
print("Study total: ", study.sum())
print("Games total: ", games.sum())
print()
print("Chat mean: ", round(chat.mean(), 1))
print("Video mean: ", round(video.mean(), 1))
print("Study mean: ", round(study.mean(), 1))
print("Games mean: ", round(games.mean(), 1))
print()
study_minus_games = study - games
print("best study minus game day - ", int(study_minus_games.argmax())+1)
print("worst study minus game day - ", int(study_minus_games.argmin())+1)
print()
app = ["Chat", "Video", "Study", "Games"]
winners = []
for i in range(30):
    val = np.array([chat[i],video[i],study[i],games[i]])
    winners.append(app[val.argmax()])
print(winners)
print()
total = chat + video + study + games
chat_share = (chat/total) * 100
video_share = (video/total) * 100
study_share = (study/total) * 100
games_share = (games/total) * 100
print(chat_share)
print(video_share)
print(study_share)
print(games_share)