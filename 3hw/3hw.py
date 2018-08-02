from random import randint, shuffle
from time import sleep


def puzzleGenerator():
    multiplicand = randint(100, 999)
    multiplierOne = randint(3, 9)
    while True:
        multiplierTwo = randint(3, 9)
        if multiplierTwo != multiplierOne:
            break
    multiplier = multiplierOne * 10 + multiplierTwo
    return [multiplicand, multiplier]


def keysGenerator():
    chars = list('ABCDEFGHIJ')
    shuffle(chars)
    return dict(enumerate(chars))


def printPuzzle(keys, puzzle, errCnt, gameCnt, avgErr):
    parts = [str(puzzle[0]),                          # Multiplicand
             str(puzzle[1]),                          # Multiplier
             str((puzzle[1] % 10) * puzzle[0]),       # Partial One
             str((int(puzzle[1] / 10)) * puzzle[0]),  # Partial Two
             str(puzzle[0] * puzzle[1])]              # Result

    temp = "\n".join(parts)
    for idx, val in keys.items():
        temp = temp.replace(str(idx), keys[idx])
    parts = temp.split("\n")
    print("""
    {p[0]:>7}           Number of errors (this game): {e}
    *{p[1]:>6}
    --------
    {p[2]:>7}           Number of games: {g}
    -{p[3]:>5}
    --------
    {p[4]:>7}           Average number of errors per game: {z:.2f}
    """.format(p=parts, e=errCnt, g=gameCnt, z=avgErr))
    return "".join(parts).isdigit()


def play(keys, puzzle, err):
    char = input("Your try?").upper()
    if(char in keys.values()):
        ans = input(char + "=")
        if(not ans.isdigit() or int(ans) not in keys.keys() or int(ans) > 9):
            print("That is not a hidden value!")
        elif(keys[int(ans)] == char):
            keys.pop(int(ans), None)
            print('Correct!')
        else:
            print("Incorrect!")
            err = err + 1
    else:
        print("That is not a code value!")
    sleep(2)
    return err


gameCount = 0
totalError = 0
while(1):
    error = 0
    puzzle = puzzleGenerator()
    keys = keysGenerator()

    while(1):
        try:
            avgErr = totalError / gameCount
        except ZeroDivisionError:
            avgErr = 0
        if(printPuzzle(keys, puzzle, error, gameCount, avgErr)):
            break
        error = play(keys, puzzle, error)
    print("Finish with {} errors".format(error))

    totalError += error
    gameCount += 1

    cont = input("Do you want to play again? ").upper()
    while cont != 'Y' and cont != 'N':
        cont = input("Do you want to play again? ").upper()
    if cont == 'N':
        break
