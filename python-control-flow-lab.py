# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
letter = input("Please enter a letter from the alphabet (a-z or A-Z)?")
letter = letter.lower()
# 2. Write the code that determines whether the letter entered is a vowel
# Prompt the user to enter a letter
# Convert the letter to lowercase for case-insensitive comparison
# Define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
# Check if the letter is a vowel
if letter == vowels[0] or letter == vowels[1] or letter == vowels[2] or letter == vowels[3] or letter == vowels[4]:
    print(f"The letter {letter} is a vowel.")
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
x = letter
if x == vowels[0] or x == vowels[1] or x == vowels[2] or x == vowels[3] or x == vowels[4]:
    print(f"The letter {x} is a vowel.")
else:
    print(f"The letter {x} is a consonant.")

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
# if x in vowels:
#     print(f"The letter {x} is a vowel.")
# else:
#     print(f"The letter {x} is a consonant.")
    
# exercise-02 Length of Phrase
    
# Write the code that:
# 1. Prompts the user to enter a phrase:
phrases = []
phrase = input("Please enter a word or phrase (or type 'quit' to exit): ")
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
phrases.append(phrase)
    # Print the length of the entered phrase
phrase_length = len(phrase)
print(f"What you entered is {phrase_length} characters long")
# 3. Return to step 1, unless the word 'quit' was entered.
if phrase.lower() == 'quit':
    print("Goodbye!")
else:
    phrases.append(phrase)
    phrase_length = len(phrase)
    print(f"What you entered is {phrase_length} characters long")

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

dog_age = int(input("Input a dog's age: "))
if dog_age < 3:
    dog_years = dog_age * 10
else:
    dog_years = 20 + (dog_age - 2) * 7

print(f"The dog's age in dog years is {dog_years}")

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lengths of three sides of a triangle:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == b == c:
    triangle_type = "equilateral"
elif a != b and b != c and c != a:
    triangle_type = "scalene"
else:
    triangle_type = "isosceles"

print(f"A triangle with sides of {a}, {b} & {c} is a {triangle_type} triangle.")





# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1

# Print the first 50 terms of the Fibonacci sequence
for term in range(50):
    print(f"term: {term} / number: {a}")
    a, b = b, a + b


# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
# Prompt the user to enter the month and day

month = input("Enter the month of the year (Jan - Dec): ")
day = int(input("Enter the day of the month: "))

# dictionary to map months to numbers for easier comparison
month_numbers = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
month_number = month_numbers[month]

# Determine the season based on the month and day
if (month_number < 3) or (month_number == 3 and day < 20) or (month_number == 12 and day >= 21):
    season = "Winter"
elif (month_number < 6) or (month_number == 6 and day < 21):
    season = "Spring"
elif (month_number < 9) or (month_number == 9 and day < 22):
    season = "Summer"
else:
    season = "Fall"

print(f"{month} {day} is in {season}")



