from os import listdir
import pandas as pd


SUDOKU_PATH = "sudoku"

def gamelist():
    return listdir(SUDOKU_PATH)

def loadGame(filename):
    game = []
    f=open(SUDOKU_PATH+"/"+filename)
    while True:
        line = f.readline()
        if not line:
            break
        game.append([int(x) for x in line.split()])
    return game

def transposeGame(game):
    newgame = {}
    for col in range(9):
        newgame[col]={}
        for row in range(9):
            newgame[col][row] = game[row][col]
        newgame[col]=list(newgame[col].values())
    return list(newgame.values())

def checkRow(game):
    error=[]
    for n in range(9):
        row = list(set(game[n]))
        if min(row) < 1 or max(row) > 9:
            error.append((n,'Invalid Value'))
        elif sum(row) != 45:
            error.append((n,'Invalid Answer'))
    return error

def explodeSubgame(game):
    minigame = [[] for _ in range(9)]
    error = []
    for row in range(9):
        for col in range(9):
            minigame[3*(row//3)+col//3].append(game[row][col])
    return minigame


if __name__ == "__main__":
    for game_file in gamelist():
        game = loadGame(game_file)
        game_t = transposeGame(game)
        game_mini = explodeSubgame(game)
        checked_game = checkRow(game)
        checked_game_t = checkRow(game_t)
        checked_game_mini = checkRow(game_mini)

        print("Checked",game_file)

        if len(checked_game)>0:
            print("\tROW ERROR:")
            for line, error in checked_game:
                print("\t\tLine:",(line+1),error)
        if len(checked_game_t)>0:
            print("\tCOL ERROR:")
            for line, error in checked_game_t:
                print("\t\tLine:",(line+1),error)
        if len(checked_game_mini)>0:
            print("\tSUBGAME ERROR:")
            for line, error in checked_game_mini:
                print("\t\tSubgame:",(line+1),error)
