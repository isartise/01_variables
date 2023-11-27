import math

# 1
# Poniżej podano boki prostokąta
# Oblicz przekątną, korzystając z twierdzenia Pitagorasa

a = 8
b = 13

diagonal = math.sqrt(a**2 + b**2)
print(diagonal)

# 2
# Poniżej podano współrzędne dwóch punktów
# Oblicz odległość między nimi (również korzystając z twierdzenia Pitagorasa)

A_x = 30
A_y = 150
B_x = 120
B_y = 100

x = 90
y = 50

distance = math.sqrt (math.pow(x,2) + math.pow(y,2))
print(distance)


# 3
# Używanie liczb zmiennoprzecinkowych do obsługi pieniędzy może być złym pomysłem
# Użyj poniższych zmiennych, aby obliczyć sumę w dolarach i centach

dollars_1 = 14
cents_1 = 23
dollars_2 = 10
cents_2 = 50

dollars_sum = dollars_1 + cents_1/100 + dollars_2 + cents_2 / 100
print(dollars_sum)

cents_sum = dollars_1 * 100 + cents_1 + dollars_2 * 100 + cents_2
print(cents_sum)
# 4
# Zmień wartości z ćwiczenia 3 na 14,23 $ i 10,99 $
# Jakie zmiany? Spróbuj to naprawić, używając wyłącznie liczb całkowitych



# 5
# Zmień wartości z ćwiczenia 3 na 14,23 $ i 10,80 $
# Jakie zmiany? Co może się przydać?