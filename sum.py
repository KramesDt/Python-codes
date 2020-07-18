def multi():
    for i in range (2,6,2):
        for j in range (1,11,2):
            print ("%d * %d = %d" % (i,j,(i*j)))
            if j == 9:
                break
print (multi())
