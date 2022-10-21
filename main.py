import requests
import re
import pandas as pd

df = pd.read_csv('PlayersInDB.csv')

counter = 0

fideimgArr = []
fideIdArr = []


for i in df['Custom']:
    try:
        x = requests.get(i)
        data = x.text
        print("Trying to pull Picture of Player: " + i)

        fideimg = re.findall("class=\"player-pic \" src=\"(.*)\"", data)[0]
        fideIdArr.append(str(df['fideID'][counter]))
        print(i)
        print(fideimg)
        print(counter)
        fideimgArr.append("https://players.chessbase.com"+fideimg)
        counter += 1

    except Exception as e:
        print(e)
        print("Failed")
        counter +=1


df1 = pd.DataFrame(fideIdArr, columns=['fideID'])
df1.to_csv("fideIDPlayer.csv", sep=',')

df2 = pd.DataFrame(fideimgArr, columns=['playerImage'])
df2.to_csv("playerImages.csv", sep=',')
