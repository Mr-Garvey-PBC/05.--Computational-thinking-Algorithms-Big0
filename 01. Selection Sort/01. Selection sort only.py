#myList=[107,24,-3,5,85,32,-99,50]
myList=[10,9,8,7,6,5,4,3,2,1,0]
print('Original List',myList,'\n')
count=0
# Selection sort algorithm start
for outerloopindex in range (len(myList)):
    
    current_min = outerloopindex
    count+=1
    for innerloopindex in range(outerloopindex+1,len(myList)):                          
        count+=1
        if myList[current_min] > myList[innerloopindex]:                                     
            current_min=innerloopindex                                                     
                
            
    myList[outerloopindex],myList[current_min]=myList[current_min],myList[outerloopindex]
# Selection sort algorithm end
    print('List after each sort',myList)

    
print(myList)                                                                          
print(count)                
# Pseudo
# Input list
# Assign first index position value as the smallest value  (set mylist[0] as current min)
# Compare smallest value with the next item in the list    (Compare mylist[0] with mylist[1])
# if the next item is smaller make that the smallest item  (if mylist[1]<mylist[0], mlist[1] becomes the new current min)
# Compare each element in the list to find the smallest item
# Assign a new value as the smallest value if neccessary
# Place the smallest item as the first item in the list    (replace mylist[0] with mylist[current min])
# Set the second item in the list as the smallest and repeat


