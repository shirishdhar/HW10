import sys

def random_generator():
	import random
	ran=random.randint(1,3)
	return ran 

def seventeen():
	with open('sample1.txt','a') as fin:
		with open('sample.txt','r') as f:
			lines=f.readlines()
			p1count=0
			p2count=0
			game_no=0
			for line in lines:
				sequence=[]
				count=17
				line1=line.strip().split(',')
				for item in line1:
					sequence.append(item)          #Appending each input of sequence
					a=int(item)
					count-=a
					if count<=0:					#If P1 has last input, P2 wins
						winner='P2'
						break
					rand=random_generator()			#Generating random input for P2
					count-=rand
					sequence.append(str(rand))
					if count<=0:					#If P2 has last input, P1 wins
						winner='P1'
						break
					continue

				if winner=='P1':
					game_no+=1
					fin.write('Game #' + str(game_no) + '. Play sequence: ' + '-'.join(sequence) +'.'+ ' Winner: P1\n')
					p1count+=1						#Increment wins of P1
				elif winner=='P2':
					game_no+=1	
					fin.write('Game #' + str(game_no) + '. Play sequence: ' + '-'.join(sequence) + '.' + ' Winner: P2\n')
					p2count+=1 						#Increment wins of P2
				continue
			fin.write('Player 1 won {this} times; Player 2 won {that} times.'.format(this=p1count,that=p2count))


def main():
	seventeen()
main()
			