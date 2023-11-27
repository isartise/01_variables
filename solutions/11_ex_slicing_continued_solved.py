


# 1
# Ask user for a word
# If it is longer than 4 characters,
# create and print out new word consisting of first two and last two characters from given string
# Otherwise, print out empty string
#
# E.g. from "elephant" print out "elnt"

user_word = input("Please provide a word: ")

if len(user_word) > 4:
    print(user_word[:2] + user_word[-2:])
else:
    print("")


# 2
# Ask user for two words
# Switch first letters and print result joined with "&" character
#
# E.g. from "dog" and "fox" print out "fog&dox"

word_one = input("Please provide the first word: ")
word_two = input("Please provide the second word: ")

print(word_two[0] + word_one[1:] + "&" + word_one[0] + word_two[1:])
