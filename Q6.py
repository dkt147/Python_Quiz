
def myfunc(n):
    sum = 0
    list = []
    for j in range(n):
        list.append(j)
    for i in range(len(list)):
        if list[i]%3==0 and list[i]%5==0:
            sum = sum + list[i]
    print(sum)

number = int(input("Enter Your range: "))
myfunc(number)