def len_(list_):
	return sum(1 for item in list_)

def main():
	print len_(((1,2),(1,4)))
	print len_('abcd')
	print len_({'a':3,'b':2})
main()