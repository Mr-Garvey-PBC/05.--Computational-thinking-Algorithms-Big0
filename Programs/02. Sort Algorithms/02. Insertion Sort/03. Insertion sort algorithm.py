import csv

data_points=[]

with open('Sort 1.csv','r') as file:
    DataIn=csv.DictReader(file)
    
    for row in DataIn:
        data_points.append(row['Data'])

data_points_int=[int(item) for item in data_points]

# Insertion algorithm

for i in range(1, len(data_points_int)):          # A for loop that will loop through each of the items in our data list
    key=data_points_int[i]
    print(key)# Key is the variable that we are going to be checking and for the first loop will be [9]
    Compared_Element_Index_Number=i-1    # THis is the index position of the item we will be comparing our key value to.
    print('c',Compared_Element_Index_Number)
    
    while Compared_Element_Index_Number>=0 and key<data_points_int[Compared_Element_Index_Number]: # Checking if our key value is less than the value it is being compared to
        
        data_points_int[Compared_Element_Index_Number+1]=data_points_int[Compared_Element_Index_Number]

        Compared_Element_Index_Number-=1  # We change index position again so we can compare the key value to another element.
    data_points_int[Compared_Element_Index_Number+1]=key # Once we have moved key value to its correct place we assign it tp the correct position.
    
print('Final sorted List',data_points_int) # Output the sorted list
