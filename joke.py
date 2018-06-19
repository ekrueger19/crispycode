import time as time
print "Knock knock."

if raw_input("> ") == "Who's there?":
    print "Interrupting cow."
    too = time.time() + 0.025
    while time.time() < too:
        print "> "
    if time.time() >= too:
        print "MOO!"
if raw_input("> ") == "No":
    print "YESSSSSSSSSS!!!!!"
else:
    print "You don't know how to do a knock-knock joke? How rude!"
