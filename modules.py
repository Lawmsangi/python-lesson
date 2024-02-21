# module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

# built-in
# import math
# # import math as m
# # from math import e
# a,b,c,d,e = 1,2,3,4,5
#
# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

# make our own module
import exampleModule

result = exampleModule.pi
result = exampleModule.square(3)
result = exampleModule.cube(3)
result = exampleModule.circumference(3)
result = exampleModule.area(3)

print(result)