import requests
from bs4 import BeautifulSoup
from time import localtime, strftime
import smtplib

day = strftime("%d", localtime())
month = strftime("%m", localtime())
year = strftime("%y", localtime())

#HTML Architecture and list notes:
#scoreboard will hold a list of the scoreboards
#each scoreboard will have a list of their own with each piece of HTML content inside

url = 'http://www.cbssports.com/nba/scoreboard/' + year + month + day

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

scoreboard = soup.find_all("div", {"class": "scoreBox spanCol2"})

body = " "

for item in scoreboard:
    try:

        gameInfo = item.contents[1]

    except:

        body = "Sorry, no games tonight!!!"

    try: 

        playersOfTheNight = item.contents[2]

    except: 

        body = body + "\n I guess that means there are no players of the night either!!!"

#All the game info is in game stats
gameStats = []
try: 
    for item in gameInfo.contents[0].find_all("td"):
        gameStats.append(item.text)
except:
    body = body + "\n no games man!"
#The index of each array holds information on each team
try: 
    teamNames = [gameStats[2], gameStats[8]]
    firstQuarter = [gameStats[3], gameStats[9]]
    secondQuarter = [gameStats[4], gameStats[10]]
    thirdQuarter = [gameStats[5], gameStats[11]]
    fourthQuarter = [gameStats[6], gameStats[12]]
    total = [gameStats[7], gameStats[13]]
except:
    pass


#All the info on players of the game are stored in playerStats
playerStats = []

try: 
    for items in playersOfTheNight.contents[0].find_all("td"):
        playerStats.append(items.text)
    body = "Alright here's the downlow on the orange things in the hoop! \n" + "The matchup is " + teamNames[0] + " VS " + teamNames[1] + "\n" + teamNames[0] + " | " + firstQuarter[0] +  " | " +  secondQuarter[0] +  " | " + thirdQuarter[0] +  " | " + fourthQuarter[0] +   " | Total: " + total[0] + "\n" + teamNames[1] + " | " + firstQuarter[1] +  " | " +  secondQuarter[1] +  " | " + thirdQuarter[1] +  " | " + fourthQuarter[1] +   " | Total: " + total[1] + "\n" + playerStats[0] + "\n" + playerStats[1] + "\n" + playerStats[2]
except:
    pass


#Lets email myself the body
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jarvisfromparkdale@gmail.com', 'parkdaleci')
    server.sendmail('jarvisfromparkdale@gmail.com', 'shababayub@gmail.com', body)
except:
    pass



















