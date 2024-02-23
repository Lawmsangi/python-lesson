# sort() method   = used with lists
# sort() function = used with iterables

students = ("Bubu","Dudu","Meemaw","Acacia")

# students.sort(reverse=True)
# sorted_students = sorted(students,reverse=True)
#
# for i in sorted_students:
#     print(i)

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))
age = lambda ages:ages[2]
# grade = lambda grades:grades[1]
sorted_students = sorted(students,key=age)
# students.sort(key=age)

for i in sorted_students:
    print(i)