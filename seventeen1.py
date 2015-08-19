import sys



def random_generator():
	import random
	ran=random.randint(1,3)
	return ran 




def seventeen():
	marbles=17
	while True:
		try: 
			user_in=int(raw_input('Your turn: How many marbles will you remove (1-3)? '))
			if (user_in not in range(1,4)) or (marbles-user_in<0):							# 1/0 used to cause an exception if conditions are met.
				1/0
		except:
			print 'Sorry, that is not a valid option. Try again! '
			continue

		else:
			print 'You removed {this} marbles'.format(this=user_in)
			marbles-=user_in
			if marbles!=0:
				print 'Number of marbles left in jar: {that}'.format(that=marbles)
			else: 
				sys.exit('There are no marbles left. User wins')
			print "Computer's turn..."
			comp_in=random_generator()
			print 'Computer removed {them} marbles.'.format(them=comp_in)
			marbles-=comp_in
			if marbles!=0:
				print 'Number of marbles left in jar: {thats}'.format(thats=marbles)
			else:
				sys.exit('There are no marbles left. Computer wins!')
			continue





def main():
	print "Let's play the game of seventeen1"
	print 'Number of marbles left in jar: 17'
	seventeen()
main()
			