# Learning globals function

'''
GLobals function return a dictionary representing the current
global system table.
'''

# Ex 1

x = 10
y = "Sumit"

print(globals())


#Ex 2 -> Accesing / modifying global variable

a = 5

def modify():
    globals()['a'] = 100
    print("Inside modify() : ",a)  # --> 100

modify()
print("Outside modify() : ",a)  #  --> 100


# Ex 3 --> Difference from locals()

b = 50

def bar():
    c = 10
    print("locals : ",locals())   # -->  {'c' : 10}
    print("globals : ",globals().keys())

bar()