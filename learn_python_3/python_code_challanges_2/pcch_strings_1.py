# Python Code Challanges: Strings

# Write a function called unique_english_letters that takes the string word as
# a parameter. The function should return the total number of unique letters
# in the string. Uppercase and lowercase letters should be counted as different letters.

def unique_english_letters(word):
  lst_word = []
  for letter in word:
    if letter in letters and letter not in lst_word:
      lst_word.append(letter)
  return len(lst_word)

# Write a function named count_char_x that takes a string named word and a
# single character named x as parameters. The function should return the
# number of times x appears in word.

def count_char_x(word, x):
  return word.count(x)

# Write a function named count_multi_char_x that takes a string named word and a
# string named x. This function should do the same thing as the count_char_x
# function you just wrote - it should return the number of times x appears in word.

def count_multi_char_x(word, x):
  return word.count(x)

# Write a function named substring_between_letters that takes a string named
# word, a single character named start, and another character named end.
# This function should return the substring between the first occurrence of
# start and end in word. If start or end are not in word, the function
# should return word.

def substring_between_letters(word, start, end):
  if start not in word or end not in word:
    return word
  else:
    start_index = word.index(start)+1
    end_index   = word.index(end)
    return word[start_index:end_index]

# Create a function called x_length_words that takes a string named sentence
# and an integer named x as parameters. This function should return True
# if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
    split_sentence = sentence.split()
    for word in split_sentence:
        if not(len(word)  >= x):
            return False
    return True
