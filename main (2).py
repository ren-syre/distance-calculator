import math

# Input the coordinates of the first point.
x1 = float(input("Enter the value of x1: "))
y1 = float(input("Enter the value of y1: "))

# Input the coordinates of the second point.
x2 = float(input("Enter the value of x2: "))
y2 = float(input("Enter the value of y2: "))

# Find out the distance using the distance formula.
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"The distance between the two points is: {distance:.2f}")

# It helped simplify the program because there were many functions.
# The functions sqrt and pow were much easier to use.
# Without sqrt and pow it would take much longer to finish the code.
