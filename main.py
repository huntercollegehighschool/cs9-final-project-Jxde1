"""
Name(s): Jade Li, Bella Becker
Name of Project: Escape the Dungeon
"""

import sys
import time
import os

def typingEffect(txt):
  for character in txt: 
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.07) 

def inputtingChoice(txt):
  for character in txt:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.07)
  choose = input()
  return choose

def quitGame():
  os.system("clear")

def intro():
  typingEffect("After defeating you in battle, the evil wizard Cornelius the Dark imprisoned you in his maze-like dungeon to slowly rot away. However, he made a mistake. You know that there is a way out of the maze. Will you be able to find it before he realizes his mistake and kills you himself? Good luck adventurer.") 
  time.sleep(1.0)

def start():
  typingEffect('\nIn front of you are two doors: a black door and a white door. Which one do you choose?')
  choice = inputtingChoice('\nEnter W for the white door or B for the black door: ')
  while choice.upper() != 'W' and choice.upper() != 'B':
    print ("\nYou must choose either W or B.")
    choice = input('\nEnter W for the white door or B for the black door: ')
  if choice.upper() == 'W':
    whitedoor()
  elif choice.upper() == 'B':
    blackdoor()

def whitedoor():
  typingEffect("\nThe door slams shut behind you, trapping you in a torch-lit cavern with three identical tunnels branching out from it. Each is flooded with a strange liquid. To your right, a bubbling green one that smells like sulfur. In the center, a smooth silver scentless one. To your left, a black, sludge-like one that smells liquorish. Which tunnel do you choose?")
  choice = inputtingChoice('\nEnter R for the tunnel on the right, C for the center tunnel, or L for the tunnel on the left: ')
  while choice.upper() != 'R' and choice.upper() != 'C' and choice.upper() != 'L':
    print('\nYou must choose either R, C, or L')
    choice = input('\nEnter C for the center tunnel, R for the right tunnel, or L for the left tunnel: ')
  if choice.upper() == 'R':
    greentunnel()
  elif choice.upper() == 'C':
    silvertunnel()
  elif choice.upper() == 'L':
    blacktunnel()

def blackdoor():
  typingEffect("\nYou find yourself in a clearing with three bridges: one made of stone, one made of glass, and one made of bone. Which one do you cross?")
  choice = inputtingChoice("\nEnter S to cross the stone bridge, G to cross the glass bridge, or B to cross the bone bridge: ")
  while choice.upper() != 'S' and choice.upper() != 'G' and choice.upper() != 'B':
    print('\nYou must choose either S, G, or B')
    choice = input('\nEnter S to cross the stone bridge, G to cross the glass bridge, or B to cross the bone bridge: ')
  if choice.upper() == 'S':
    stonebridge()
  elif choice.upper() == 'G':
    glassbridge()
  elif choice.upper() == 'B':
    bonebridge()

def greentunnel():
  typingEffect('\nThe bubbling green liquid feels suprisingly cool as you step into it. You take a few hesitant steps and then the floor comes out from under you and you\'re sucked down into the liquid. You think you\'re gonna die but it just spits you out into a familiar looking room. And then you realize that you\'re back where you started.')
  start()
def silvertunnel():
  typingEffect("\nImmediately after you step into the silver liquid, it hardens around your feet. You try to get out of it but you're glued in. But you're still moving along with the current of the silver liquid, trapped in its stream. It takes you around bend after bend then suddenly it lets go of its grip on your feet and sends you flying into a small, dark room. And you realize you're back in the first room.")
  start()
