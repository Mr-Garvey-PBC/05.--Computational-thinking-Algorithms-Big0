# Number of operations carreid out determins our complexity
# Our functions want to add up the all the numbers between 0 and 5, but it could be any number for example.


# In this first function, we have a constant number of operations, the size of the input doesnt matter.
# We use the formula (x*(x+1)/2)  to get the total, x in this case is 5, so if we wanted to find the sum of the numbers between
# 0-100 we would just use 100 as x and it does not effect how long out function runs for.
def add_up_to_n_1(x):
    return (x*(x+1)/2)    # Just 1 operations no matter size of n, *,+,/
 
print(add_up_to_n_1(5))
 

# In this second function, we don't have a constant number of operations, the size of the input does matter.
# We use a for loop to add each number individually  to get the total, x in this case is 5, so the for loop will run 5 times, or you could think of it as we have 5 operations to run
# if we changed the input from 5 to 100 then the for loop would have to run 100 times using more memory and taking longer than function 1
def add_up_to_n_2(x):
    total=0                    # 1 assignments for =
    for i in range (1,x+1):
        total+=i               # n additions, n comparisons to make sure loop hasnt gone past x+1 iterations
    return(total)              # also have n amount if increments

print(add_up_to_n_2(5))        # As n increases then the number of operations are going to increase as well
  
