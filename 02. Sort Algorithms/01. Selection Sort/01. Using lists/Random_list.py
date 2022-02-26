import random

mylist=[]
user_amount=int(input("How many values in the list would you like: "))

for i in range (user_amount):
    x=random.randint(1,10)
    mylist.append(x)
    
print(mylist)