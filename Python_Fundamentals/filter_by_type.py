# This function will take a given variable and return the type.
def variableType(inputVariable):

    returnVal = "Type not found!"

    if isinstance(inputVariable, int):
        if inputVariable >=100:
            returnVal = "That's a big number!"
        else:
            returnVal = "That's a small number!"
    elif isinstance(inputVariable, str):
        if len(inputVariable) >= 50:
            #print len(inputVariable)
            returnVal = "Long sentence."
        else:
            #print len(inputVariable)
            returnVal = "Short sentence."
    elif isinstance(inputVariable, list):
         if len(inputVariable) >= 10:
             print len(inputVariable)
             returnVal = "Big list."
         else:
             print len(inputVariable)
             returnVal = "Short list."

    return returnVal




# Testing the function.
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


testVariableList = [sI,mI,bI,eI,spI,sS,mS,bS,eS,aL,mL,lL,eL,spL]

for testVal in testVariableList:
    print variableType(testVal)
