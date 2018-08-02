from random import randint, shuffle
from string import ascii_uppercase


def showRiddle(store):
    print("    " + store[0].replace("", " "))
    print("x     " + store[1].replace("", " "))
    print("-----------")
    print("  " + store[2].replace("", " "))
    print(store[3].replace("", " "))
    print("-----------")
    print(store[4].replace("", " "))
    return


def generate():
    multiplicand = randint(100, 999)
    multiplierOne = randint(3, 9)
    while True:
        multiplierTwo = randint(3, 9)
        if multiplierTwo != multiplierOne:
            break

    partialOne = multiplierOne * multiplicand
    partialTwo = multiplierTwo * multiplicand
    result = int(str(multiplierTwo) + str(multiplierOne)) * multiplicand
    return [str(multiplicand),
            str(multiplierTwo) + str(multiplierOne),
            str(partialOne),
            str(partialTwo),
            str(result)]


def obfuscate(store):
    chars = list(ascii_uppercase)
    shuffle(chars)
    keys = chars[0:10]
    for idx, string in enumerate(store):
        for idx, val in enumerate(keys):
            string.replace(str(idx), val)

    def replaceOccurence(string):
        for idx, val in enumerate(keys):
            string = string.replace(str(idx), val)
        return string

    return list(map(replaceOccurence, store)), dict(enumerate(keys))


store, keys = obfuscate(generate())
showRiddle(store)
