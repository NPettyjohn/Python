# This function takes a list of strings and a substring parameter and returns
# new list that only contains list items containing the supplied substring.

def filterListBySubstring(input_list, filter_string):
    outputList = []
    for elem in input_list:
        # print elem
        # print elem.find(filter_string)
        if elem.find(filter_string) != -1:
            outputList.append(elem)
    return outputList



# Testing the filterListBySubstring() function.

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

print filterListBySubstring(word_list, char)
