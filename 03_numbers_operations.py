

# ** to dedykowany operator potęgi

number = 2
second_power = number ** 2
fourth_power = number ** 4
print(second_power)
print(fourth_power)

square_root = 4 ** 0.5
print(square_root)


# Zwykłe dzielenie
# Wynik zawsze jest liczbą zmiennoprzecinkową!

print(10 / 2)


# Zwracanie ilorazu
# Dla dwóch liczb całkowitych, wynik jest liczbą całkowitą
# Reszta jest pomijana

print(10 // 2)
print(19 // 10)


# Zwracanie reszty - Operacja modulo
# Dla dwóch liczb całkowitych, wynik jest liczbą całkowitą

print(10 % 10)
print(19 % 10)


# Mieszanie liczb całkowitych i zmiennoprzecinkowych działa dobrze, ale zmiennoprzecinkowa jest zaraźliwa

print(15 + 1.5)
print(25.5 / 2)
print(10 + 1.0)
print(type(10 + 1.0))


# Ma to wpływ na operatory dzielenia!

print(19.0 // 10)
print(19 // 10.0)

print(19.0 % 10)
print(19 % 10.0)
