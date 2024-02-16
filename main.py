#collection = single "variable" used to store multiple values
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK. No duplicated
#tuple = () ordered and unchangeable. Duplicates OK. Faster

#fruits = ["apple","orange","banana","coconut"]
#fruits = {"apple","orange","banana","coconut","coconut"}
fruits = ("apple","orange","banana","coconut","coconut")
#print(dir(fruits))
#print(fruits[::3])
#fruits[0]= "pineapple"
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(2,"pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("coconut"))
#print(fruits.count("pineapple"))
for fruit in fruits:
    print(fruit)
#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop()
#print(fruits)
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pine" in fruits)