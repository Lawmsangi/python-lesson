#typecasting = The process of converting a value of one data
#type to another(string,boolean,float,integer)
#Explicit vs Implicit
#typecasting is used to see if somebody typed in their name or not
#implicit is when a value or variable is converted into different
#data type automatically

name = "Acacia"
age = 23
gpa = 4.3
student = True

#print(type(student))
student = str(student)
gpa = int(gpa)
age = float(age)
#print(type(age))
print(type(student))

#implicit
x = 2
y = 2.0

x = x/y

print(x)