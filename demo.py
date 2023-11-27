# demo code to see if everything works well!


def print_tree(height):
    for i in range(1, height + 1):
        row = " " * (height - i) + "*" * (2 * i - 1)
        print(row)


user_input = input("Please provide a number from 0 to 10: ")

try:
    height = int(user_input)
    print_tree(height)
except ValueError:
    print("Something other than number was provided!")
