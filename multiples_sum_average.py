
# Multiples example.

# Print odd numbers 1 to 1000.
for i in range(1,1000):
    if i % 2 != 0:
        print i

# Print multiples of 5 from 5 to 1,000,000.
for i in range(5,1000000):
    if i % 5 == 0:
        print i

# Sum list example.
a = [1, 2, 5, 10, 255, 3]
for i in a:
    print i

# Average list example.
print sum(a)/float(len(a))
