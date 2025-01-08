result = ["head","tail","head","head","tail","head","head","tail","tail","head","tail"]
head = 0
tail = 0
for re in result:
    if re == "head":
        head += 1
print(head,"times of head")