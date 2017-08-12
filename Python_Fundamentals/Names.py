# Create string to print students list in the correct format.
def printStudentNames(inputList):
    outputString = ""
    for elem in inputList:
        outputString += elem['first_name'] + " " + elem['last_name'] + "\n"
    return outputString

# Create string to print users dictionary in the correct format.
def printUsersDictionary(inputDictionary):
    outputString = ""
    for dictElem in inputDictionary:
        # print dictElem
        outputString += dictElem + "\n"
        counter = 0
        for listElem in inputDictionary[dictElem]:
            # print listElem
            counter += 1
            outputString += str(counter) + " - " + listElem['first_name'] + " " + listElem['last_name'] + " - " + str(len(listElem['first_name'])+len(listElem['last_name'])) +  "\n"
    return outputString



# Test area.
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print printStudentNames(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
print printUsersDictionary(users)
