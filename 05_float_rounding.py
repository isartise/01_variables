

# Zaokrąglanie może być stosowane w obliczeniach do radzenia sobie z precyzją

print(0.1 + 0.1 + 0.1 == 0.3)

print(0.3)
print(0.1 + 0.1 + 0.1)

print(round(0.3, 2))
print(round(0.1 + 0.1 + 0.1, 2))

# Wynik będzie taki, jak się spodziewamy

print(round(0.1 + 0.1 + 0.1, 2) == round(0.3, 2))

# Ale to, co jest w pamięci komputera, nie może być zmienione!

print("{:.27f}".format(0.3))
print("{:.27f}".format(round(0.3, 2)))

# Trzeba uważać również na zaokrąglanie

print(round(0.05, 1))
print("{:.27f}".format(0.05))

print(round(0.15, 1))
print("{:.27f}".format(0.15))

print(round(0.0499999999999999999, 1))
print("{:.27f}".format(0.0499999999999999999))
