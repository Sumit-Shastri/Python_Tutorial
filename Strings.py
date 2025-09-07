# Strings in python are written in 'single quoutes' or "double quotes"


# example
# both are same
a = "Hello\n"
b = 'Hello\n'

print(a)
print(b)


# Multiline strings

c = '''This is a 
multiline string
using 3 single quates\n'''

d = """This is a 
multiline string
using 3 double
quotes\n"""

print(c)
print(d)


# strings as an Array

strarr = "Hello"
print(strarr[1])


# Looping in Strings

str = "\nThis string is used for looping\n"

for i in str:
    print(i)


# Finding length of a string using len() function

str1 = "SumitShastti"
print(len(str1))


# Checking string

str2 = "Alan walker was dancing in Amitabh bacchan's Bathroom"
print("was" in str2)

  #with if statement

if "was" in str2:
    print("Yes , Alan walker was dancing\n")


# Checking if not using 'not in'

print("helo" not in str)

  #using if statement

if "hello" not in str2:
    print("Still alan walker is dancing")
