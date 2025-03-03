from helpers.game import Game
from helpers.menu import Menu
import os

def main(): 
    menu = Menu()
    if (menu.playing):
        os.system('clear')
        game = Game(10, 20)
        game.render()
        

if __name__ == "__main__":
    main()