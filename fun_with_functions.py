# Function will loop through the numbers between 1 and 2000 and tell you whether
# the current number is odd or even.
def oddOrEven():
    for counter in range(1,2001):
        if counter % 2 != 0:
            print "Number is " + str(counter) + ". This is an odd number."
        else:
            print "Number is " + str(counter) + ". This is an even number."

# This function will take a list of numbers and multiply each by another number
# passed as the second parameter.
def listMultiplier(list_to_multiply, number_to_multiply_by):
    outputList = []
    for val in list_to_multiply:
        outputList.append(val * number_to_multiply_by)
    return outputList

# Hacker challenge function. Creates a list of lists containing '1' printed the
# number of times specified item the input list.
def layeredMultiples(inputList):
    outputList = []
    subList = []
    for val in inputList:
        for counter in range(0,val):
            subList.append(1)
        outputList.append(subList)
        subList = []
    return outputList




# Function test area.
oddOrEven()

a = [2,4,10,16]
print listMultiplier(a, 5)

print layeredMultiples(listMultiplier([2,4,5],3))
