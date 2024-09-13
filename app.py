import os

matrix = list[list[int | str]]

EMPTY_MATRIX: matrix = [[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]

i = 0

def Check4InList(list: list) -> int:
    """Looks for exactly 4 same elements in a list"""
    ONE_PATTERN, TWO_PATTERN = [1, 1, 1, 1], [2, 2, 2, 2]

    for i in range(len(list) - 4 + 1):
        if list[i:i+4] == ONE_PATTERN:
            return 1
        elif list[i:i+4] == TWO_PATTERN:
            return 2
        else:
            continue
    return 0


def RotateMatrix(matrix: matrix) -> matrix:
    """Roates matrix by 90"""
    rows, cols = len(matrix), len(matrix[0])
    rotatedMatrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotatedMatrix[j][rows - 1 - i] = matrix[i][j]
    return rotatedMatrix


def DiagonalLists(matrix: matrix) -> matrix:
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


def CheckRows(matrix: matrix) -> matrix | int:
    """Looks for winner in all rows"""
    for list in matrix:
        checkedList = Check4InList(list)
        if checkedList != 0:
            return checkedList
        else: 
            continue
    return 0


def CheckCols(matrix: matrix) -> matrix | int:
    """Looks for winner in all columns"""
    rotatedMatrix = RotateMatrix(matrix)

    for list in rotatedMatrix:
        checkedList = Check4InList(list)
        if checkedList != 0:
            return checkedList
        else: 
            continue
    return 0


def CheckDiags(matrix: matrix) -> matrix | int:
    """Looks for winner in all diagnoals"""
    diags = DiagonalLists(matrix)

    for list in diags:
        checkedList = Check4InList(list)
        if checkedList != 0:
            return checkedList
        else:
            continue
    return 0


def WinnerCheck(matrix: matrix) -> matrix | int:
    """Looks for Winner"""
    if CheckRows(matrix) != 0:
        return CheckRows(matrix)
    elif CheckCols(matrix) != 0:
        return CheckCols(matrix)
    elif CheckDiags(matrix) != 0:
        return CheckDiags(matrix)
    else:
        return 0
    

def DeterminePlayer() -> int:
    """Flip-flop to the players take turns"""
    global i
    if i % 2 == 0:
        i += 1
        return 1
    else:
        i += 1
        return 2

def PromptPlayer() -> int:
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
    

def PlacePiece(matrix: matrix, player: int) -> matrix:
    """Places piece into correct column"""
    choice = PromptPlayer()
    newMatrix = matrix.copy()

    for row in newMatrix:
        if row[choice] == 0:
            row[choice] = player
            break
    return newMatrix


def WinnerAnnouncement(verdict: int) -> str | None:
    """Gets verdict from WinnerCheck and chooses what to say"""
    match verdict:
        case 1: return "Player 1 wins!"
        case 2: return "Player 2 wins!"
        case _: return None


def ConvertZero(num: int) -> str | int:
    """Literally converts 0 to _ to prettify field"""
    if num == 0:
        return "_"
    else:
        return num
    

def PrintMatrix(matrix: matrix) -> None:
    os.system("cls")
    print(" 1  2  3  4  5  6  7")
    print(" v  v  v  v  v  v  v")
    for row in reversed(matrix):
        for element in row:
            print(f" {ConvertZero(element)} ", end="")
        print("")
    

playMatrix: matrix = EMPTY_MATRIX.copy()

while(True):
    PrintMatrix(playMatrix)

    hasWinner: int = WinnerCheck(playMatrix)

    if hasWinner != 0:
        print(WinnerAnnouncement(hasWinner))
        break
    else:
        playMatrix = PlacePiece(playMatrix, DeterminePlayer())