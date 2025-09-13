'''
Given a dictionary {"1": "100", "2": "200"},
convert both keys and values to integers.
'''

a = {"1":"100","2":"200"}

casted_a = {int(k): int(v) for k,v in a.items()}
print(casted_a)
print(type(casted_a))

