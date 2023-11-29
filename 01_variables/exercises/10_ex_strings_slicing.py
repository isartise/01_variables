

text = "The quick brown fox"
secret_message = "Ppy!tthooono ai!s@ #c$oooolo!o"

# 1
# Z tekstu zmiennej wypisz pierwsze trzy znaki („The”)

print(text[0:3])
# 2
# # Z tekstu zmiennego wydrukuj od 5. do 9. znaku ("quick")

print(text[4:9])

# 3
# Ze zmiennej secret_message wypisz co drugi znak

print(len(secret_message))
print(secret_message[:29:2])
# 4
# Użyj slicingu, aby utworzyć następujący ciąg:
# "The fox"
print(text[:3] + " " + text[-3:])

# 5
# Użyj slicingu, aby utworzyć następujący ciąg:
# "The kciuq brown fox"

reversed_fragment = text[4:9]

print(text[:3] + " " + reversed_fragment[::-1] + " " + text[10:20])