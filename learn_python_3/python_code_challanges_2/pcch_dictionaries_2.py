# Python Code Challanges: Dictionaries(Advance)

# Write a function named word_length_dictionary that takes a list of strings
# named words as a parameter. The function should return a dictionary of
# key/value pairs where every key is a word in words and every value is the
# length of that word.

def word_length_dictionary(words):
  new_dictionary = {}
  for word in words:
    new_dictionary[word] = len(word)
  return new_dictionary

# Write a function named frequency_dictionary that takes a list of elements
# named words as a parameter. The function should return a dictionary
# containing the frequency of each element in words.

def frequency_dictionary(words):
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

# Create a function named unique_values that takes a dictionary named
# my_dictionary as a parameter. The function should return the number
# of unique values in the dictionary.

def unique_values(my_dictionary):
  lst = []
  for item in my_dictionary.values():
    if item not in lst:
      lst.append(item)
  return len(lst)

# Create a function named count_first_letter that takes a dictionary named
# names as a parameter. names should be a dictionary where the key is a last
# name and the value is a list of first names. For example, the dictionary
# might look like this:

# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter
# of a last name, and the value is the number of people whose last name begins
# with that letter. So in example above, the function would return:

# {"S" : 4, "L": 3}

def count_first_letter(names):
  new_dictionary = {}
  for first_name,last_name in names.items():
    if first_name[0] not in new_dictionary:
      new_dictionary[first_name[0]] = len(last_name)
    else:
      new_dictionary[first_name[0]] += len(last_name)
  return new_dictionary
