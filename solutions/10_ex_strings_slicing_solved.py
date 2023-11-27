

text = "The quick brown fox"
secret_message = "Ppy!tthooono ai!s@ #c$oooolo!o"

# 1
# From variable text, print out first three characters ("The")

fragment = text[:3]
print(fragment)


# 2
# From variable text, print out from 5th character to 9th ("quick")

fragment = text[4:9]

print(fragment)


# 3
# From variable secret_message, print out every other character

message = secret_message[::2]
print(message)


# 4
# Use slicing on variable text to create following string:
# "The fox"

text = "The quick brown fox"

word_1 = text[:3]  # 0, 1, 2 indexes
word_2 = text[-3:]  # -3, -2, -1

print(word_1)
print(word_2)
print(word_1 + " " + word_2)

# 5
# Use slicing on variable text to create following string:
# "The kciuq brown fox"

text = "The quick brown fox"

fragment = text[4:9]
reversed_fragment = fragment[::-1]
print(reversed_fragment)

solution = text[:4] + reversed_fragment + text[9:]
print(solution)
