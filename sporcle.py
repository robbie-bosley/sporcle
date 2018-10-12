import os

print "You are entering a score from a sporcle quiz!"
inpscore = input("What was your raw score?\n")
score = float(inpscore)
inpmaximum = input("What was the maximum score?\n")
maximum = float(inpmaximum)
print "score is", score, ",  maximum is", maximum, "and their sum is", score+maximum, "and their ratio is ", score/maximum
percentage = (score/maximum)*100
inpaverage = input("What was the average percentage?\n")
average = int(inpaverage)
difference = percentage - average
category = raw_input("What was the category?\n")
players = raw_input("How many of you played the quiz?\n")
day = raw_input("What day is it (number form, where day 79 is 11/10/2018)\n")
winnipeg = raw_input("Winnipeg? [y/n]\n")


print "Ok, so on day", day, ",", players, "of you played a", category, "quiz, and you got", score, "/", maximum, "=", percentage, "% while the average was", average, "%? And winnipeg is a ", winnipeg, "?"

goodlist = ["That right there was the work of a superior intellect."]
averagelist = ["You get an A for ... Average."]

print "That's a difference of", difference, "!"
if (difference < 0):
    print "That's pants!"
elif (difference > 10):
    print "That's dead good, that!"
else:
    print "That's not bad at all."

with open('sporcle.sh', 'w') as fout:
    fout.write("#!/bin/bash\n")
    fout.write("echo "+str(score)+" "+str(maximum)+" "+str(percentage)+" "+str(average)+" "+str(difference)+" "+category+" "+day+" "+players+" "+winnipeg+" >> sporcle.txt\n")
    fout.write("echo Score stored to sporcle.txt")

os.system("chmod 755 sporcle.sh")

submit = raw_input("Are the details above correct?[y/n]\n")
if (submit == "y"):
    os.system("./sporcle.sh")
else:
    print "You can store the score still by sourcing sporcle.sh"

