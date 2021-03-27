# Python Code Challange: Dictionaries

# Write a function named sum_values that takes a dictionary named my_dictionary
# as a parameter. The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  sum_values = 0
  for item in my_dictionary.values():
    sum_values += item
  return sum_values

# Create a function called sum_even_keys that takes a dictionary named
# my_dictionary, with all integer keys and values, as a parameter.
# This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
  sum_keys = 0
  for key,item in my_dictionary.items():
    if key%2 == 0:
      sum_keys += item
  return sum_keys

# Create a function named add_ten that takes a dictionary with integer values
# named my_dictionary as a parameter. The function should add 10 to every
# value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):
  for key in my_dictionary:
    my_dictionary[key] +=10
  return my_dictionary

# Create a function named values_that_are_keys that takes a dictionary named
# my_dictionary as a parameter. This function should return a list of all
# values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
  new_lst = []
  for item in my_dictionary.values():
    if item in my_dictionary:
      new_lst.append(item)
  return new_lst

# Write a function named max_key that takes a dictionary named my_dictionary
# as a parameter. The function should return the key associated with the
# largest value in the dictionary.

def max_key(my_dictionary):
  max_value = max(my_dictionary.values())
  for key in my_dictionary.keys():
    if my_dictionary[key] == max_value:
      return key
