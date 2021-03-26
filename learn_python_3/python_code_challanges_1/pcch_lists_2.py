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

def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2):
        return item1
    elif lst.count(item1) < lst.count(item2):
        return item2
    else:
        return item1

# Create a function named double_index that has two parameters: a list named
# lst and a single number named index. The function should return a new list
# where all elements are the same as in lst except for the element at index.
# The element at index should be double the value of the element at index of
# the original lst. If index is not a valid index, the function should return
# the original list.

def double_index(lst, index):
  if index <= len(lst):
      lst[index] = lst[index] * index
      return lst
  else:
      return lst

# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return
# the middle element. If there are an even number of elements, the function
# should return the average of the middle two elements.

def middle_element(lst):
    if len(lst)%2 == 0:
        sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
        return sum / 2
    else:
        return lst[int(len(lst)/2)]
