import math
x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
y1 = float(input("Enter the value of y1: "))
y2 = float(input("Enter the value of y2: "))

x= math.pow(((x1-x2)), 2)
y= math.pow(((y1-y2)), 2)

print(x)
print(y)

distance= round(math.sqrt(x + y), 2)
print ("The distance between the two given points is:", distance)
# It helped simplify the program because there were many functions.
# The functions sqrt and pow were much easier to use.
# Without sqrt and pow it would take much longer to finish the code.