
myList=[107,24,-3,5,85,32,-99,50] # Hard coded list that must be sorted

count=1  # Count vriable to count how many sorts are carried out

# Start of sort algorithm 
for outerloopindex in range (len(myList)):                      # Outer For loop, runs from 0 -> length of the list
    current_min=outerloopindex                                  # Assign the current min index position as the Outer For Loop counter value.
                                                                # First time the loop runs outerloopindex=0
    print("\nList at the start of loop",count,"is",myList,"\n") # Output the unsorted list to the user
    print("\nThe value assigned as the current min for loop",count,"is:",myList[current_min])
                                                                                                      
    # The inner loop is one element ahead of the outside for loop, this allows the two elements to be compared.   
    for innerloopindex in range(outerloopindex+1,len(myList)):           # Inner FOR loop, runs from 1 -> length of the list
        print("Inner loop value being compared to the current min value: ",myList[innerloopindex],"\n")
        
        if myList[current_min]>myList[innerloopindex]:           # Comparing the current minimum value with the item next in the lsit
            print("The IF statement is making the comparison, Is",myList[current_min]," > than",myList[innerloopindex])
            current_min=innerloopindex                           # If the element at mylist[innerloopindex] is smaller than the current minimum, then it becomes the new current min value
            print("The new current min is:",myList[current_min],"\n")
            
    myList[outerloopindex],myList[current_min]=myList[current_min],myList[outerloopindex]     # Swapping postions
    print('List after',count,'runs',myList)    # Outputing the list after each iteration
    count+=1                                   # Increase the loop counter value
    input()                                    # Waiting for an input from user to continue the sorting.
    
print('sorted list',myList)                                                                           # Output sorted list
                
# Pseudo
# Input list
# Assign first value as the smallest value
# Compare smallest value with the next item in the list
# if the next item is smaller make that the smallest item
# Compare each element in the list to find the smallest item
# place the smallest item as the first item in the list
# Set the second item in the list as the smallest and repeat

