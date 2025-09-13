"""
How would you write a function that takes a list of strings
like ["1", "2", "3"] and casts them all to integers, handling
errors gracefully?
"""

def caster(lst):
    for i in lst:
            a = int(i)
            print(a)

list1 = ["1","5","7","34","21"]

caster(list1)


# with error handling

def safe_list_cast(lst):
    result = []
    for i in lst:
        try:
            result.append(int(i))
        except ValueError:
            print("Skipping invalid value : ",i)
    print(result)

safe_list_cast(list1)

list2 = ["14","34","8","65","three","21","five","90"]
safe_list_cast(list2)