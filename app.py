from helpers.game import Game
from helpers.menu import Menu
from helpers.functions import clear_screen
import curses

KEY_1 = ord("1")
KEY_2 = ord("2")
KEY_3 = ord("3")

def main(stdscr: curses.window): 
    clear_screen(stdscr)

    height,width = stdscr.getmaxyx()

    menu = Menu(height, width, stdscr)

    while True:
        menu.displayMenu()
        curses.curs_set(0)  # Hide cursor

        choice = stdscr.getch()  # Get user input
        if choice == KEY_1:
            game = Game(height, width, stdscr)
            game.render()
        elif choice == KEY_2:
            clear_screen(stdscr)
            stdscr.refresh()
            menu.showInstructions(stdscr)
            clear_screen(stdscr)
        elif choice == KEY_3:
            break
        else:
            stdscr.addstr(int(height * 0.7), int(width / 2), "Choose a valid option!", curses.A_UNDERLINE)


if __name__ == "__main__":
    curses.wrapper(main)
