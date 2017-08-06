



def listToDict(inputList1, inputList2):
    newDict = {}
    list1 = []
    list2 = []
    minListIndex = 0

    if len(inputList1) >= len(inputList2):
        list1 = inputList1
        list2 = inputList2
        minListIndex = len(inputList2)
    else:
        list1 = inputList2
        list2 = inputList1
        minListIndex = len(inputList1)


    for counter in range(0, minListIndex):
        # print inputList1[counter], inputList2[counter]
        newDict[list1[counter]] = list2[counter]
    return newDict




# Test section.
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print listToDict(name, favorite_animal)
