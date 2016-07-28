#first we assign tyoes of people to a string
x = "there are %d types of people." % 10
#now we define some more strings 
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y
#now we print the srtings we assigned earlier
print "I said: %r." % x 
print "I also said: '%s' ." %y 
#we define some more strings
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#here we have 
print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string with a right side"

print w + e
