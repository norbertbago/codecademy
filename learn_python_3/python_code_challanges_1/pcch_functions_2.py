# Python Code Challenges: Functions (Advanced)

# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should
# return the third multiple.

def first_three_multiples(num):
    print(num)
    print(num*2)
    print(num*3)
    return num*3

# Create a function called tip() that has two parameters named total and
# percentage. This function should return the amount you should tip given
# a total and the percentage you want to tip.

def tip(total, percentage):
  return total*percentage/100

# Write a function named introduction() that has two parameters named
# first_name and last_name. The function should return the last_name,
# followed by a comma, a space, first_name another space, and finally last_name.

def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

# Some say that every one year of a human’s life is equivalent to seven years
# of a dog’s life. Write a function named dog_years() that has two parameters
# named name and age. The function should compute the age in dog years and
# return the following string: "{name}, you are {age} years old in dog years"

def dog_years(name, age):
    return "{name}, you are {age} years old in dog years".format(name=name,age=age*7)

# Create a function named lots_of_math(). This function should have four
# parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print c subtracted from d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.

def lots_of_math(a,b,c,d):
    first = a + b
    second = c - d
    third = first * second
    last = third % a
    print(first)
    print(second)
    print(third)
    return last
