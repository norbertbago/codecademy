# Python Code Challnages

# Create a function named larger_sum() that takes two lists of numbers as
# parameters named lst1 and lst2. The function should return the list whose
# elements sum to the greater number. If the sum of the elements of each list
# are equal, return lst1.

def larger_sum(lst1, lst2):
    if sum(lst1) > sum(lst2):
        return lst1
    elif sum(lst1) < sum(lst2):
        return lst2
    else:
        return lst1

# Create a function named over_nine_thousand() that takes a list of numbers
# named lst as a parameter. The function should sum the elements of the list
# until the sum is greater than 9000. When this happens, the function should
# return the sum. If the sum of all of the elements is never greater than 9000,
# the function should return total sum of all the elements. If the list is
# empty, the function should return 0.

def over_nine_thousand(lst):
    sum = 0
    for x in lst:
        if sum > 9000:
            return sum
        elif lst == []:
            return 0
        else:
            sum += x
    return sum


# Create a function named max_num() that takes a list of numbers named nums
# as a parameter. The function should return the largest number in nums

def max_num(nums):
  return max(nums)
