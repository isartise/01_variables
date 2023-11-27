

# 1
# Poll results are:
# "Yes" - 8
# "No" - 2
# Print out "+" and "-" characters for respecive options
# Calculate how many characters you need!
#
# Expected result in console:
#
# Yes
# ++++++++
# No
# --

votes_yes = 8
votes_no = 2

print("Yes")
print("+" * votes_yes)
print("No")
print("-" * votes_no)


# 2
# What happens when you change vote counts to 86 for "Yes" and 41 for "No"? Does it fit in one line?

votes_yes = 86
votes_no = 41

print("Yes")
print("+" * votes_yes)
print("No")
print("-" * votes_no)


# 3
# Let's say we want one character to represent 10 votes
# So 10 votes for "Yes", should print a single "+"
# Calculate the number of characters needed for data below and print the result
#
# Expected result in console
#
# Yes
# ++++++++
# No
# ----

votes_yes = 82
votes_no = 41

yes_marks = votes_yes // 10
no_marks = votes_no // 10

print("Yes")
print("+" * yes_marks)
print("No")
print("-" * no_marks)
