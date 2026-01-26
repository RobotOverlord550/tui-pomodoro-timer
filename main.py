import time
import curses
from curses import wrapper

POMODORO_WORK_TIME_SEC:int = 1500
POMODORO_BREAK_TIME_SEC:int = 300
POMODORO_CYCLES:int = 4


def timer(seconds, time_display_string: str, stdscr: curses.window):
    while(seconds):
        mins, secs = divmod(seconds, 60)
        timer: str = time_display_string.format(mins, secs)
        stdscr.addstr(0, 0, timer)
        stdscr.refresh()
        time.sleep(1)
        seconds -= 1


def start_work(stdscr: curses.window):
    timer(POMODORO_WORK_TIME_SEC, "Time left of work: {:02d}:{:02d}", stdscr)


def start_break(stdscr: curses.window):
    timer(POMODORO_BREAK_TIME_SEC, "Time left of break: {:02d}:{:02d}", stdscr)


def main(stdscr: curses.window):
    stdscr.clear()
    stdscr.addstr(0, 0, "Press any key to start timer")
    stdscr.refresh()
    stdscr.getch()
    for _ in range(POMODORO_CYCLES):
        stdscr.clear()
        start_work(stdscr)
        start_break(stdscr)


wrapper(main)