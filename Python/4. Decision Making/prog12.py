side1 = int(input("Enter First Side: "))
side2 = int(input("Enter Second Side: "))
side3 = int(input("Enter Third Side: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")

elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")