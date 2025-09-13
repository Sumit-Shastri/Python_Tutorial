# take string as input and convert to number

s = input("Enter a string : ")
a = int(s)
print(a)

# convert float 99.99 into a string

f = 99.99
g = int(f)
print(g)    # --> 99

# Convert integer 45 into a string and concatenate it with " is my age".

b = 45
c = str(b)
d = " is my age"
e = c + d
print(e)

# Take user input for a number and convert it into both int and float. Print both.

user = int(input("Enter a number : "))
user_int = int(user)
user_float = float(user)

print("casted int : ",user_int)
print("casted float : ",user_float)


# Convert True and False into integers. What do you get?

T = True
F = False

T_int = int(T)
F_int = int(F)

print("True : ",T_int,"\nFalse : ",F_int)  # 1   0