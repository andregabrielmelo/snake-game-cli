import curses

def prompt_user(stdscr: curses.window, y: int, x: int, text: str, key: int) -> bool:
    choice = stdscr.getch()
    while choice != key:
        stdscr.addstr(y, x, text)  # Display text at a valid position
        stdscr.refresh()
        choice = stdscr.getch()
    
    return True

def clear_screen(stdscr):
    stdscr.clear()    