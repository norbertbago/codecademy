# Python Code Challange: Loops

# Create a function named divisible_by_ten() that takes a list of numbers named
# nums as a parameter. Return the count of how many numbers in the list are
# divisible by 10.

def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num%10==0:
            count +=1
    return count

# Create a function named add_greetings() which takes a list of strings named
# names as a parameter. In the function, create an empty list that will contain
# each greeting. Add the string 'Hello, ' in front of each name in names and
# append the greeting to the list. Return the new list containing the greetings.

def add_greetings(names):
    return [('Hello, ' + name) for name in names]

# Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of
# the list is not even. The function should then return lst.

def delete_starting_evens(lst):
    for item in lst:
        if item%2!=0:
            return lst[lst.index(item):]
    return []

# Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from
# lst that has an odd index. The function should then return this new list.

def odd_indices(lst):
    return [x for x in lst if lst.index(x)%2 != 0]

# Create a function named exponents() that takes two lists as parameters named
# bases and powers. Return a new list containing every number in bases raised
# to every number in powers.

def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst
