import random, os, time, sys  # imports modules
from cards import cards
from decks import deckp1, deckp2

shuffledDeck = random.sample(cards, len(cards))  # shuffled deck


def shuffleSplit():  # shuffles the deck len(cards) amount of times
    for i in range(len(cards)):
        print(shuffledDeck[i])
    counter = 0
    for i in range(26): # 26
        counter += 1
        deckp1.append(shuffledDeck[counter])
        deckp2.append(shuffledDeck[counter + 26]) # +26


def typingPrint(text):  # source of the fun text is found in the main.py file
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def start():
    os.system("clear")
    # print(deckp1) - this is for debugging
    # print(deckp2)
    time.sleep(1)
    typingPrint("LET'S START")
    time.sleep(1)


def gaming():
    # Chooses random cards from 0 to how ever big their pile is
    randCard1 = random.randrange(0, len(deckp1))
    randCard2 = random.randrange(0, len(deckp2))

    def results(): # Results.
        time.sleep(.5)
        typingPrint("Amount of Player One's Cards: " +  str(len(deckp1)) + "\n")
        time.sleep(.5)
        typingPrint("Amount of Player Two's Cards: " + str(len(deckp2)) + "\n")

    os.system("clear")
    time.sleep(.5)
    typingPrint("Your card: " + str(deckp1[randCard1]["face"]) + "\n")
    time.sleep(1)
    typingPrint("Opponent's card: " + str(deckp2[randCard2]["face"]) + "\n")
    time.sleep(1)
    # If Player One's Card is bigger than the other
    if deckp1[randCard1]["value"] > deckp2[randCard2]["value"]:
        deckp1.append(deckp2[randCard2])
        deckp2.remove(deckp2[randCard2])
        typingPrint("You Win!" + "\n")
        results()

    # If Player One's Card is lower than the other
    elif deckp1[randCard1]["value"] < deckp2[randCard2]["value"]:
        deckp2.append(deckp1[randCard1])
        deckp1.remove(deckp1[randCard1])
        typingPrint("You Lose!" + "\n")
        results()
    # If Player One's plays an ace it's lower than the other guy's two
    elif deckp1[randCard1]["value"] == 14 and deckp2[randCard2]["value"] == 2:
        deckp2.append(deckp1[randCard1])
        deckp1.remove(deckp1[randCard1])
        typingPrint("You Lose!" + "\n")
        results()
    # If Player Two plays an ace player one wins
    elif deckp1[randCard1]["value"] == 2 and deckp2[randCard2]["value"] == 14:
        deckp1.append(deckp2[randCard2])
        deckp2.remove(deckp2[randCard2])
        typingPrint("You Win!" + "\n")
        results()
    # If the cards are equal
    elif deckp1[randCard1]["value"] == deckp2[randCard2]["value"]:

        def war():
            # Multiple randoc cards from the decks
            randCardEqual1 = random.randrange(0, len(deckp1))
            randCardEqual2 = random.randrange(0, len(deckp2))
            randCardD11 = random.randrange(0, len(deckp1))
            randCardD12 = random.randrange(0, len(deckp1))
            randCardD13 = random.randrange(0, len(deckp1))
            randCardD21 = random.randrange(0, len(deckp2))
            randCardD22 = random.randrange(0, len(deckp2))
            randCardD23 = random.randrange(0, len(deckp2))

            print("War!")
            time.sleep(1)  # Every time.sleep being used is a waiting
            typingPrint("Player One will place three cards down")
            time.sleep(1)

            # Just to make it look long
            def dot():  # Just so code looks nicer
                print()
                typingPrint("•")
                time.sleep(0.5)

            dot()
            dot()
            dot()
            print()
            typingPrint("Player Two will place three cards down")

            time.sleep(1)
            dot()
            dot()
            dot()
            print()
            typingPrint("Your card: " + str(deckp1[randCardEqual1]["face"]) + "\n")
            typingPrint("Opponent's card: " + str(deckp2[randCardEqual2]["face"]) + "\n")

            # Hard coded because doing this more would make me add
            # If greater
            if deckp1[randCardEqual1]["value"] > deckp2[randCardEqual2][
                    "value"]:  # Same code but takes more cards
                deckp1.append(deckp2[randCardEqual2])
                deckp1.append(deckp2[randCardD21])
                deckp1.append(deckp2[randCardD22])
                deckp1.append(deckp2[randCardD23])
                deckp2.remove(deckp2[randCardEqual2])
                deckp2.remove(deckp2[randCardD21])
                deckp2.remove(deckp2[randCardD22])
                deckp2.remove(deckp2[randCardD23])
                typingPrint("You Win!" + "\n")
                results()

        # If lower
            elif deckp1[randCardEqual1]["value"] < deckp2[randCardEqual2][
                    "value"]:
                deckp2.extend(deckp1[randCardEqual1])
                deckp1.append(deckp1[randCardD11])
                deckp1.append(deckp1[randCardD12])
                deckp1.append(deckp1[randCardD13])
                deckp1.remove(deckp1[randCardEqual1])
                deckp1.remove(deckp1[randCardD11])
                deckp1.remove(deckp1[randCardD12])
                deckp1.remove(deckp1[randCardD13])
                typingPrint("You Lose!" + "\n")
                results()
            # Run the whole thing again if they are Equal
            elif deckp1[randCard1]["value"] == deckp2[randCard2]["value"]:
                war()
        war()

    time.sleep(2)
    typingPrint("Click Enter to go again")
    input()