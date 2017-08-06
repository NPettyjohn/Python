def drawStars(inputList):
    outputString = ""
    for elem in inputList:
        if isinstance(elem, int):
            for counter in range(0, elem):
                outputString += "*"
            outputString += "\n"
        elif isinstance(elem, str):
            for counter in range(0, len(elem)):
                firstLetter = elem[0]
                outputString += firstLetter.lower()
            outputString += "\n"

    return outputString

# Testing section.
x = [4, 6, 1, 3, 5, 7, 25]
print drawStars(x)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print drawStars(x)
