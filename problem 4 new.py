#Raymundo Sanchez
#Nov 3, 2020
#this for nu range will tell it to make a list from 1 to 50
#the reason why it goes over 50 is because python starts at 0 so you would only get until 49
# because of this I had to start at 1 and end in 51 now you actually get the list to 50.
for num in range (1,51):
    #print(num)
    #this print wasn't needed any more since I put it at the bottom.
    #the divisible by both had to go in the beginning because you would then would get it if in the end
    # the main reason is because it sees the both version as a last resort if both divisible by 3 or 5 arent found
    # and the issue is that they are found so you would get the both option at all
    # also the print num was moved to the end since it was near the beginning so it wouldn't read the if statements.
    if num %3 ==0 and num %5 == 0:
        print ("Divisible by both")
    elif num %3 == 0:
        print ("Divisible by 3")
    elif num %5 ==0:
        print ("Divisible by 5")
    else:
        print (num)
    



