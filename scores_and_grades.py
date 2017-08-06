# Function generates ten scores between 60 and 100. Each time a score is
# generated, function displays what the grade is for a particular score.
def generateRandomScores():
    import random
    print "Scores and Grades"
    for counter in range(0, 10):
        randomScore = random.randint(60, 100)
        if randomScore < 70:
            grade = "D"
        elif randomScore >= 70 and randomScore < 80:
            grade = "C"
        elif randomScore >= 80 and randomScore < 90:
            grade = "B"
        elif randomScore >= 90:
            grade = "A"
        print "Score: " + str(randomScore) + "; Your grade is " + grade
    print "End of program. Bye!"

# Function test section.

generateRandomScores()
