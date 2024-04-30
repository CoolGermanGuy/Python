import random
import json

path = r'C:\Users\HBGLou.Riedel\Documents\layouts\1.json'

with open(path) as user_file:
    parsed_json = json.load(user_file)
    
board = [[{"value": 0, "solution": 9, "isChangeable": True, "isCorrect": False} for _ in range(9)] for _ in range(9)]

# translate json to python
for row in range(9):
    for column in range(9):
        board[row][column] = parsed_json[row][column]

def set(line, column, number):
    line -= 1
    column -= 1
    if board[line][column]["isChangeable"]:
        board[line][column]["value"] = number
        if board[line][column]["value"] == board[line][column]["solution"]:
            board[line][column]["isCorrect"] = True
    else:
        print("cannot change predefined number")
    checkWin()
        
def checkWin():
    for i in range(9):
        for h in range(9):
            if not board[i][h]["isCorrect"] == False or not board[i][h]["value"]:
                return False
                break
            else:
                if i == 9 and h == 9:
                    return True
                    win()
def win():
    print("you won!")
    
def drawBoard():
    outputString = "| "
    lineIteration = 0
    columnIteration = 0
    print("=========================")
    for i in range(9): # loops over ROWS
        for h in range(9): # loops over COLUMNS
            #print(f'{i + 1}:{h + 1} {board[i][h]["value"]}')
            outputString += str(board[i][h]["value"]) + " "
            columnIteration += 1
            if columnIteration % 3 == 0:
                outputString += "| "
        # for i in range(9) loop
        print(outputString)
        outputString = "| "
        lineIteration += 1
        if lineIteration % 3 == 0:
            print("=========================")
        

            
        

while checkWin() != True:
    drawBoard()
    line = int(input("Line: "))
    column = int(input("Column: "))
    number = int(input("Number: "))
    
    set(line, column, number)





