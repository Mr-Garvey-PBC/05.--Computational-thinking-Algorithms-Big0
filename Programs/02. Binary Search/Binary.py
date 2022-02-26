myList=[17,2,26,78,43,90,23,56,12]  # Hard coded list that is NOT sorted
myList.sort()                       # Using inbuilt Python abilities to sort list

print(myList)                       # Outputting sorted list
key=int(input("Enter key value to search for: "))      # Asking the user what value to search for
start=input("Start the search y/n: ")                  # Start the search

while start!='n':                    # Condition to start search based on user input
    first_index_value=0              # Setting a variable that will be used for calculating the midpoint (Will always be 0)
    last_index_value=(len(myList)-1) # Setting a variable that will be used for calcualting the midpoint (Will always be length of a list)

# **** Start of binary search algorithm*****

    while first_index_value<=last_index_value:              # Condition to start the binary search
        mid_point=(last_index_value+first_index_value)//2   # Midpoint calcualtion, //2 means there will be no remainder, e.g 9//4 = 2 , 5//3 =1
        if myList[mid_point]<key:                           # If the value stored at the index position of the midpoint is < than the search value
            first_index_value=mid_point+1                   # The new first_index_value becomes midpoint index position + 1, so all values before the midpoint are discarded
        elif myList[mid_point]>key:                         # If the value stored at the index position of the midpoint is > than the search value
            last_index_value=mid_point-1                    # The new last_index_value becomes midpoint index position - 1, so all values after the midpoint are discarded           
        else:
            print("Value is at position: ",mid_point)       # Midpoint value is the searched for value
            break                                           # End while loop
        
# ***** End of binary search algorithm ******

    start=input("Search again y/n: ")                       # Just put in so i wont have to restart the program each time i run it for the lads.
    key=int(input("Enter new key to search for")) 
