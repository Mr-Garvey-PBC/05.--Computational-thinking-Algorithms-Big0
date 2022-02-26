# Binary search algorithm - working
myList=[3,7,13,18,28,35,41,50]
myList.sort()                                                        # Using inbuilt Python abilities to sort list
    
print("List sorted: ",myList)                                                           # Outputting sorted list
key=int(input("Enter key value to search for: "))                            # Asking the user what value to search for
FOUND=False                                                      
    
while FOUND==False:                                              
    first_index_value=0
    last_index_value=(len(myList)-1)                                

# **** Start of binary search algorithm*****

    while first_index_value<=last_index_value:              # Condition to start the binary search
        mid_point=(last_index_value+first_index_value)//2   # Midpoint calcualtion, //2 means there will be no remainder, e.g 9//4 = 2 , 5//3 =1
        print(mid_point)
        if myList[mid_point]<key:                           # If the value stored at the index position of the midpoint is < than the search value
            first_index_value=mid_point+1                   # The new first_index_value becomes midpoint index position + 1, so all values before the midpoint are discarded
        elif myList[mid_point]>key:                         # If the value stored at the index position of the midpoint is > than the search value
            last_index_value=mid_point-1                    # The new last_index_value becomes midpoint index position - 1, so all values after the midpoint are discarded           
        elif myList[mid_point]==key:
            print("Value is at position: ",mid_point)       # Midpoint value is the searched for value
            FOUND==True
            break
    else:
        print("Item not found")
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
# End WHile






 
