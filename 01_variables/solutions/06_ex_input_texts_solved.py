

# 1
# Ask the user for their name
# Then, print out a greeting using his name. E.g. "Hello John"

user_name = input("State your name: ")

print("Hello " + user_name)


# 2
# Ask the user for their name
# Then, print out how many letters there are in their name

user_name = input("State your name: ")
number_of_letters = len(user_name)

print(number_of_letters)


# 3
# Ask the user for their login
# Then, ask for password and print out following messages:
# Greeting with login, e.g. "Hello johnS"
# "Your password is hidden: #####"
# Use length of password to calculate how many "#" characters you need

user_login = input("Please provide login: ")
user_password = input("Please provide password: ")
pass_len = len(user_password)

print("Hello " + user_login)
print("Hidden password: " + "#" * pass_len)
