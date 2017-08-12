# Function simulates tossing a coin 5,000 times and prints how many times
# the head/tail appears.
def coinTossSimulation(numberOfIterations):
    import random
    print "Starting the program..."
    headsTotal = 0
    tailsTotal = 0
    for counter in range(1,numberOfIterations +1 ):
        randNum = random.randint(0, 1)
        if randNum == 0:
            flipResult = "Head"
            headsTotal += 1
            print ("Attempt #" + str(counter) + ": Throwing a coin... It's a "
                    + flipResult + "! ... Got " + str(headsTotal) + " head(s) so far and "
                    + str(tailsTotal) + " tail(s) so far.")
        else:
            flipResult = "Tail"
            tailsTotal += 1
            print ("Attempt #" + str(counter) + ": Throwing a coin... It's a "
                    + flipResult + "! ... Got " + str(headsTotal) + " head(s) so far and "
                    + str(tailsTotal) + " tail(s) so far.")

    print "Ending the program, thank you!"


# Test the function.
coinTossSimulation(100000)
