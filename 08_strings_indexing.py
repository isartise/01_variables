

# Możemy uzyskać dostęp do znaków za pomocą indeksowania
# Indeksowanie zaczyna się od 0 (pierwszy znak) i sięga do długości-1 (ostatni znak)


text = "The quick brown fox"
print(len(text))

first_character = text[0]

print(first_character)

second_character = text[1]
print(second_character)

last_character = text[18]
print(last_character)

# Próba uzyskania dostępu do znaku z indeksem wyższym niż długośc stringa skutkuje błędem!

more = text[19]
print(more)


# Inny sposób indeksowania wspak od -długość (pierwszy znak) aż do -1 (ostatni znak)

first_character = text[-19]
print(first_character)

second_character = text[-18]
print(second_character)

last_character = text[-1]
print(last_character)

# Ale to nie jest takie dziwne, jak się wydaje!

length = len(text)

last_character = text[length-1]
print(last_character)

second_to_last_character = text[length-2]
print(second_to_last_character)


# Jednak string nie jest mutowalny (zmienny) - nie możemy przypisywać nowych wartości do indeksów!

text[0] = "A"

