miles_total = 0
gallons_total = 0

gallons=float(input("Enter the gallons used (-1 to end): "))

while gallons !=-1:
    miles=float(input("Enter the miles driven: "))
    miles_total+=miles
    gallons_total+=gallons

    if gallons!=0:
        mpg=miles/gallons
        print("The miles/gallon for this tank was ",mpg)
    gallons=float(input("Enter the gallons used (-1 to end): "))
if gallons_total !=0:
    mpg_total=miles_total/gallons_total
    print("Total MPG so far: ",mpg_total)