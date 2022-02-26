# Linear complexity
# O(n)
   
import matplotlib.pyplot as plt
import numpy as np

# Linear complexity 1
mylist=[1,2,3,4]

for item in mylist:
    print(item)  # imagine this print statement is an operation or calculation the program must do
                 # The bigger the list the more times this statement must print or if it was a calcualtion then it would mean more calculations the more numbers in the list
         
# Linear complexity 2
# Think of a linear eqution y=x+2, every x value has 2 added to it to get the corresponding y-value
# The more x-values the more calcualtaions must be done
x = [2, 4, 6, 8, 10, 12]

y = [4, 6, 8, 10, 12, 14]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()
