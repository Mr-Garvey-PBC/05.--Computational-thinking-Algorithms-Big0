mylist = [17,9,4,-12,3,39] 

# Move through the list the same number of times as there is elements in the list. (Not very efficent)
for i in range(len(mylist)):       

    for j in range(0, len(mylist)-i-1):
        # -i-1 limits the amount of values being compared during each iteration as the last elements are sorted
        # The -1 in particular stops an 'out of range' error as it stops python trying to compare the final element with a non existing element
        # The -i makes it so only the unsorted elements are sorted and the code doesnt run through the full list each time
        # First iteration 8-0-1=7, so only the first 6 elements are compared
        # Second iteration 8-1-1=6 so only the first 5 elements are compared
        
        if mylist[j] > mylist[j+1] :
            #print('if',mylist[j],'>',mylist[j+1])
            
            #mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            
            key=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]= key

print ("Sorted array :") 
print(mylist)



# Student work

# Put in print statements to follow the value of each variable during each iteration

