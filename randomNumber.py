# random module tutorial
import random

# Return number between x and y included both

a = random.randint(1,10)
print("random number between 1 and 10 (included both) : ",a)


# Return number between x(included) and y (not included)

b = random.randrange(1,11)
print("random number between 1(inluded) and 10 (not included) : ",b)



# Return random number from a list

fruits = ["apple","banana","oranges","mangoes"]
random_fruit = random.choice(fruits)
print("Random fruit is :",random_fruit)


# Return a random float number between 0 to 1

z = random.random()
print("Random float between 0 to 1 : ",z)


# Take a sequence and return in random order

sequence = [2,4,6,8,10,12,14,16,18,20]
random.shuffle(sequence)
print("Random sequence of 'sequence list' is : ",sequence)


# Uniform() --> returns a random float number between two given parameters

y = random.uniform(2,9)
print("random float between 2 to 9 is :",y)