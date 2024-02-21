# *args = allows you to pass multiple non-key arguments(* is a must)
# **kwargs = allows you to pass multiple keyword arguments
#  * unpacking operator
# 1. positional 2. DEFAULT 3. keyword 4. arbitrary

# Example 1:
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(3,2,1))

# Example 2:
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Miss","Acacia","Morningstar", "II")

# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address(street="111 Fake St.",
#               apt="100",
#               city="Aizawl",
#               state="Mizoram",
#               zip="12345")

# Exercise

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.","Spongebob","Squarepants","III",
               street="111 Fake St.",
               pobox= "PO Box #1200",
               city="Aizawl",
               state="Mizoram",
               zip="12345"
               )