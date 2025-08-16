side1 = int(input("Enter First Side:"))
side2 = int(input("Enter Second Side:"))
side3 = int(input("Enter Third Size:"))

if side1 == side2 or side2 == side3 or side3 == side1:
    print("It's an Isosceles Triangle")
else:
    print("It's not isosceles Triangle")
