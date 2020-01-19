from main import BlackJack
from game import Shufflin
from game import Game
import random

line = "       +------------------------------------------------------+"
gap = "       |                                                      |"
leftMargin = "       "
title = ("             ___  _    ____ ____ _  _  _ ____ ____ _  _  \n" +
         "             |__] |    |__| |    |_/   | |__| |    |_/   \n" +
         "             |__] |___ |  | |___ | \_ _| |  | |___ | \_  \n" +
         "             ==========================================    ")
credits = "                        Jose Edgar Renato"
space = "                                                               "
bot = "Bot vs Dealer"

print(line)
print(gap)
print(leftMargin)
print(title)
print(credits)
print(space)
print(space)

Game(Shufflin())

print(space)
print(space)

print(bot)
print(space)
trainingIteration = 10000
simulationIteration = 1000
game = BlackJack()
game.offPolicyMonteCarloTraining(trainingIteration)
game.playGame(simulationIteration)
print(space)
