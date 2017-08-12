# This function prints the contents of a the passed dictionary.
def printDictionary(inputDictionary):
    print "My name is " + inputDictionary['name']
    print "My age is " + str(inputDictionary['age'])
    print "My country of birth is " + inputDictionary['birthplace']
    print "My favorite language is " + inputDictionary['favorite_language']




# Test area
studentInfoDictionary = {
    'name'              : "Nick Pettyjohn",
    'age'               : 30,
    'birthplace'        : "USA",
    'favorite_language' : "Python",
}

printDictionary(studentInfoDictionary)
