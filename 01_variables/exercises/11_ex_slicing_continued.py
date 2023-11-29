# 1
# Poproś użytkownika o słowo
# Jeśli jest dłuższy niż 4 znaki,
# utwórz i wydrukuj nowe słowo składające się z dwóch pierwszych i dwóch ostatnich znaków z podanego ciągu
# W przeciwnym razie wydrukuj pusty ciąg
#
# Np. z „elephant” wypisz „elnt”

user_word = input("Provide a word:")
if len(user_word) > 4:
    print(user_word[:2] + user_word[-2:])
else:
    print("")

# 2
# Poproś użytkownika o dwa słowa
# Zmień pierwsze litery i wydrukuj wynik połączony znakiem „&”.
#
# Np. z "dog" i "fox" wydrukuj "fog&dox"

word_1 = input("Provide first word:")
word_2 = input("Provide second word:")

print(word_2[0] + word_1[1:] + "&" + word_1[0] + word_2[1:])