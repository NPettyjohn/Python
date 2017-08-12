# This function compares two lists and returns True if all elements match,
# otherwise it returns False.
def listsMatch(list_one, list_two):
    resultMessage = "These lists are the same."

    # Check to see if lists are same length.
    if len(list_one) != len(list_two):
        resultMessage = "These lists are not the same because one list has more items."
        return resultMessage

    for idx in range(0, len(list_one)):
        if list_one[idx] == list_two[idx]:
            pass
        else:
            resultMessage = "These lists are not the same."

    return resultMessage



# Testing listMatch function.
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

print listsMatch(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

print listsMatch(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

print listsMatch(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

print listsMatch(list_one, list_two)
