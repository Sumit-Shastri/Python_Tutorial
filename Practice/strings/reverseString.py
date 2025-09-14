# How do you reverse a string in Python?

# Way 1 : slicing

str1 = "Python"
str1_reversed = str1[::-1]
print(str1_reversed,"\n")


# Way 2 : using loop

str2 = "Python"
str2_reversed = ""

for ch in str2:
    str2_reversed = ch + str2_reversed
print(str2_reversed,"\n")


# using reversed() + join()

str3 = "Python"
str3_reversed = "".join(reversed(str3))
print(str3_reversed)