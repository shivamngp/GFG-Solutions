a = int(input("enter the first angle : "))
b = int(input("enter the second angle : "))
c = int(input("enter the third angle : "))
if a==b==c:
    print("triangle is a equlateral triangle")
elif a==b or b==c or a==c:
    print("triangle is a ISoscelence triangle")
elif a==90 or b==90 or c==90:
    print("triangle is a right angled triangle")
elif a!=b!=c:
    print("triangle is a scelence triangle")
else:
    ("unable to find type of triangle")