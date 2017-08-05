# This function will loop through a list and appent all of the strings, and sum all
# of the numbers, and then print the resulting concatenated string, and summed number.

def summarizeList(inputList):
    hasString = False
    hasNumber = False
    outputString = ""
    outputSum = 0
    for elem in inputList:
        if isinstance(elem, str):
            hasString = True
            outputString += " " + elem
        elif isinstance(elem, (int, long, float, complex)):
            hasNumber = True
            outputSum = outputSum + elem
    if hasString == True and hasNumber == True:
        typeResponseText = "The list you entered is of mixed type"
        outputString = "String: " + outputString
        outputSum = "Sum: " + str(outputSum)
        return typeResponseText, outputString, outputSum
    elif hasString == True and hasNumber == False:
        typeResponseText = "The list you entered is of string type"
        outputString = "String: " + outputString
        return typeResponseText, outputString
    elif hasString == False and hasNumber == True:
        typeResponseText = "The list you entered is of number type"
        outputSum = "Sum: " + str(outputSum)
        return typeResponseText, outputSum


# Testing the summarizeList function.
testList = ['magical unicorns',19,'hello',98.98,'world']
for elem in summarizeList(testList):
     print elem

testList = [2,3,1,7,4,12]
for elem in summarizeList(testList):
     print elem

testList = ['magical','unicorns']
for elem in summarizeList(testList):
     print elem
