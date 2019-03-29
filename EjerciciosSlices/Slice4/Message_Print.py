def age_msg(age):
    if (age == None or age < 0): print "Error, invalid age"
    if (age <= 12): print "You are child"
    if (age > 12 and age <= 17): print "Your are teenager"
    if (age > 17 and age <= 29): print "You are young"
    if (age > 29): print "You are adult"