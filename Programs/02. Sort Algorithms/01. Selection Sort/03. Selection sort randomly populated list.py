# Selection sort is an algorithm that sorts a list by selecting the smallest element from an unsorted list
# in each iteration and places that element at the beginning of the unsorted list. Your list ends up sorted
# from smallest to largest or vice versa depending on what you want.

import random                   # Code for randomly generating a list of user specified numbers
myList=[]
user=int(input("How many random numbers do you want to generate: "))

for counter in range(user):
    myList.append(random.randint(-100,100))
print(myList)


# Two FOR loops, one loop (inner) is looping one index position in front of the outer loop which allows
# two values be compared to find the smaller/larger element.

for outerloopindex in range (len(myList)):
    
    smallest_value_index=outerloopindex                                                             # Setting the first index position as the minimum value, if you print(smallest) you get 0,  its only the index position not the element at that position
    print("\nThe outer loop value and smallest value we start with is: ",myList[outerloopindex])
    print(myList)                                                                                       # Initial FOR loop is always one index position behind the inner FOR loop
    
    for innerloopindex in range(outerloopindex+1,len(myList)):                          # Inner FOR loop that starts at index position (from outer FOR loop)+1
        print("Inner loop value: ",myList[innerloopindex])

        if myList[smallest_value_index]>myList[innerloopindex]:                                     # Comparing the value at index position[smalles] (from outer loop) and value at index postion[i], which is the next value in the list
            print("Is",myList[smallest_value_index]," > than",myList[innerloopindex])
            smallest_value_index=innerloopindex                                                     # If the inner FOR loop value is smaller than the outer loop value, assign the inner loop as the smaller value
            print("The smallest value is now: ",myList[smallest_value_index])
            
    myList[outerloopindex],myList[smallest_value_index]=myList[smallest_value_index],myList[outerloopindex]     # Swapping postions
    
print(myList)                                                                           # Output sorted list
                
# Pseudo
# Input list
# Assign first value as the smallest value
# Compare smallest value with the next item in the list
# if the next item is smaller make that the smallest item
# Compare each element in the list to find the smallest item
# place the smallest item as the first item in the list
# Set the second item in the list as the smallest and repeat

