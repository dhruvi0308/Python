distance=int(input("Enter distane in kms:"))
if distance<1:
    print("You can walk")
elif 1 <= distance <= 5:
    print("You can bicycle")
elif 5 <= distance <= 20:
    print("You can take a car")
else:
    print("You can take a train")
