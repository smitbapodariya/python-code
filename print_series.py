a = int(input("Enter number:"))
sum = 0
for i in range(1,a+1):
    sum = sum + i
    print(i,end="+")
print("=",sum)