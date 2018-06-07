y = 0
x = raw_input("> ")
print "Hello. Will you help me? Answer y/n"
if x == "y":
    print "Thank you. I am a genie and can tell your future."
    print "Do you want to know your future? Answer y/n"
    if x == "y":
        print "You will die in approximately thirty seconds."
    elif x == "n":
        print "Good choice. You may leave."
    else:
        print "You have made a mistake with your answer. Please retry."
elif x == "n":
    print "Dude. You are literally so rude. Omg."
else:
    print "You made a mistake somewhere along the line. Try again."
