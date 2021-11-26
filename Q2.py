# List with different starting and ending point
#list = [89,45,2,3,45,20,70,2,50,20,29]

# List with same starting and ending point
list = [29,45,2,3,45,20,70,2,50,20,29]

first = list[0]

# checking list value using loop
for i in range(len(list)):
    # storing last value at the end of iteration
    last = list[i]


# Checking both variables containing first and last value
if first==last:
    print("First and Last number is same!")
else:
    print("First and Last number is not same!")