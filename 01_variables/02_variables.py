# Liczby całkowite (Integers)

x = 1
print(x)
print(type(x))


# Liczby zmiennoprzecinkowe (Floats)

pi = 3.14
print(pi)
print(type(pi))


# Tekst, ciąg znaków (Strings)

text = "Lorem ipsum"
print(text)
print(type(text))


# Przypisanie wyniku obliczeń

result = (12 + 23 - 10) * 5
print(result, type(result))


# Zmiana typu zmiennej

result = "Hello!"
print(result, type(result))


# Użycie zmiennych w obliczeniach

number_a = 5
number_b = number_a - 3
print(number_b)


# "Konwersje" - Tworzenie wartości konkretnego typu, bazując na innych wartościach

text_value = "3.14"
float_value = float(text_value)
print(float_value)
print(type(float_value))


text_value = "1"
integer_value = int(text_value)
print(integer_value)
print(type(integer_value))


float_value = 3.14
text = "Moja ulubiona liczba to: " + str(float_value)
print(text)
