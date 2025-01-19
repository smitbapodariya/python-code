def prm(no):
    c = 0
    for i in range(2,no):
        if no % 2 == 0:
            c = 1
            break
    if c==0:
        print(no,"is a prime number")
    else:
        print(no,"is not prime number")

prm(12)

