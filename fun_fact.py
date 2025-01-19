def fac(num):
    fact = 1
    for i in range(1,num):
        fact *= i
    print("factorial of",num,"is: ",fact)

fac(5)