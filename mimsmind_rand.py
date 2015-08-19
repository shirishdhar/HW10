import sys
import random

def get_randomdigit_lastname1lastname2(length):
    l2=10**length
    x=random.randint(0,l2-1)
    print str(x).zfill(length)




def main():
    try:
        length=int(sys.argv[1])
    except:
        get_randomdigit_lastname1lastname2(3)
    else:
        get_randomdigit_lastname1lastname2(length)
main()
