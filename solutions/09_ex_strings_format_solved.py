

# 1
# Below is variable score. Use it and string formatting to display message:
# "Your score is 90.75!"
# Use format method or formatted string

score = 90.75

# No longer adding strings!
# "Your score is " + str(score) + "!"

print("Your score is {}!".format(score))
print(f"Your score is {score}!")


# 2
# Use score from #1
# Display the same message, but specify formatting to show three decimal places.
# Expected result: "Your score is 90.750!"

print("Your score is {:.3f}!".format(score))


# 3
# A few years ago 41737 programmers out of 88615 used Python
# Print out this fraction as a percentage with decimal precision of one place.
# Expected result: "47.1% programmers use Python!"

fraction = 41737 / 88615

print(f"{fraction:.1%} programmers use Python!")
