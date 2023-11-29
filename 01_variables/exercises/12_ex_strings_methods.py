# 1
# Zapytaj użytkownika o imie.
# Wyświetl pozdrowienie z imieniem pisaną wielką literą.
#
# Np. w przypadku imienia „jan” wyświetl „Witaj Jan”

user_name = input("Provide your name:")

print("Witaj " + user_name.capitalize())
# 2
# Napisz kod, który policzy, ile razy fraza „Nowy Jork” została użyta w następującym fragmencie:

text = """New York, often called New York City (NYC) to distinguish it from the state of New York,
is the most populous city in the United States.
With a 2020 population of 8,804,190 distributed over 300.46 square miles (778.2 km2),
New York City is also the most densely populated major city in the United States.
"""


# 3
# Napisz kod, który znajdzie frazę „population” w tekście zmiennym (od #2). Wydrukuj indeks.

index_of_population = text.find("population")
print(index_of_population)




# 4
# Napisz kod, który zastąpi każdą frazę "New York City" słowem „NYC” w powyższym fragmencie tekstu.

text_with_replacement = text.replace("New York City", "NYC")
print(text_with_replacement)
# 5
# Użyj wyniku z punktu 3, aby wydrukować fragment tekstu wokół słowa „population”, w tym:
# 25 znaków przed słowem i 25 znaków po słowie.

index_of_population = text.find("population")
print(index_of_population)

print(text[:index_of_population])
