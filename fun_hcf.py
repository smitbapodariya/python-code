def hcf(n1,n2):
    smaller = 0
    if n1 < n2:
        smaller = n1
    else:
        smaller = n2

    for i in range(1,smaller+1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i
        return hcf

num1 = 54
num2 = 72

print("hcf of ",num1,"and",num2,"is==>",hcf(num1,num2))