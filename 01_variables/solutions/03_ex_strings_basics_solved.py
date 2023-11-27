

# 1
# Put your name in variable called user_name

user_name = "john"


# 2
# Create email address based on user_name using variable below, print it to console
# Example of result: "john@gmail.com"

domain = "gmail.com"
full_domain = "@" + domain
email_address = user_name + full_domain

print(email_address)


# 3
# Email above is not unique, let's make it more complicated
# Put your surname in variable called user_surname
# Create email address based on user_name, length of the surname, and domain, print it to console
# Use the variables that you have
# Example of result: "john9@gmail.com"

user_surname = "doe"
surname_length = len(user_surname)

email_address = user_name + str(surname_length) + "@" + domain
print(email_address)
