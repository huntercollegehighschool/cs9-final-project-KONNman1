"""
Name: Kai Nizhner
Name of Project: A New World (Choose your own adventure project - modified).

OVERVIEW:
main.py is used to start and run the game as a whole
ANewWorldIntroText.py is used as introduction text.
GameStage1.py is the first level of the game.
GameStage2.py is the second level of the game. (will finish outside of class)
GameStage3.py is the third level of the game. (will finish outside of class)
NextStepEndText.py is used as exit text for the game, and to set up a future part.

NOTE:
I meant to have more than 2 levels in this game (found in GameStage1.py) -- this is a very simplified version of my original plan (I also meant to have a money system involved in the game). The coding was really complex for me; I have no prior experience coding outside of this class so it's somewhat inefficient from the start and there were some funky choices I made that I had to deal with later, including usage of recursion. 
What I have now meets the requirements for the project, I believe, so I'm handing it in as is to meet the (extended) due date. If I have time, outside of class, I'll continue with this game: I'll add more parts to the preliminary section (that's why GameStage2 and GameStage3 are commented out) and I'll add to the story as a whole, building off the "NextStepEndText.py" file.

NOTE 2: 
Sorry, the text is super dense! 150+ lines will not be fun to read ... hopefully the game is fun to play, at least!
"""


import os
import time
os.system('clear')

def sleepandclear():
  time.sleep(1)
  os.system('clear')

start = input("Start game? yes / no: ").lower()
while start not in ["yes", "y", "no", "n"]:
  sleepandclear()
  print("That was not an option.")
  sleepandclear()
  start = input("Start game? yes / no: ").lower()
  
if start == "yes" or start == "y":
  sleepandclear()
  print("Game starting.")
  sleepandclear()
  import ANewWorldIntroText
  import GameStage1
  #import GameStage2
  #import GameStage3
  import NextStepEndText
  
elif start == "no" or start == "n":
  sleepandclear()
  print("You're missing out.")
  sleepandclear()