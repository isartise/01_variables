# 1
# Wyniki ankiety to:
# „Tak” - 8
# „Nie” - 2
# Wydrukuj znaki „+” i „-” dla odpowiednich opcji
# Oblicz, ile znaków potrzebujesz!
#
# Oczekiwany wynik w konsoli:
#
# Tak
#++++++++
# NIE
#--

votes_yes = 8
votes_no = 2

votes_yes_in_crosses = "++++++++"
votes_no_in_minus_signs = "--"
print("TAK")
print(votes_yes_in_crosses)
print("NIE")
print(votes_no_in_minus_signs)

# 2
# Co się stanie, jeśli zmienisz liczbę głosów na 86 na „Tak” i 41 na „Nie”? Czy mieści się to w jednej linijce?

votes_yes_in_crosses = 86 * "+"
votes_no_in_minus_signs = 41 * "-"

print(votes_yes_in_crosses)
print(votes_no_in_minus_signs)

# 3
# Powiedzmy, że chcemy, aby jeden znak reprezentował 10 głosów
# Zatem 10 głosów na „Tak”, powinno zostać wydrukowane pojedyncze „+”
# Oblicz liczbę znaków wymaganych dla poniższych danych i wydrukuj wynik
#
# Oczekiwany wynik w konsoli
#
# Tak
#++++++++
# NIE
# ----

votes_yes = 82
votes_no = 41

votes_yes_modified = (votes_yes // 10) * "+"
votes_no_modified = (votes_no // 10) * "-"

print(votes_yes_modified)
print(votes_no_modified)