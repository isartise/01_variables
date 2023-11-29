# 1
# Poniżej znajduje się wynik przypisany do zmiennej. Użyj go i sformatuj ciąg znaków, aby wyświetlić wiadomość:
# „Twój wynik to 90.75!”
# Użyj metody formatowania lub sformatowanego ciągu

score = 90.75

print("Twój wynik to " + format(score))

# 2
# Użyj wyniku z punktu 1
# Wyświetl ten sam komunikat, ale określ formatowanie tak, aby wyświetlało trzy miejsca po przecinku.
# Oczekiwany wynik: „Twój wynik to 90.750!”

print("Twój wynik to: {:.3f}".format(score))


# 3
# Kilka lat temu 41737 programistów z 88615 korzystało z Pythona
# Wydrukuj ten ułamek jako procent z dokładnością do jednego miejsca po przecinku.
# Oczekiwany wynik: „47,1% programistów używa Pythona!”

value_percentage = float(float(41737/88615) * 100)
print("{:.1f}".format(value_percentage) + "% programistów używa Pythona!")




