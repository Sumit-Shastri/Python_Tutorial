# How do you concatenate 2 strings ?
from pygments.lexer import words

# method 1 : using '+' operator

str1 = "Sumit"
str2 = "Shastri"

str3 = "Mr. " + str1 + " " + str2

print(str3)


# Method 2 : using join()  --> Most efficient

str4 = ["Python","is","awesome"]
result = " ".join(str4)
print(result)


# Method 3 : using f-string

str5 = "sumit"
greetings = f"Hello, {str5} !"
print(greetings)


# method 4 : using % formatting

str6 = "Good"
str7 = "Morning"
result2 = "%s %s"%(str6,str7)
print(result2)

# Method 5 : using format() function ---> old method

s1 = "data"
s2 = "science"
result3 = "{} {}".format(s1,s2)
print(result3)