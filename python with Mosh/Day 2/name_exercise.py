name = input("Enter your name: ")

if len(name) < 3:
    print("Name must have atleast 3 char lengths")
elif len(name) > 50:
    print("Name can be of max 50 char length")
else:
    print("name looks good")