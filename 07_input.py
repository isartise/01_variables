

# Funkcja input() służy do pobierania tekstu od użytkownika
user_input = input()
print(user_input)


# Funkcja input() przyjmuje łańcuch znaków, który będzie używany jako podpowiedź

user_input = input("Please state your name: ")
greeting = "Hello " + user_input
print(greeting)


# Funkcja input() zawsze zwraca łańcuch znaków! Nawet jeśli znaki to tylko cyfry

user_value = input("Please provide number from 1 to 10: ")
value_type = type(user_value)
print(value_type)

result = 10 + user_value
print(result)


# Musimy przekształcić tekst w liczbę

# int() dla liczb całkowitych

user_input = input("Please provide number from 1 to 10: ")

user_value = int(user_input)

value_type = type(user_value)
print(value_type)

result = 10 + user_value
print(result)


# float() dla liczb zmiennoprzecinkowych

user_input = input("Please provide number or fraction from 1 to 10: ")

user_value = float(user_input)

value_type = type(user_value)
print(value_type)

result = 10 + user_value
print(result)
