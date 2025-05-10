import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the WPM Test!\n")
    stdscr.refresh()
    stdscr.getkey()  # Wait for a key press
    
wrapper(main)