

# Wartości mogą być umieszczone w łańcuchu za pomocą metody format

user_value = 42
string_value = "Your value is: {}".format(user_value)

print(string_value)


# Przykład z wieloma wartościami poniżej

name = "john"
name_length = len(name)

string_value = "Name {} has {} characters".format(name, name_length)

print(string_value)


# Od wersji Pythona 3.6+ możemy korzystać z f-strings

name = "john"
name_length = len(name)

string_value = f"Name {name} has {name_length} charactes"

print(string_value)


# Nawiasy mogą zawierać formułę do formatowania wartości
# https://docs.python.org/3/library/string.html#formatstrings

fraction = 2 / 3
print(fraction)

# ":." precyzja dziesiętna; "2" dwie pozycje; "f" format jako liczba zmiennoprzecinkowa
string_value = "Your fraction is: {:.2f}".format(fraction)
print(string_value)

# ":." precyzja dziesiętna; "1" jedna pozycja; "%" format jako procent
string_value = f"Percentage is: {fraction:.1%}"
print(string_value)


dollars = 50
cents = 5

# ":0" wypełnij zerami; "2" do dwóch miejsc
string_value = "Your total is ${},{:02}".format(dollars, cents)
print(string_value)

