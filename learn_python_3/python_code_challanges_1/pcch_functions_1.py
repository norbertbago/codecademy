# Python Code Challanges: Functions

# Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.

def tenth_power(num):
    return num ** 10

# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.

def square_root(num):
    return num ** 0.5

# Create a function called win_percentage() that takes two parameters named
# wins and losses. This function should return out the total percentage of
# games won by a team based on these two numbers.

def win_percentage(wins, losses):
    return (wins/(wins + losses))*100

# Write a function named average() that has two parameters named num1 and num2.
# The function should return the average of these two numbers.

def average(num1, num2):
    return (num1 + num2)/2

# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.

def remainder(num1, num2):
  return (num1*2)%num2
