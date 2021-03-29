# Python Code Challnages: Strings (Advanced)

# Write a function called check_for_name that takes two strings as parameters
# named sentence and name. The function should return True if name appears in
# sentence in all lowercase letters, all uppercase letters, or with any mix of
# uppercase and lowercase letters. The function should return False otherwise.

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

# Create a function named every_other_letter that takes a string named word as
# a parameter. The function should return a string containing every other letter in word.

def every_other_letter(word):
    new_word = ""
    for letter in range(0,len(word),2):
      new_word += word[letter]
    return new_word

# Write a function named reverse_string that has a string named word as a
# parameter. The function should return word in reverse.

def reverse_string(word):
  return word[-1::-1]

# Write a function called make_spoonerism that takes two strings as parameters
# named word1 and word2. Finding the first syllable of a word is a difficult
# task, so for our function, we’re going to switch the first letters of each word.
# Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
  return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

# Create a function named add_exclamation that has one parameter named word.
# This function should add exclamation points to the end of word until word is
# 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  if len(word) >= 20:
    return word
  else:
    return word + "!"*(20-len(word))
