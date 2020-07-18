for num in range (1,30):
    for i in range (3,num):
        if num%i==0:
            j=num/i
            print  ('%d equals %d * %d' % (num,i,j)) 
