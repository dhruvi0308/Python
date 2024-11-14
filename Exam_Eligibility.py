c_held=int(input("Enter the number of classes held:"))
c_attend=int(input("Enter the number of classes attended:"))

a_per=(c_attend/c_held)*100
print(a_per,"%")
if a_per<80:
    print("Not permitted in exam")
else:
    print("Permitted in exam")