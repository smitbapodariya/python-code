marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20
}
for key,value in marks.items():
    if value>=18:
        print(key,value," pass")
    else:
        print(key,value," fail")
print("pass record==>")
for key,value in marks.items():
    if value>=18:
        print(key,value," pass")
        