# How do you split a string into a list?


# way 1 : using split()

str1 = "Python is awesome"
words = str1.split()
print(words,"\n")

# way 2 : spliting by specific delimiter

str2 = "Python,is,awesome"
words2 = str2.split(",")
print(words2,"\n")

# Way 3 : limiting number of split with max split()

str3 = "Hello , my name is sumit shastri"
words3 = str3.split(" ",3)
print(words3,"\n")


# way 4: splitting into characters

str4 = "Sumit"
chars = list(str4)
print(chars)