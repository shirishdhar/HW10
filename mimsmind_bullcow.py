def get_bullcow(guess, rand_num):
     for i in range(len(rand_num)):
            if guess[i]==rand_num[i]:
                bull_count1+=1 
                b=list(rand_num)           #Replaces the bull letter with 'a'(can be anything) 
                b[i]='a'
                c=''.join(b)
                rand_num=c

        for i in range(len(rand_num)):
            if (guess[i] in rand_num):
                cow_count1+=1
                index=rand_num.index(guess[i])
                b=list(rand_num)           #Replaces the cow letter with 'b'(can be anything) 
                b[index]='b'
                c=''.join(b)
                rand_num=c
                