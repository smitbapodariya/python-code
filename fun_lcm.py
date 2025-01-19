def lcm(n1,n2):
    greater = 0
    if n1 > n2:
        greater = n1
    else:
        greater = n2

    while(True):
        if greater % n1 == 0 and greater % n2 == 0:
            lcm = greater
            break
        greater += 1
    return lcm


num1 = 12
num2 = 50
print("the LCM of",num1,"and",num2,"is==>",lcm(num1,num2))