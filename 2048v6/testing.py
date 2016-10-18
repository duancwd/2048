from Game import *

""" 
for testing with user input
"""

def play():
    game = game2048()
    game.display()
    while True:
        move = input("your move: ")
        game.operation(move)
        game.display()

play()
