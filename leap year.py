#Leap year calculator
def leap_year(year):
    if int(year)%4==0:
        print ("Leap year")
    else:
        print ("Not a leap year")
            

year=input("Enter year: ")
leap_year(year)
