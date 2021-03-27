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
    
