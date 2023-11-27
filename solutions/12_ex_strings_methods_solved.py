

# 1
# Ask the user for name.
# Display greetings with name capitalized.
#
# E.g. for name "john", display "Hello John"

user_name = input("State your name please: ")
capitalized_name = user_name.capitalize()

print("Hello " + capitalized_name)


# 2
# Write code, that will count how many times phrase "New York" is used in following fragment:

text = """New York, often called New York City (NYC) to distinguish it from the state of New York,
is the most populous city in the United States.
With a 2020 population of 8,804,190 distributed over 300.46 square miles (778.2 km2),
New York City is also the most densely populated major city in the United States.
"""

ny_count = text.count("New York")
print(ny_count)


# 3
# Write code, that will find phrase "population" in variable text (from #2). Print out the index.

pop_index = text.find("population")
print(pop_index)


# 4
# Write code, that will replace each phrase "New York City" with "NYC", in the above text fragment.

replaced_text = text.replace("New York City", "NYC")
print(replaced_text)


# 5
# Use result from #3 to print out text fragment around word "population", including:
# 25 characters before the word and 25 characters after the word.

print(text[pop_index-25:pop_index+25+len("population")])
