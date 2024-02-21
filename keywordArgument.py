# keyword arguments = an argument preceded by an identifier
# helps with readability
# order of arguments doesn't matter
# 1. positional 2. DEFAULT 3. keyword 4. arbitrary

# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")
#
# hello("Hello", "Miss", last="Morningstar", first="Acacia")

# for x in range(1,11):
#     print(x, end=" ")

# print("1","2","3","4","5", sep="-")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=91, area=123, first=456, last=7890)
print(phone_num)