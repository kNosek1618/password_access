
password = None
itter = 0
left = 4

while password != "night":
    itter += 1
    left -= 1
    password = input("enter your password: ")
    if password != "night":
        print(f"you have {left} left")
    if itter > 3 and password != "night":
        print("YOU LOCK!")
        break
else:
    print("CORRECT !")