def blacktunnel():
  typingEffect("\nUpon stepping onto the black liquid, the black liquid hardens under your feet, allowing you to walk on it. You walk down the tunnel and reach a room with three exits: a water slide with a boat, a metal slide, and a ladder attached to the wall of a well. With only these exits, which do you choose?")
  choice = inputtingChoice('\nEnter W to go down the water slide, M to go down the metal slide, or L to climb down the ladder: ')
  while choice.upper() != 'W' and choice.upper() != 'M' and choice.upper() != 'L':
    print('\nYou must choose either W, M, or L')
    choice = input('\nEnter W to go down the water slide, M to go down the metal slide, or L to climb down the ladder: ')
  if choice.upper() == 'W':
    waterslide()
  elif choice.upper() == 'M':
    metalslide()
  elif choice.upper() == 'L':
    ladder()

def stonebridge():
  typingEffect("\nThe stone bridge is solid under your feet. It leads you to an elevated platform connected to three elevators. Dropping down would leave you stranded, and you can't go back. Which elevator do you choose?")
  choice = inputtingChoice("\nEnter one to enter the first elevator, two to enter the second elevator, or three to enter the third: ")
  while choice.lower() != "one" and choice.lower() != "two" and choice.lower() != "three":
    print("\nYou must choose one, two, or three.")
    choice = input("\nEnter one to enter the first elevator or two to enter the second elevator: ")
  if choice.lower() == "one":
    elevatorone()
  elif choice.lower() == "two":
    elevatortwo()
  elif choice.lower() == "three":
    elevatorthree()
def glassbridge():
  typingEffect("\nThough the bridge is made of glass, it's sturdy under your feet. It leads you to an empty chamber with two archways. One archway marks a pitch black tunnel. The other marks a tunnel lit by torches on both sides. Which do you choose?")
  choice = inputtingChoice("\nEnter PB to head into the pitch black tunnel or T to head into the tunnel lit by torches: ")
  while choice.upper() != "PB" and choice.upper() != "T":
    print("\nYou must choose PB or T.")
    choice = input("\nEnter PB to head into the pitch black tunnel or T to head into the tunnel lit by torches: ")
  if choice.upper() == "PB":
    pitchblack()
  elif choice.upper() == "T":
    torchtunnel()
def bonebridge():
  typingEffect("\nThe bone bridge leads you to an open clearing. There is a long road ahead of you. There is a saddled unicorn to your right and a motorcycle to your left. Do you chose to continue down the road by foot or ride the unicorn or motorcycle?")
  choice = inputtingChoice("\nEnter U to ride the unicorn, M to ride the motorcycle, or F to continue by foot: ")
  while choice.upper() != "U" and choice.upper() != "M" and choice.upper() != "F":
    print("\nYou must choose either U, M, or F.")
    choice = input("\nEnter U to ride the unicorn, M to ride the motorcycle, or F to continue by foot:  ")
  if choice.upper() == "U":
    typingEffect("\nYou ride the unicorn along the road for a few minutes, then reach a clearing. Somehow you have circled back to a familiar fork in the road!")
    blackdoor()
  elif choice.upper() == "M":
    typingEffect("\nYou ride the motorcycle along the road for a few minutes, then reach a clearing. Somehow you have circled back to a familiar fork in the road!")
    blackdoor()
  elif choice.upper() =="F":
    typingEffect("\nYou walk along the road for what seems like hours, then finally reach an open clearing. Somehow you have circled back to a familiar fork in the road!")
    blackdoor()
