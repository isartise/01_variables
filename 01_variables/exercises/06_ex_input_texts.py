# 1
# Zapytaj użytkownika o jego imię i nazwisko
# Następnie wydrukuj powitanie, używając jego imienia. Np. "Cześć John"
User_name = str(input("Provide your name:"))
User_surname = str(input("Provide your surname"))

print("Hello " + User_name)


# 2
# Zapytaj użytkownika o jego imię i nazwisko
# Następnie wydrukuj, ile liter ma jego/jej imię

User_name = str(input("Provide your name:"))
User_surname = str(input("Provide your surname"))

print("your name has " + str(len(User_name)) + " letters")
# 3
# Zapytaj użytkownika o login
# Następnie poproś o hasło i wydrukuj następujące wiadomości:
# Powitanie z loginem, np. „Witam, John”
# „Twoje hasło jest ukryte: #####”
# Użyj długości hasła, aby obliczyć, ile znaków „#” potrzebujesz

user_login = str(input("Provide your login:"))
user_password = str(input("Provide your password:"))

print("Hello " + user_login)
print("Your password is hidden: " + (len(user_password)) * "#")
