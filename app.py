from helpers.game import Game
from helpers.menu import Menu
import curses, time

def main(stdscr): 
    clear_screen(stdscr)

    height,width = stdscr.getmaxyx()

    menu = Menu(height, width)
    game = Game(height, width)

    while True:
        menu.displayMenu(stdscr)
        stdscr.addstr(int(height*0.9), int(width/2), "Choose a option!", curses.A_BOLD) # display game title
        choice = stdscr.getch()
        if choice == ord("1"):
            stdscr.addstr(int(height*0.9), int(width/2), str(choice), curses.A_UNDERLINE) # display game title
            clear_screen(stdscr)
            stdscr.refresh()
            game.render(stdscr)
        elif choice == ord("2"):
            clear_screen(stdscr)
            stdscr.refresh()
            menu.showInstructions(stdscr)
            clear_screen(stdscr)
        elif choice == ord("3"):
            break
        else:
            stdscr.addstr(int(height*0.9), int(width/2), "Choose a valid option!", curses.A_UNDERLINE) # display game title


def clear_screen(stdscr):
    stdscr.clear()



if __name__ == "__main__":
    curses.wrapper(main)
