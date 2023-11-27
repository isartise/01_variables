

# Liczby zmiennoprzecinkowe i ograniczenia precyzji

print(0.1 + 0.1 + 0.1 == 0.3)

print(0.3)
print(0.1)
print(0.1 + 0.1 + 0.1)

print("{:.17f}".format(0.3))
print("{:.17f}".format(0.1 + 0.1 + 0.1))


# Liczby całkowite są nieograniczone
# https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types

number = 2 ** 63 - 1
print(number, type(number))

number_2 = number ** 2
print(number_2, type(number_2))

number_3 = number_2 * -2
print(number_3, type(number_3))
