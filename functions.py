# function = A block of reusable code
#           place () after the function name to invoke it

# any data you send inside a function is called argument, but
# it needs a matching parameter

# def happy_birthday(name,age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()
#
# happy_birthday("Bro", 24)
# happy_birthday("Bro", 24)
# happy_birthday("Bro", 24)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
#
# display_invoice("Acacia",32.41,"01/01")

# return = statement used to end a function
#          and send a result back to the caller

# def add(x,y):
#     z = x + y
#     return z
#
# def subtract(x,y):
#     z = x - y
#     return z
#
# def multiply(x,y):
#     z = x * y
#     return z
#
# def divide(x,y):
#     z = x/y
#     return z
#
# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("acacia", "morningstar")
print(full_name)