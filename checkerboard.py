# This function just creates prints a checkerboard pattern of stars in the console
def printCheckerboard(numberOfTimes):
    outputString = ""
    for counter in range(0, numberOfTimes):
        if counter % 2 == 0:
            outputString += "\n" + " * * * *"
        else:
            outputString += "\n" + "* * * *"

    return outputString

# Test the function.
print printCheckerboard(1200000)
