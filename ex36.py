#the bedroom
def bed_room():
	print "You are in the Bedroom"
	print "You can either look out the Window ,go to the Bathroom"
	print "or go back to the Hall"
	print "What will you do?"
	
	choice = raw_input("> ")
	
	if choice == "window":
		print "Some trees, and a wall is visible"
		print " "
		bed_room()
	elif choice == "bathroom":
		bath_room()
	elif choice == "hall":
		print " "
		start()
	else:
		print "Just going to stand around then?"
		print " "
		bed_room()
#the bathroom
def bath_room():
	print "You are in the Bathroom!"
	print "you can take a Bath, Brush your teeth, Drink from the toilet"
	print "or go back to the Bedroom"
	print "what will you do?"
	
	choice = raw_input("> ")
	
	if choice == "bath":
		print "You took a bath!"
		print " "
		bath_room()
	elif choice == "brush":
		print "You brushed your teeth!"
		print " "
		bath_room()
	elif choice == "drink":
		print "EWW! ARE YOU OK? I MEAN COME ON MAN?"
		print " "
		bath_room()
	elif choice == "bedroom":
		print " "
		bed_room()
	else:
		print "Just going to stand around then?"
		print " "
		bath_room()
#the dinning room
def dinning_room():
	print "You are in the Dinning room!"
	print "You can either go to the Kitchen or look at the Paintings"
	print "Or go back to the Hall"
	print "What will you do?"
	
	choice = raw_input("> ")
	
	if choice == "kitchen":
		print " "
		kitchen()
	elif choice == "paintings":
		print "Some weird modern art is hanging on the walls"
		print " "
		dinning_room()
	elif choice == "hall":
		print " "
		start()
	else:
		print "Just going to stand around then"
		print " "
		dinning_room()
#the kitchen 
def kitchen():
	print "You are in the kitchen!"
	print "You can cook a Meal, Get some Snacks, make Coffee"
	print "Or go back to the Dinning room"
	print "What will you do?"
	
	choice = raw_input("> ")
	
	if choice == "meal":
		print "You tried cooking a meal but you burnt it!"
		print "Nice job" 
		print " "
		kitchen()
	elif choice == "snacks":
		print "You got some snacks from the fridge and ate them!"
		print " "
		kitchen()
	elif choice == "coffee":
		print "You made some Coffee and drunk it!"
		print " "
		kitchen()
	elif choice == "dinning":
		print " "
		dinning_room()
	else:
		print "Just going to stand around then?"
		print " "
		kitchen()
#the game room
def game_room():
	print "You are in the Game room!"
	print "You can play Snooker, Darts, Air Hockey or go the Gym"
	print "Or go back to the Hall"
	print "What will you do?"
	
	choice = raw_input("> ")
	
	if choice == "snooker":
		print "Going to play alone are we?"
		print " "
		game_room()
	elif choice == "darts":
		print "Going to play alone are we?"
		print " "
		game_room()
	elif choice == "hockey":
		print "Going to play alone are we?"
		print " "
		game_room()
	elif choice == "gym":
		print " "
		gym()
	elif choice == "hall":
		print " "
		start()
	else:
		print "Just going to stand around then?"
		print " "
		game_room()
#the gym
def gym():
	print "You are in the Gym!"
	print "You can go on the Treadmill, Training bike ot lift some Weights"
	print "Or go back to the game room"
	print "What will you do?"
	
	choice = raw_input("> ")
	
	if choice == "treadmill":
		print "You were only able to do 2 Km before getting exausted!"
		print " "
		gym()
	elif choice == "bike":
		print "You were able to 10 KM on the bike!"
		print "Good job!"
		print " "
		gym()
	elif choice == "weights":
		print "You were only able to lift 5 Kg!"
		print "Wow you are good at this!"
		print " "
		gym()
	elif choice == "game":
		print " "
		game_room()
	else:
		print "Just going to stand around then?"
		gym()
#the starting point which is the hall in this case
def start():
	print "You are in a Hall"
	print "There are 4 doors leading out of the room"
	print "Which one will you take?"
	
	choice = raw_input("> ")
	
	if choice == "1":
		bed_room()
	elif choice == "2":
		dinning_room()
	elif choice == "3":
		game_room()
	elif choice == "4":
		print "Hey you cant go outside alone!"
		print "It's too dangerous!"
		print " "
		start()
	else:
		print "Just going to stand around then?"
		start()
start()
