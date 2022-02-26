myList=['A','C','E','D','B','F','H','G','I']                        # Hard coded list that is NOT sorted
myList.sort()                                                       # Using inbuilt Python abilities to sort list
    
print(myList)                                                       # Outputting sorted list
key=input("Enter key value to search for: ")                        # Asking the user what value to search for (CASE SENSITIVE)
FOUND=False                                                      
    
while FOUND==False:                                                 # A variable used as a condition to end the WHile loop                                             
    first_index_value=0                                             # Declaring the first index value of the list
    last_index_value=(len(myList)-1)                                # Declaring the last index value of the list (STARTS AT 0 so thats why it is length of the list-1)                              

# **** Start of binary search algorithm*****

    while first_index_value<=last_index_value:              # Condition to start the binary search
        mid_point=(last_index_value+first_index_value)//2   # Midpoint calcualtion, //2 means there will be no remainder, e.g 9//4 = 2 , 5//3 =1
        print("Mid_point value is:",mid_point)              # Displaying what the mid point value is each time the loop runs
        if myList[mid_point]<key:                           # If the value stored at the index position of the midpoint is < than the key
            first_index_value=mid_point+1                   # The new first_index_value becomes midpoint index position + 1, so all values before the midpoint are discarded
        elif myList[mid_point]>key:                         # If the value stored at the index position of the midpoint is > than the key
            last_index_value=mid_point-1                    # The new last_index_value becomes midpoint index position - 1, so all values after the midpoint are discarded           
        elif myList[mid_point]==key:
            print("Value is at position: ",mid_point)       # Midpoint value is the key
            FOUND==True                                     # Changes the variable FOUND to end the outer loop
            break                                           # Ending the inner loop
    else:
        print("Item not found")                             # Else condition to tell the user the item was not found in the list.
    break
    
# ***** End of binary search algorithm ******


# Pseudocode
# Declare List
# Declare variable 'found'
# Sort the list if it is not sorted
# Input key value
# While loop
#     Declare first and last index position of list
#     While loop
#         Calculate the midpoint (first_index+last_index)/2
#         Compare midpoint element with key
#         If midpoint < key
#             New first index position becomes Midpoint+1
#         Elif midpoint > key
#             New first index position becomes Midpoint-1
#         Elif midpoint == key
#             Tell user index position
#             change found variable to True
#     End WHile
# End While





 
