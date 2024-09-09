import os

EMPTY_MATRIX = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]

i = 0

def Check4InList(array):
    """Looks for exactly 4 same elements in a list"""
    ONE_PATTERN, TWO_PATTERN = [1, 1, 1, 1], [2, 2, 2, 2]

    for i in range(len(array) - 4 + 1):
        if array[i:i+4] == ONE_PATTERN:
            return 1
        elif array[i:i+4] == TWO_PATTERN:
            return 2
        else:
            continue
    return 0


def RotateMatrix(matrix):
    """Roates matrix by 90"""
    rows, cols = len(matrix), len(matrix[0])
    rotatedMatrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotatedMatrix[j][rows - 1 - i] = matrix[i][j]
    return rotatedMatrix


def DiagonalLists(matrix):
    """Remaps diagnoals onto a list of lists"""
    m = matrix
    diags = [
        [m[2][0], m[3][1], m[4][2], m[5][3]],
        [m[1][0], m[2][1], m[3][2], m[4][3], m[5][4]],
        [m[0][0], m[1][1], m[2][2], m[3][3], m[4][4], m[5][5]],
        [m[0][1], m[1][2], m[2][3], m[3][4], m[4][5], m[5][6]],
        [m[0][2], m[1][3], m[2][4], m[3][5], m[4][6]],
        [m[0][3], m[1][4], m[2][5], m[3][6]],
        [m[0][3], m[1][2], m[2][1], m[3][0]],
        [m[0][4], m[1][3], m[2][2], m[3][1], m[4][0]],
        [m[0][5], m[1][4], m[2][3], m[3][2], m[4][1], m[5][0]],
        [m[0][6], m[1][5], m[2][4], m[3][3], m[4][2], m[5][1]],
        [m[1][6], m[2][5], m[3][4], m[4][3], m[5][2]],
        [m[2][6], m[3][5], m[4][4], m[5][3]]
        ]
    return diags


def CheckRows(matrix):
    """Looks for winner in all rows"""
    for list in matrix:
        checkedList = Check4InList(list)
        if checkedList != 0:
            return checkedList
        else: 
            continue
    return 0


def CheckCols(matrix):
    """Looks for winner in all columns"""
    rotatedMatrix = RotateMatrix(matrix)

    for list in rotatedMatrix:
        checkedList = Check4InList(list)
        if checkedList != 0:
            return checkedList
        else: 
            continue
    return 0


def CheckDiags(matrix):
    """Looks for winner in all diagnoals"""
    diags = DiagonalLists(matrix)

    for list in diags:
        checkedList = Check4InList(list)
        if checkedList != 0:
            return checkedList
        else:
            continue
    return 0


def WinnerCheck(matrix):
    """Looks for Winner"""
    if CheckRows(matrix) != 0:
        return CheckRows(matrix)
    elif CheckCols(matrix) != 0:
        return CheckCols(matrix)
    elif CheckDiags(matrix) != 0:
        return CheckDiags(matrix)
    else:
        return 0
    

def DeterminePlayer():
    """Flip-flop to the players take turns"""
    global i
    if i % 2 == 0:
        piece = 1
    else:
        piece = 2
    i += 1
    return piece

def PromptPlayer():
    """Prompts player and catches wrong inputs"""
    VALID_CHOICES = [1, 2, 3, 4, 5, 6, 7]

    while (True):
        choice = input("Please select a column! 1 - 7: ")
        try:
            choice = int(choice)
        except:
            continue

        if choice in VALID_CHOICES:
            return int(choice) - 1
        else: 
            continue
    

def PlacePiece(matrix, column, player):
    """Places piece into correct column"""
    newMatrix = matrix.copy()

    for row in newMatrix:
        if row[column] == 0:
            row[column] = player
            break
    return newMatrix


def WinnerAnnouncement(verdict):
    """Gets verdict from WinnerCheck and chooses what to say"""
    match verdict:
        case 0: pass
        case 1: return "Player 1 wins!"
        case 2: return "Player 2 wins!"


def ConvertZero(num):
    """Literally converts 0 to _"""
    if num == 0:
        return "_"
    else:
        return num
    

playMatrix = EMPTY_MATRIX.copy()

while(True):
    os.system("cls")
    print(" 1  2  3  4  5  6  7")
    print(" v  v  v  v  v  v  v")
    for row in reversed(playMatrix):
        for element in row:
            print(f" {ConvertZero(element)} ", end="")
        print("")

    verdict = WinnerCheck(playMatrix)

    if verdict == 0:
        choice = PromptPlayer()
        playMatrix = PlacePiece(playMatrix, choice, DeterminePlayer())
    else:
        print(WinnerAnnouncement(verdict))
        break