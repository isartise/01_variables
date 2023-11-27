

# Typ string ma wiele użytecznych metod
# Oryginalny łańcuch znakowy nie jest modyfikowany! Zwracany jest nowy łańcuch, jeśli jest to możliwe


string_value = "The quick brown fox"


# Capitalize

name = "john"
capitalized_name = name.capitalize()

print(capitalized_name)


# Upper

text = "The quick brown fox"
all_caps = text.upper()

print(all_caps)


# Lower

text = "The quick brown fox"
all_lower = text.lower()

print(all_lower)


# Count

text = "The quick brown fox"
count_of_o = text.count("o")

print(count_of_o)


# Find

text = "The quick brown fox"
index_of_fox = text.find("fox")

print(index_of_fox)
print(text[:index_of_fox])


# Replace

text = "The quick brown fox"
text_with_replacement = text.replace("fox", "dog")

print(text_with_replacement)


text = "The quick brown fox fox fox"
text_with_replacement = text.replace("fox", "dog")

print(text_with_replacement)


text = "The quick brown fox fox fox"
text_with_replacement = text.replace("fox", "dog", 1)

print(text_with_replacement)

# Dodatkowe rozwiązanie jak zamienić łańcuch ale zaczynając od końca
# Dokumentacja: https://docs.python.org/3/library/stdtypes.html#str.rsplit
# Dokumentacja: https://docs.python.org/3/library/stdtypes.html#str.join


text_to_replace = "fox"
replacement_text = "dog"

print(replacement_text.join(text.rsplit(text_to_replace, 1)))