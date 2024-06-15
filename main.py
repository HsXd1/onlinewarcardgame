# My War
from config import shuffleSplit, start, gaming
from decks import deckp1, deckp2
import os, time, sys
# First prompt to start


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


os.system("clear")
input("Press Enter to Start:")
typingPrint("Shuffling the Deck, please wait...")
time.sleep(2)
shuffleSplit()
start()
while len(deckp1) != 0 or len(deckp2) != 0:  # Loops the game until someone wins
  if len(deckp1) == 0 or len(deckp2) == 0:
    print("You have won the battle, and the war. o7, Soldier.")
    sys.exit()
  else: 
    gaming()


# typing animation: https://www.101computing.net/python-typing-text-effect/
