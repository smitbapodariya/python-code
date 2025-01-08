a = int(input("Enter number:"))
sum = 0
for i in range(1,a+1):
    sum = sum + i**2
    print(i**2,end="+")
print("=",sum)