import csv
import statistics
from matplotlib import pyplot as plt

ratings=[]
ratings_int=[]
ones=[]
twos=[]
threes=[]
fours=[]
fives=[]
hotel_stars=['1 star','2 star','3 star','4 star','5 star']

# Openong the file and adding desired value to the list
with open('tripadvisor.csv','r') as file:
    dataIn=csv.DictReader(file)

    for row in dataIn:
       ratings.append(row['Rating'])

# Pre processing the data
ratings_int=[int(item) for item in ratings]

# Insertion sort to sort data in list 
for i in range(1,len(ratings_int)):
    key=ratings_int[i]                                         
    j=i-1   
    
    while j>=0 and key<ratings_int[j]: 
        ratings_int[j+1]=ratings_int[j]                                 
        j-=1
        
    ratings_int[j+1]=key            

# Post processing
# Iterating through the processed list to append star ratings to appropriate list   
for i in range(0,len(ratings_int)):
    if ratings_int[i]==1:
        ones.append(ratings_int)
    elif ratings_int[i]==2:
        twos.append(ratings_int)
    elif ratings_int[i]==3:
        threes.append(ratings_int)
    elif ratings_int[i]==4:
        fours.append(ratings_int)
    else:
        fives.append(ratings_int)
        
stars_count=[len(ones),len(twos),len(threes),len(fours),len(fives)]
print('The mode is',statistics.mode(ratings_int))
print('The mode is',statistics.mean(ratings_int))
print('The mode is',statistics.median(ratings_int))


# Graphing the information
plt.bar(hotel_stars,stars_count)
plt.title('Star ratings according to Trip Advisor')
plt.xlabel('Star Rating')
plt.ylabel('Amount of stars')
plt.axis(xmin=0,xmax=10,ymin=0,ymax=10000)
plt.show() 
