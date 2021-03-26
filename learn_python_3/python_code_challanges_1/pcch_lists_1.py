# Python Code Challenges: Lists

# Create a function called append_size that has one parameter named lst.
# The function should append the size of lst (inclusive) to the end of lst.
# The function should then return this new list.

def append_size(lst):
    lst.append(len(lst))
    return lst

# Write a function named append_sum that has one parameter — a list named
# named lst. The function should add the last two elements of lst together
# and append the result to lst. It should do this process three times and
# then return lst.

def append_sum(lst):
    lst.append(lst[-2]+lst[-1])
    lst.append(lst[-2]+lst[-1])
    lst.append(lst[-2]+lst[-1])
    return lst

# Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more
# elements. If both lists are the same size, then return the last element of lst1.

def larger_list(lst1, lst2):
    if len(lst1) == len(lst2):
        return lst1[-1]
    elif len(lst1) > len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

# Create a function named more_than_n that has three parameters named lst,
# item, and n. The function should return True if item appears in the list
# more than n times. The function should return False otherwise.

def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False

# Write a function named combine_sort that has two parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result.
# Return the new sorted list.

def combine_sort(lst1, lst2):
    new_lst = lst1 + lst2
    return sorted(new_lst)
