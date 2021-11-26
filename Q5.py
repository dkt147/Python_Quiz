def fizz_buzz(n):
    if n%3==0 and n%5!=0:
        print("Fizz")
    if n%5==0 and n%3!=0:
        print("Buzz")
    if n%3==0 and n%5==0:
        print("Fizz Buzz")
    if n%3!=0 or n%5!=0:
        print(n)

number = int(input("Enter Your number: "))
fizz_buzz(number)