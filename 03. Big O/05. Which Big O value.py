#Pseudocode for algorithm with all three complexities.

if condition_is_met == 'quadratic':
    for outerloop in range len(list):
        for innerloop in range len(list):
            sum=sum+innerloop
            
elif condition_is_met == 'linear':
    for counter in range len(list):
        sum=sum+counter

elif condition_is_met== 'constant':
    sum=(number*(number+1)/2)