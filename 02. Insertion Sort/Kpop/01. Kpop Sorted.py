import csv

data_points=[]
with open('kpop_idols.csv','r',encoding='utf-8') as file: # May have to add encoding='utf-8'
    DataIn=csv.DictReader(file)
    
    for row in DataIn:
        if row['Full Name'] != '':
            data_points.append(row['Full Name'])   # 1  Data --> Full Name
        
#data_points_int=[int(item) for item in data_points]    # USe this line if you are sorting numbers and want to change data type from string to int  
    
for i in range(1, len(data_points)):          # A for loop that will loop through each of the items in our data list
    key=data_points[i]                        # Key is the variable that we are going to be checking and for the first loop will be [9]
    Compared_Against_Index_Number=i-1             # THis is the index position of the item we will be comparing our key value to.
                                                  # For the first loop through it will be 1-1=0, second loop 2-1=1 etc
    
  
    while Compared_Against_Index_Number>=0 and key<data_points[Compared_Against_Index_Number]: # Checking if our key value is less than the value it is being compared to
 
        data_points[Compared_Against_Index_Number+1]=data_points[Compared_Against_Index_Number]  # Add in this line
        
        Compared_Against_Index_Number-=1 # Add in this line 
        
    data_points[Compared_Against_Index_Number+1]=key  

print(data_points) # Output the sorted list
    