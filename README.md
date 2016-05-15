# NBA-Python-Web-Crawler

This web-crawler crawls through the CBS Sports page and scrapes specific data relevant to the NBA games played that night. This data is then emailed to a user. 
By setting up a scheduled task (Windows), this script can be ran daily. 

###Motivation:
I got busy with school so I couldn't check the scores daily even though crazy stuff was going on in the playoffs. I also wanted some experience with automation in Python. 

###How to use:
Follow the steps below if you want to run this for yourself
- Download the file from this repo.
- Install Python.
- Run the following in command line: 
- ```pip install requests```
- ```pip install bs4 ```
- Add your email to the code (replace my email).
- Set up a scheduled task in Windows to run the script daily (would recommend setting it at night, ~2am when all games are done)

###Future Implementation:
 - Refactor crawler into a class that can scrape data from multiple pages for multiple sports throughout the year
 - Based on time of year calls different functions correlating to sports leagues active at the time
 - Use a texting API to send text updates instead of emails

