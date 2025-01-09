india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

user1 = input("Enter a city==>")
user2 = input("Enter a city==>")

if user1 == "mumbai" and "banglore" and "chennai" and "delhi":
    if user2 == "mumbai" and "banglore" and "chennai" and "delhi":
        print("both city in india")
    else:
        print("They don't belong to same country")
elif user1 == "lahore" or "karachi" or "islamabad":
    print("this city in pakistan ")
elif user1 == "dhaka" or "khulna" or "rangpur":
    print("this city in bangladesh ")
else:
    print("you choose a wrong option")
