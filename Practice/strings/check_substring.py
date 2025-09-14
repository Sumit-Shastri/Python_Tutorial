# How do you check if a substring exists in a string?

# Way 1 - Using 'in' operator

str1 = "Python is awesome"
print("Python" in str1)   # True
print("java" in str1,"\n")  # False


# Way 2 - Using find() or index()

str2 = "Python is awesome"
print(str2.find("is"))   # 7 (index of first outcome)
print(str2.find("hello"),"\n")  # -1 (not found)

print(str2.index("is"))  # 7 (index of first outcome)
# print(str2.index("hello"))  # ValueError (raises error)


# Way 3 - using count()

str3 = "Python is awesome"
print(str3.count("aw"))  # >1  that means yes
print(str3.count("hello")) # 0 , that means no

