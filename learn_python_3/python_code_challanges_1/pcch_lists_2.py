# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100
# (inclusive).

def every_three_nums(start):
    return [x for x in range(start, 101, 3)]

# Create a function named remove_middle which has three parameters named lst,
# start, and end. The function should return a list where all elements in lst
# with an index between start and end (inclusive) have been removed.

def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]

# Create a function named more_frequent_item that has three parameters named
# lst, item1, and item2. Return either item1 or item2 depending on which
# item appears more often in lst. If the two items appear the same number
# of times, return item1.
