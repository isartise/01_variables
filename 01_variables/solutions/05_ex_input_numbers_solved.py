

# 1
# Ask the user to provide length and width of rectangle (use two inputs)
# Calculate and print out area and perimeter

length = input("length: ")
width = input("width: ")
length_value = float(length)
width_value = float(width)

area = length_value * width_value
perimeter = 2 * length_value + 2 * width_value

print(area)
print(perimeter)


# 2
# Ask user how many votes there were for "Yes" and how many for "No" options in poll (use two inputs)
# Print out "+" and "-" characters for respecive options
#
# Expected result in console if user provided 8 for "Yes" and 2 for "No":
#
# Yes
# ++++++++
# No
# --

vote_yes = input("enter number of votes for yes: ")
vote_no = input("enter number of votes for no: ")
yes_value = int(vote_yes)
no_value = int(vote_no)

print('yes')
print("+" * yes_value)
print("no")
print("-" * no_value)
