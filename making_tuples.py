
# Function converts dictionary arguement into a list of key-value tuples.
def convertDictToTupleList(inputDict):
    outputList = []
    for elem in inputDict:
        outputList.append((elem, inputDict[elem]))
        # print elem, inputDict[elem]

    return outputList





# Testing section.

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print convertDictToTupleList(my_dict)
