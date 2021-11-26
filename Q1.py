# Taking string as an input
string = input("Enter Your string: ")

# Searching in a string using loop
for i in range(len(string)):

    # Checking if index is even
    if i%2==0:
        # Printing even values with respect to index
        print(string[i])