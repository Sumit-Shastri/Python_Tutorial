# You get user input "3.14" (string). How would you safely cast it to float?

# Step 1
usr_input = "3.14"
usr_input_float = float(usr_input)
print(usr_input_float)
print(type(usr_input_float),"\n")

#Step 2 - handling it safely

s = input("Enter a number : ")
try :
    num = float(s)
    print("Valid number : ",num,"\n")
except ValueError:
    print("Invalid input ! Cannot covert to float\n")