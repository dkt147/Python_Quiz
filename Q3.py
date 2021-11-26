# Creating and Initializing List_1
list_1 = [1,2,3,4,5,6,7,8,9,10]

# Creating and Initializing List_2 with different values
list_2 = [11,12,13,14,15,16,17,18,19,20]

# Creating New List
new_list = []

# Searching List_1 values
for i in range(len(list_1)):
    # Checking if value is odd
    if list_1[i]%2!=0:
        # Append value of List_1 to New_List
        new_list.append(list_1[i])


# Searching List_2 values
for i in range(len(list_2)):
    # Checking if value is even
    if list_2[i]%2==0:
        # Append value of List_2 to New_List
        new_list.append(list_2[i])

# Printing List_1
print("List 1: ",list_1)

# Printing List_2
print("List 2: ",list_2)

print(" ")

# Printing New_List containing both odd values from List_1 and even values from List_2
print("New List: ",new_list)