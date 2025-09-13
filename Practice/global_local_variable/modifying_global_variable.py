# How do you modify a global variable inside a function? (use global)

# without global variable

a = 23

def modify_01():
    a = 30
    print("Modified a inside function  is : ",a)  # --> 30

modify_01()
print("Modified a outside function is : ",a,"\n") # --> 23



# With global variable

x = 23  # global variable

def modify_02():
    global x
    x = 30
    print("Modified x inside function is : ",x) # --> 30

modify_02()
print("Modified x outside function is : ",x) # --> 30
