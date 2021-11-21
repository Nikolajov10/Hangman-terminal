from game import HangmanGame
from time import sleep
from curses import wrapper,echo,start_color,color_pair,init_pair,COLOR_RED,\
    COLOR_BLACK

def initColors():
    start_color()
    init_pair(1, COLOR_RED, COLOR_BLACK)

def printTrys(stdscr,trys,row)->None:
    first = False
    col = 0
    stdscr.addstr(row,col,"Trys: ")
    col += 6
    for t in trys:
        if not first: first = True
        else:
            stdscr.addstr(row,col,",",color_pair(1))
            col += 1
        stdscr.addstr(row,col,t,color_pair(1))
        col += len(t)

def main(stdscr):
    stdscr.clear()
    initColors()
    game = HangmanGame()
    bad_trys = []
    hited = set()
    game.startGame()
    word = ["*"] * len(game.getWord())
    row = 1
    stdscr.addstr("Welcome to Hangman game!")
    echo()
    started = False
    while True:
        if not started:
            stdscr.addstr(row,0,"Do you wanna play?(y/n)")
            play = stdscr.getstr().decode(encoding="utf-8")
            if play != "y" and play !="yes":
                stdscr.clear()
                break
            started = True
            stdscr.clear()
            row  = 0

        stdscr.addstr(row,0,"Current word: " + "".join(word))
        row += 1
        stdscr.addstr(row,0,"Mistakes:" + str(game.getMistakes()))
        row += 1
        printTrys(stdscr,bad_trys,row)
        row += 1
        stdscr.addstr(row,0,"Enter word or letter:")
        row += 1
        stdscr.refresh()
        user_input = stdscr.getstr().decode(encoding="utf-8")
        if len(user_input) < 2  and user_input not in hited:
            positions = game.checkLetter(user_input)
            if positions:
                for pos in positions:
                    word[pos] = user_input
                hited.add(user_input)
            else:
                bad_trys.append(user_input)
        elif user_input not in hited:
            game.checkWord(user_input)
            if not game.isEnd(): bad_trys.append(user_input)
        if game.isEnd():
            stdscr.addstr(row,0,game.endGame())
            stdscr.refresh()
            bad_trys = []
            sleep(2.5)
            game.startGame()
            word = ["*"] * len(game.getWord())
            stdscr.clear()
            row = 0
            started = False
        if row == 12:
            sleep(1)
            stdscr.clear()
            row = 0

wrapper(main)