# 1
# Poproś użytkownika o podanie długości i szerokości prostokąta (użyj dwóch danych wejściowych)
# Oblicz i wydrukuj powierzchnię i obwód

user_rectangle_a = float(input("Provide rectangle side a:"))
user_rectangle_b = float(input("Provide rectangle side b:"))

area = user_rectangle_a * user_rectangle_b
circuit = 2 * user_rectangle_b + 2 * user_rectangle_a

print(area)
print(circuit)

# 2
# Zapytaj użytkownika, ile głosów było w ankiecie na „Tak”, a ile na „Nie” (użyj dwóch danych wejściowych)
# Wydrukuj znaki „+” i „-” dla odpowiednich opcji
#
# Oczekiwany wynik w konsoli, jeśli użytkownik podał 8 dla „Tak” i 2 dla „Nie”:
#
# Tak
#++++++++
# NIE
#--

user_votes_yes = int(input("Provide votes for yes:"))
user_votes_no = int(input("Provide votes for no:"))

print("TAK")
print(user_votes_yes * "+")
print("NO")
print(user_votes_no * "-")