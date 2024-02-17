import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
#c = root over a square + b square
c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C = {round(c,2)}")

