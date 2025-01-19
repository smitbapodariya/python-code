def fibb(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibb(num-1) + fibb(num-2)

print(fibb(10))

