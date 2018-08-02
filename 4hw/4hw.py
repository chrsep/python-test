import random
import time

#cc = 0
games = 0
errors = 0
error = 0


def unique2digits():
    while (1):
        x = random.randint(12, 98)
        if x % 11:
            return x


def createASetOfNumbers():
    while (1):
        m1 = random.randint(112, 999)
        m2 = unique2digits()
        product1 = m1 * (m2 % 10)
        if product1 < 1000:
            continue
        product2 = m1 * (m2 // 10)
        if product2 < 1000:
            continue
        answer = m1 * m2
        if answer < 10000:
            continue
        RV = [m1, m2]
        M1 = str(m1)
        M2 = str(m2)
        P1 = str(product1)
        P2 = str(product2)
        A = str(answer)
        RV.append(M1[1:] + M2 + P1[2:] + P2[2:] + A[3])
        RV.append(M1[0] + P1[0:2] + P2[0:2] + A[0:3])
        print(RV)
        return RV


def displayPuzzle(A, codekeys):
    global error, errors, games
    s = ("%d%d%d%d%d" % (A[0], A[1], A[0] * (A[1] % 10), A[0] * (A[1] // 10),
                         A[0] * A[1]))
    for i in codekeys:
        s = s.replace(str(i), codekeys[i])
    print("\n\n\n")
    print("    %s%+40s%d" % (s[0:3], "Number of errors (this game): ", error))
    print("   x %s" % s[3:5])
    print("  -----")
    print("   %s%+27s%d" % (s[5:9], "Number of games: ", games))
    print("  %s" % s[9:13])
    print("  -----")
    print(
        "  %s%+45s" % (s[13:18], "Average number of errors per game: "),
        end='')
    if (games > 0):
        print("%4.2f\n\n" % (errors / games))
    else:
        print("0.00\n\n")
    return s.isdigit()


def oneplay(A, codekeys):
    global error
    x = input("Your try? ")
    x = x.capitalize()
    if (x in codekeys.values()):
        y = input(str(x) + "=")
        if (y in str(list(codekeys))):
            if (codekeys[int(y)] == x):
                print("Correct!")
                del codekeys[int(y)]
            else:
                print("Incorrect.")
                z = error
                error = z + 1
        else:
            print("That is not a hidden value")
    else:
        print("That is not a code value")
    time.sleep(2)


def cypher():
    L = list("ABCDEFGHIJ")
    random.shuffle(L)
    return dict(enumerate(L))


while (1):
    A = createASetOfNumbers()
    codekeys = cypher()
    error = 0
    while (1):
        if (displayPuzzle(A, codekeys)):
            break
        oneplay(A, codekeys)

    print("Finished with", error, "errors. ", end='')
    errors += error
    games += 1
    play = input("Play again (Y/N): ")
    if ((play[0] == "N") or (play[0] == "n")):
        break
