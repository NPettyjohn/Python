
# Fun with strings.
words = "It's thanksgiving day. It's my birthday, too!"
# print words
print "The position of the first instance of 'day' is: " + str(words.find("day"))
words = words.replace(" day", " month")
print words

#Min and max examples.
x = [2,54,-2,7,12,98]
# print x
print min(x)
print max(x)

# First and last examples.
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
x = [x[0],x[len(x)-1]]
print x

# New list exaples.
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y=x[len(x)/2:]
x = [x[:len(x)/2]]
x.extend(y)
print x
