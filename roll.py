#!/usr/bin/python
import array
import random
import argparse

def roll(numberOfDice=1, diceFace=6, difficultyCheck=5):
    resultList = []
    successes = 0
    for d in range(numberOfDice):
        result = random.randint(1,diceFace)
        resultList.append(result)
        if result >= difficultyCheck:
            successes += 1
    return "Rolls: " + str(resultList) + "\nTotal: " + str(sum(resultList)) + "\nSuccesses: " + str(successes)


parser = argparse.ArgumentParser(description='Roll some dice')
parser.add_argument("dice", default=1, type=int, help='Number of dice to roll.')
parser.add_argument('-d', default=6, type=int, help='Number of sides on the dice.' )
parser.add_argument('-s', default=5, type=int, help='What results are considered a success?')
args = parser.parse_args()

numberOfDice = args.dice
if args.d:
    diceFace = args.d
if args.s:
     difficultyCheck = args.s

print (roll(numberOfDice, diceFace, difficultyCheck))


