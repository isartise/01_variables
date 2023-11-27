

# Wyciąganie fragmentów oznacza pobieranie znaków z określonego zakresu
# [start : stop : krok]

# Znak, który odpowiada indeksowi stop, nie będzie uwzględniony!
text = "The quick brown fox"

print(text[0:3])  # zwraca znaki o indeksach 0, 1, 2 (bez 3!)
print(text[4:9])  # zwraca znaki o indeksach 4, 5, 6, 7, 8 (bez 9!)

# Przy żądaniu [start : stop : krok] niektóre parametry mogą być opcjonalne!

print(text[:])  # Cały string

print(text[:3])  # Od domyślnego startu (początek łańcucha) do 3 (wyłączone)

print(text[4:])  # Od 4 (włącznie) do domyślnego stopu (koniec łańcucha)

print(text[::-1])  # Wszystko, ale wspak (krok -1)


# Te fragmenty to nowe łańcuchy - mogą być przypisane i używane

animal = text[-3:]
print(animal)

# Co drugi znak
print(text[:8:2])

print(text[::2])
