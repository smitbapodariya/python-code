a = int(input("Enter number:"))
sum = 0
for i in range(1,a+1):
    sum = sum + i
    if i%2==0:
        print(i**2,end="+")
    else:
        print(i**2,end="-")
print("=",sum)