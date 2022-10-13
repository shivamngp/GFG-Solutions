num=int(input("enter an integer"))
i=2
while i <= num - 1:
    if num%i==0:
        print(num,'is not a prime number')
        break
    i += 1
else :
    15print(num,'is a prime number')