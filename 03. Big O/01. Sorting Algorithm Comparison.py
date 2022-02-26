import csv
import timeit

data_points=[]
with open('kpop_idols.csv','r',encoding='utf-8') as file: 
    DataIn=csv.DictReader(file)
        
    for row in DataIn:
        if row['Full Name'] != '':
            data_points.append(row['Full Name'])


def insertion(data_points):
                            
    for i in range(1, len(data_points)):         
        key=data_points[i]                        
        Compared_Against_Index_Number=i-1            
                                                     
        while Compared_Against_Index_Number>=0 and key<data_points[Compared_Against_Index_Number]: 
             #data_points[Compared_Against_Index_Number],data_points[Compared_Against_Index_Number+1]=data_points[Compared_Against_Index_Number+1],data_points[Compared_Against_Index_Number]
             data_points[Compared_Against_Index_Number+1]=data_points[Compared_Against_Index_Number]  
            
             Compared_Against_Index_Number-=1 
            
        data_points[Compared_Against_Index_Number+1]=key  

    return (data_points) 



def selection(data_points):
                     
    for outerloopindex in range (len(data_points)):
        smallest_value_index=outerloopindex                                                                                                                  
        
        for innerloopindex in range(outerloopindex+1,len(data_points)):                          
            if data_points[smallest_value_index]>data_points[innerloopindex]:                                     
                smallest_value_index=innerloopindex                                                     
                         
        data_points[outerloopindex],data_points[smallest_value_index]=data_points[smallest_value_index],data_points[outerloopindex]     
                                                                        
    return(data_points)


def bubble(data_points):
   
    for i in range(len(data_points)):       

        for j in range(0, len(data_points)-i-1):   
            if data_points[j] > data_points[j+1] :
                data_points[j], data_points[j+1] = data_points[j+1], data_points[j]     
               
    return (data_points)


# Insertion sort
starttime = timeit.default_timer()
print("The start time for the insertion sort is :",starttime)
insertion(data_points)
print("The time difference is :", timeit.default_timer() - starttime,'\n')

# Selection sort
starttime = timeit.default_timer()
print("The start time for the selection sort is :",starttime)
selection(data_points)
print("The time difference is :", timeit.default_timer() - starttime,'\n')
 
# Bubble sort
starttime = timeit.default_timer()
print("The start time for the bubble sort is :",starttime)
bubble(data_points)
print("The time difference is :", timeit.default_timer() - starttime,'\n')
        