def waterslide():
  typingEffect("\nYou climb into the boat and ride down the water slide. The slide eventually falls into a chamber, where the stream is stopped by a locked door. There are four buttons to the left of the door, with an air, earth, fire, and water symbol respectively. Maybe one of these buttons will free you from the dungeon. Which one do you push?")
  choice = inputtingChoice("\nEnter air, earth, fire, or water for the specified button: ")
  while choice.lower() != "air" and choice.lower() != "earth" and choice.lower() != "fire" and choice.lower() != "water":
    print("\nYou must choose a button.")
    choice = input("\nEnter air, earth, fire, or water for the specified button: ")
  if choice.lower() == "air":
    typingEffect("\nYou press the air button, and you're lifted up by a gust of wind into a room that looks very familiar. Oh no, you're back where you started!")
    start()
  elif choice.lower() == "earth":
    typingEffect("\nYou press the earth button and the floor cracks open underneath you. You fall with a thud to a cold, stone floor. Oh no, you're back where you started!")
    start()
  elif choice.lower() == "fire":
    typingEffect("\nYou climb out of the boat and hit the button with the fire symbol. The door creaks and opens, letting in sunlight. You jump back in the boat and sail into the ocean. You have escaped. Congratulations adventurer!")
    choice = inputtingChoice("\nEnter S to play again or Q to quit the game: ")
    while choice.upper() != "S" and choice.upper() != "Q":
      print("\nYou must choose S or Q.")
      choice = input("\nEnter S to play again or Q to quit the game: ")
    if choice.upper() == "S":
      intro()
      start()
    elif choice.upper() == "Q":
      inputtingChoice("\nGoodbye. We sincerely apologize for all the suffering we put you through today.") 
      time.sleep(1.0)
      quitGame()
  elif choice.lower() == "water":
    typingEffect("\nYou press the water button and a tunnel opens up to your left. The current pushes you and your boat through this tunnel, away from the locked door. Your boat stops abruptly at the end of the tunnel, throwing you out onto a cold, stone floor. You look back for the boat but the passageway you came through has closed up behind you. Oh no! You're back where you started!")
    start()
def metalslide():
  typingEffect("\nThe metal slide leads you down to the room you started in.")
  start()
def ladder():
  typingEffect("\nYou climb over the edge and venture down the ladder. Slowly, light opens up at the bottom. You drop down to see two familiar doors. You've returned to the beginning room.")
  start()

def elevatorone():
  typingEffect("\nThe elevator door opens once you get near it, letting you walk inside. The door closes and the vibrations tell you it's moving. When the door opens, you find yourself looking at two familiar doors. You've returned to the beginning room.")
  start()
def elevatortwo():
  typingEffect("\nThe elevator door opens once you get near it, letting you walk inside. The door closes and the vibrations tell you it's moving. When the door opens, you find yourself looking at two familiar doors. You've returned to the beginning room.")
  start()
def elevatorthree():
  typingEffect("\nThe elevator door opens once you get near it, letting you walk inside. The door closes and the vibrations tell you it's moving. When the door opens, you find yourself staring at a library. Walking through it, the books on the shelves are all empty. You walk until you reach a pedestal with two books. The left is a blue book with several bookmarks sticking out. The right is a red book with gold embossing. You hope one of these will help you get out. Which do you read first?")
  choice = inputtingChoice("\nEnter left for the blue book or right for the red book: ")
  while choice.lower() != "left" and choice.lower() != "right":
    print("You must choose the left book or the right book.")
    choice = input("\nEnter left for the blue book or right for the red book: ")
  if choice.lower() == "left":
    bluebook()
  elif choice.lower() == "right":
    redbook()

def bluebook():
  typingEffect("\nYou open up the blue book to the first bookmark. Fortunately, it tells you precisely how to escape. 'Escape route: Through the white door --> tunnel with black sludge --> water slide --> fire button' Suddenly, just as you finish reading, the book sucks you in and spits you out in a familiar chamber.")
  blackdoor()
def redbook():
  typingEffect("\nYou randomly open up the book only to be sucked in immediately. The book spits you out in the room you first started in.")
  start()

def pitchblack():
  typingEffect("\nYou crawl along, keeping your hand on the wall, for what seems like forever. Then you see a light ahead of you! What could it be! You run up to it and find--NO!!! It's the room you started in.")
  start()
def torchtunnel():
  typingEffect("\nTorch tunnel winds around and around, and then suddenly you see a patch of blue sky ahead of you! You run towards it as fast as you can, but a step before you're free a wall slams down in front of you, forcing you to continue to your right. The tunnel leads you to a large cavern.")
  whitedoor()
intro()
start()



#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
