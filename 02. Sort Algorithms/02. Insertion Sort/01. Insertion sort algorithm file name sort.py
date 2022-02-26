import csv

data_points=[]
with open('Names sort.csv','r') as file:
    DataIn=csv.DictReader(file)
    
    for row in DataIn:
        data_points.append(row['Names'])
           
    
for i in range(1, len(data_points)):          # A for loop that will loop through each of the items in our data list
    key=data_points[i]                        # Key is the variable that we are going to be checking and for the first loop will be [9]
    Compared_Against_Index_Number=i-1             # THis is the index position of the item we will be comparing our key value to.
                                                  # For the first loop through it will be 1-1=0, second loop 2-1=1 etc
     
    while Compared_Against_Index_Number>=0 and key<data_points[Compared_Against_Index_Number]: # Checking if our key value is less than the value it is being compared to
 
        data_points[Compared_Against_Index_Number+1]=data_points[Compared_Against_Index_Number]
        
        Compared_Against_Index_Number-=1  
        
    data_points[Compared_Against_Index_Number+1]=key  

print(data_points) # Output the sorted list
    