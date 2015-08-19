with open('small.txt','r') as f:
	lines=f.readlines()
	i=1
	with open('small1.txt','w') as fin:
		for line in lines:
 			fin.write(str(i) + ' ' + line) 
			i+=1