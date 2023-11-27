# 1
# Umieść swoje imię i nazwisko w zmiennej o nazwie user_name
user_name = "Izabela" + " " + "Grzelecka"
print(user_name)


# 2
# Utwórz adres e-mail na podstawie nazwy użytkownika, używając poniższej zmiennej, wydrukuj go w konsoli
# Przykład wyniku: "jan@gmail.com"

domain = "gmail.com"
at = "@"
user = "somebody"

email_adress = user + at + domain
print(email_adress)
# 3
# Powyższy e-mail nie jest unikalny
# Umieść swoje nazwisko w zmiennej o nazwie user_surname
# Utwórz adres e-mail na podstawie nazwy użytkownika, długości nazwiska i domeny, wydrukuj go na konsoli
# Użyj zmiennych, które masz
# Przykład wyniku: "jan9@gmail.com"

user_surname = "Grzelecka"
surname_length = len(user_surname)
email_adress = user_surname + str(surname_length) + at + domain
print(email_adress)
